def matmul(keymat, msgmat):
    result = []

    for i in range(3):
        result.append(keymat[i][0]*msgmat[0] + keymat[i][1]*msgmat[1] + keymat[i][2]*msgmat[2])

    return result

msg = input("Enter the message: ").upper()
key = input("Enter the key: ").upper()

keymat = [ord(c) - 65 for c in key]
keymat = [keymat[i:i+3] for i in range(0, len(keymat), 3)]

msgmat = [ord(c) - ord('A') for c in msg]
msgmat = [msgmat[i:i+3] for i in range(0, len(msgmat), 3)]

cipmsg = []

for i in msgmat:
    cipmsg.extend([num%26 for num in matmul(keymat,i)])

ciphertext = "".join([chr(i+65) for i in cipmsg])

print(f"Original message: {msg}\nEncrypted message: {ciphertext}")
