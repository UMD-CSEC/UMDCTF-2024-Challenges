from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import socket
import string
import time



KEY = bytes.fromhex('262d0f6261daf5fda4036d8526b2c017')
IV = bytes.fromhex('2652b7ae08b281594c488cf2e6daee43')
MODE = AES.MODE_CBC
FLAG = 'umdctf{I_l0vE_p@dINg_0rAClE_@tTacKS}'

HOST = 'localhost'
PORT = 12345



def pad(m):

    len_m = len(m)//2 # byte length
    extra_bytes = 16-(len_m%16)

    if extra_bytes == 0:

        padding = extra_bytes*(hex(extra_bytes)[2:])

    else:

        padding = extra_bytes*('0'+hex(extra_bytes)[2:])
    
    return m+padding

def encrypt(pt):

    global KEY, IV, MODE

    cipher = AES.new(key=KEY, iv=IV, mode=MODE)
    ct = cipher.encrypt(pt)
    
    ct_hex = ct.hex()
    ct_hex = '0'*(len(ct_hex)%16)+ct_hex
    return ct.hex()



# checks if byte array pt has valid PKCS#7 padding
def valid_padding(pt): 
   
    last_byte = pt[-1:]
    
    repeat = int(last_byte.hex(),16)
  
    if repeat == 0 or repeat > 16:

        return False
    
    else: # check padding
        
        expected_padding = last_byte*repeat
        actual_padding = pt[-repeat:]

        return (actual_padding  == expected_padding)

# checks if decrypted ct has valid PKCS#7 padding
def check_ct(ct):

    global KEY, IV, MODE

    ct = bytes.fromhex(ct)

    cipher = AES.new(key=KEY, iv=IV, mode=MODE)
    return valid_padding(cipher.decrypt(ct))



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:

        conn.sendall(b'welcome!!\n')

        while True:

            conn.sendall(b'give me a ciphertext and I\'ll tell you if the corresponding plaintext has valid padding\n')
            
            data = conn.recv(4*16*8)
            data = data.decode("utf-8")
            data = data[:-1]
            resp = None
  
            if len(data) != 2*2*16:

                resp = 'wrong ciphertext size!\n'
            
            elif not all(c in string.hexdigits for c in data):

                resp = 'invalid ciphertext format!\n'

            elif check_ct(data):

                resp = 'valid padding :)\n'

            elif not check_ct(data):

                resp = 'invalid padding :(\n'

            else:

                resp = 'wrong ciphertext format!\n'

            conn.sendall(resp.encode('utf-8'))
            conn.sendall(b'\n\n\n')
            time.sleep(.5)
            
    