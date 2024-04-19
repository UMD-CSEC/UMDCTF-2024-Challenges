from Crypto.Cipher import AES



BLOCKSIZE = 16 # aes128, blocksize is 16 bytes
KEY = bytes.fromhex('02'*BLOCKSIZE)
IV = bytes.fromhex('00'*BLOCKSIZE) # iv 16 characters long
MODE = AES.MODE_CBC
FLAG = b'umdctf{I_l0vE_p@dINg_0rAClE_@tTacKS}'
PT = FLAG+bytes.fromhex('00'*(len(FLAG)%BLOCKSIZE))



def encrypt(pt):

    global KEY, IV, MODE

    cipher = AES.new(key=KEY, iv=IV, mode=MODE)
    ct = cipher.encrypt(pt)
    
    ct_hex = ct.hex()
    ct_hex = '0'*(len(ct_hex)%BLOCKSIZE)+ct_hex
    return ct.hex()

# checks if byte array pt has valid PKCS#7 padding
def valid_padding(pt): 
   
    last_byte = pt[-1:]
    
    repeat = int(last_byte.hex(),16)
  
    if repeat == 0 or repeat > BLOCKSIZE:

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



CT = encrypt(PT)
print(CT)