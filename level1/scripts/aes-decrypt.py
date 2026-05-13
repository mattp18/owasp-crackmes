from Crypto.Cipher import AES
import base64

key = bytes.fromhex("8d127684cbc37c17616d806cf50473cc")
ciphertext = base64.b64decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=")

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# 4. Remove PKCS7 padding
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

# 5. Print result
print("Raw bytes:", plaintext)
print("Secret:", plaintext.decode("utf-8"))