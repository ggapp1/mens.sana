def encrypt(key, text):
    ciphertext = []
    for i, c in enumerate(text):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        ciphertext.append(chr((msg_c + key_c) % 127))
    return ''.join(ciphertext)

def decrypt(key, text):
    decrypted_text = []
    for i, c in enumerate(text):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        decrypted_text.append(chr((enc_c - key_c) % 127))
    return ''.join(decrypted_text)
