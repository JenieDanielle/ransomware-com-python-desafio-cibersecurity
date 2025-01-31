import os
import pyaes

#abrir arquivo criptografado

file_name = 'teste.txt.testeransomware'
file = open('file_name', 'rb')
file_data = file.read()
file.close()

#chave de criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remover arquivos criptografados

os.remove(file_name)

#criar um arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()