from adv_lib.attacks import sigma_zero
import torch
from torch import Tensor, nn
from torch.autograd import grad
import torchvision
from PIL import Image
import math

def sigma_zero(model: nn.Module,
               inputs: Tensor,
               labels: Tensor,
               num_steps: int = 3000,
               n0: float = 1.0,
               s: float = 0.001,
               t0: float = 0.3,
               t_factor: float = 0.01,
               grad_norm: float = float('inf')) -> Tensor:

    batch_size, numel = len(inputs), inputs[0].numel()
    batch_view = lambda tensor: tensor.view(batch_size, *[1] * (inputs.ndim - 1))

    d = torch.zeros_like(inputs, requires_grad=True)
    # Adam variables
    exp_avg = torch.zeros_like(inputs)
    exp_avg_sq = torch.zeros_like(inputs)
    b1, b2 = 0.9, 0.999

    best_l0 = inputs.new_full((batch_size,), numel)
    best_adv = inputs.clone()
    t = torch.full_like(best_l0, t0)

    n = n0
    for i in range(num_steps):
        adv_inputs = inputs + d

        # compute loss
        logits = model(adv_inputs)
        dl_loss = nn.BCEWithLogitsLoss()(logits, labels.unsqueeze(0))
        d_square = d.square()
        l0_approx_normalized = (d_square / (d_square + s)).flatten(1).mean(dim=1)

        # keep best solutions
        predicted_classes = (logits > 0).float().squeeze()
        l0_norm = d.data.flatten(1).norm(p=0, dim=1)

        is_adv = predicted_classes != labels
        is_smaller = l0_norm < best_l0
        is_both = is_adv & is_smaller
        best_l0 = torch.where(is_both, l0_norm, best_l0)
        best_adv = torch.where(batch_view(is_both), adv_inputs.detach(), best_adv)

        # compute loss and gradient
        adv_loss = (-dl_loss + l0_approx_normalized).sum()
        d_grad = grad(adv_loss, inputs=d, only_inputs=True)[0]

        # normalize gradient based on grad_norm type
        d_inf_norm = d_grad.flatten(1).norm(p=grad_norm, dim=1).clamp_(min=1e-12)
        d_grad.div_(batch_view(d_inf_norm))

        # adam computations
        exp_avg.lerp_(d_grad, weight=1 - b1)
        exp_avg_sq.mul_(b2).addcmul_(d_grad, d_grad, value=1 - b2)
        bias_correction1 = 1 - b1 ** (i + 1)
        bias_correction2 = 1 - b2 ** (i + 1)
        denom = exp_avg_sq.sqrt().div_(bias_correction2 ** 0.5).add_(1e-8)

        # step and clamp
        d.data.addcdiv_(exp_avg, denom, value=-n / bias_correction1)
        d.data.add_(inputs).clamp_(min=0, max=1).sub_(inputs)

        # update step size with cosine annealing
        n = 0.1 * n0 + 0.9 * n0 * (1 + math.cos(math.pi * i / num_steps)) / 2
        # dynamic thresholding
        t.add_(torch.where(is_adv, t_factor * n, -t_factor * n)).clamp_(min=0, max=1)

        # filter components
        d.data[d.data.abs() < batch_view(t)] = 0

    return best_adv

model = torchvision.models.resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, 1)
model.load_state_dict(torch.load("model.pt"))

worm = Image.open("worm.png")
worm = torchvision.transforms.ToTensor()(worm).unsqueeze(0)

y = model(worm)

out = sigma_zero(model, worm, torch.tensor([1], dtype=torch.float32))

Image.fromarray((out.squeeze().detach().numpy() * 255).astype("uint8").transpose(1, 2, 0)).save("out.png")

y = model(out)
print(torch.sigmoid(y))

out = (out * 255).int().squeeze().transpose(0, 1).transpose(1, 2)
worm = (worm * 255).int().squeeze().transpose(0, 1).transpose(1, 2)
print(torch.count_nonzero(out - worm))

nonzeroCoords = torch.nonzero(out - worm)
print(nonzeroCoords)
for coord in nonzeroCoords:
    print(f"{coord[1].item()},{coord[0].item()},{out[coord[0], coord[1], 0].item()},{out[coord[0], coord[1], 1].item()},{out[coord[0], coord[1], 2].item()}", end=";")