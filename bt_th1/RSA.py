
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad 
import time 
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
 
# Tạo cặp khóa RSA 
key = RSA.generate(2048) 
private_key = key.export_key() 
public_key = key.publickey().export_key() 
 
# Mã hóa khóa AES bằng khóa công khai RSA và đo thời gian 
aes_key = get_random_bytes(16) 
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key)) 
 
start_time = time.time()
encrypted_aes_key = cipher_rsa.encrypt(aes_key) 
end_time = time.time() 
rsa_encryption_time = end_time - start_time 
 
print("Khóa AES sau khi mã hóa bằng RSA:", encrypted_aes_key) 
print("Thời gian mã hóa RSA:", rsa_encryption_time, "giây") 
 
# Giải mã khóa AES bằng khóa bí mật RSA và đo thời gian 
decipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key)) 
 
start_time = time.time() 
decrypted_aes_key = decipher_rsa.decrypt(encrypted_aes_key) 
end_time = time.time() 
rsa_decryption_time = end_time - start_time 
 
print("Khóa AES sau khi giải mã:", decrypted_aes_key) 
print("Thời gian giải mã RSA:", rsa_decryption_time, "giây")