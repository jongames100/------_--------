def xor_encrypt_decrypt(file_path, key):
    # Open the file for reading in binary mode
    file = open(file_path, 'rb')
    data = file.read()
    file.close()
    # Perform XOR operation on each byte
    encrypted_data = bytearray([]) #makes a binary array that everything in becomes binary
    for byte in data:
        encrypted_data.append(byte ^ key)
    
    # Open the file for writing in binary mode
    file = open(file_path, 'wb')#opens and makes it able to be change in binary
    file.write(encrypted_data)
    file.close()

xor_encrypt_decrypt("C:\\Users\\jongames100\Desktop\\testxor.txt", 5)