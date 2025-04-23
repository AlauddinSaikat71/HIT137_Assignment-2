def encrypt_text(text, n, m):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            if ch <= 'm':
                shift = (ord(ch) - ord('a') + n * m) % 13
                result.append(chr(ord('a') + shift))
            else:
                shift = (ord(ch) - ord('a') - (n + m)) % 13
                result.append(chr(ord('n') + shift))
        elif 'A' <= ch <= 'Z':
            if ch <= 'M':
                shift = (ord(ch) - ord('A') - n) % 13
                result.append(chr(ord('A') + shift))
            else:
                shift = (ord(ch) - ord('A') + (m ** 2)) % 13
                result.append(chr(ord('N') + shift))
        else:
            result.append(ch)
    return ''.join(result)

def decrypt_text(text, n, m):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            if ch <= 'm':
                shift = (ord(ch) - ord('a') - n * m) % 13
                result.append(chr(ord('a') + shift))
            else:
                shift = (ord(ch) - ord('a') + (n + m)) % 13
                result.append(chr(ord('n') + shift))
        elif 'A' <= ch <= 'Z':
            if ch <= 'M':
                shift = (ord(ch) - ord('A') + n) % 13
                result.append(chr(ord('A') + shift))
            else:
                shift = (ord(ch) - ord('A') - (m ** 2)) % 13
                result.append(chr(ord('N') + shift))
        else:
            result.append(ch)
    return ''.join(result)

def check_decryption(original, decrypted):
    # Just normalize line endings and trim extra whitespace
    original_clean = original.replace('\r\n', '\n').strip()
    decrypted_clean = decrypted.replace('\r\n', '\n').strip()
    return original_clean == decrypted_clean

def main():
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    # Read original text
    with open("raw_text.txt", "r", encoding='utf-8') as f:
        original_text = f.read()

    # Encrypt and write to file
    encrypted_text = encrypt_text(original_text, n, m)
    with open("encrypted_text.txt", "w", encoding='utf-8') as f:
        f.write(encrypted_text)

    # Decrypt and write to file
    decrypted_text = decrypt_text(encrypted_text, n, m)
    with open("decrypted_text.txt", "w", encoding='utf-8') as f:
        f.write(decrypted_text)

    # Print preview (first 300 characters only)
    print("\nOriginal Text:\n", original_text)
    print("\nEncrypted Text:\n", encrypted_text)
    print("\nDecrypted Text:\n", decrypted_text)
    print("\nDecryption successful:", check_decryption(original_text, decrypted_text))

if __name__ == "__main__":
    main()
