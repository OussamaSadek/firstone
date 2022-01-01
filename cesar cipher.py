alphabets = "abcdefghijklmnopqrstuvwxyz"
choise = input("envrypt=1/decrypt=2: ")
message = input("Enter the message: ")
encrypt = ""
decrypt = ""
key = 3
if choise == "1":
    for letter in message:
        new_position = (alphabets.find(letter)+key) % len(alphabets)
        encrypt += alphabets[new_position]
    print("Encrypted message:", encrypt)
if choise == "2":
    for letter in message:
        new_pos = (alphabets.find(letter)-key) % len(alphabets)
        decrypt += alphabets[new_pos]
    print("Decrypted message:", decrypt)
