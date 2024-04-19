from padding_oracle import IV,CT,BLOCKSIZE,check_ct
from Crypto.Random import get_random_bytes



# Finds str1^str2 
def xor(str1,str2):

    xored = bytes(a ^ b for a, b in zip(bytes.fromhex(str1), bytes.fromhex(str2)))
    xored_str = xored.hex()
   
    return xored_str



def attack_block(CT1,CT2):

    I_block2 = '' # intermediate step
    P_block2 = '' # plaintext block2
    ct_block1 = CT1
    ct_block2 = CT2

    for i in range(0,BLOCKSIZE):
        
        i1 = BLOCKSIZE-i-1 # block starting byte
        i2 = BLOCKSIZE-i # block ending byte
        
        padding_byte = ('0' if i+1 < 0x10 else '')+hex(i+1)[2:]
        padding_block2 = padding_byte*(i+1)
    
        # trying different bytes
        for j in range(0x000,0x100):
            
            prefix = get_random_bytes(i1).hex() 
            attempt = ('0' if j < 0x10 else '')+hex(j)[2:] 
            suffix = xor(I_block2,padding_block2[2:])

            ctp_block1 = prefix+attempt+suffix
            ctp = ctp_block1+ct_block2
            
            if check_ct(ctp):

                I_byte = xor(padding_byte,attempt)
                I_block2 = I_byte+I_block2

                P_byte = xor(CT1[2*i1:2*i2],I_byte)
                P_block2 = P_byte+P_block2

                break

    return P_block2

def attack(CT):

    global BLOCKSIZE, IV

    pt = ''
    # 32, # 0
    for i in range(len(CT)-2*BLOCKSIZE,-1,-2*BLOCKSIZE):
       
        i1 = i-2*BLOCKSIZE
        i2 = i
        i3 = i+2*BLOCKSIZE
      
        block1 = IV.hex() if i1 < 0 else CT[i1:i2]
        block2 = CT[i2:i3]

        pt = attack_block(block1,block2)+pt

    pt = bytes.fromhex(pt).decode()
    return pt
        
   

print(attack(CT))