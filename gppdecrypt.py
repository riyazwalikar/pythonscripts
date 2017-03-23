import sys
import base64
from Crypto.Cipher import AES

unpad = lambda s : s[:-ord(s[-1])]

# AES Key - https://msdn.microsoft.com/en-us/library/cc422924.aspx
key = "\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b"

def decrypt(enc):
	pad = "=" * (4 - (len(enc) % 4))
	enc = base64.b64decode(enc + pad)
	iv = "\x00" * 16
	cipher = AES.new(key,AES.MODE_CBC,iv)
	print unpad(cipher.decrypt(enc)).decode('utf16')

if __name__ == "__main__":
	decrypt(sys.argv[1])