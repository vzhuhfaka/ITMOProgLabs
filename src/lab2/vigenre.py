from pydoc import plain


def fill_str(string, lenght):
    a = lenght / len(string)
    res = string * int(a)
    a = lenght - len(res)
    return res + string[0:a]


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
    for symbol_index in range(0, len(plaintext)):
        symbol = plaintext[symbol_index]
        unicode_index = ord(symbol)
        if symbol in alphabet or symbol in alphabet.upper():
            if symbol in alphabet:
                shift = ord(fill_str(keyword, len(plaintext))[symbol_index]) - 97
                if unicode_index + shift > 122:
                    unicode_index = unicode_index + shift - 26
                else:
                    unicode_index += shift
                ciphertext += chr(unicode_index)
            else:
                shift = ord(fill_str(keyword, len(plaintext))[symbol_index]) - 65
                if unicode_index + shift > 90:
                    unicode_index = unicode_index + shift - 26
                else:
                    unicode_index += shift
                ciphertext += chr(unicode_index)
        else:
            ciphertext += chr(unicode_index)

    return ciphertext

print(encrypt_vigenere('Hello world!', 'dnj'))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
    for symbol_index in range(0, len(ciphertext)):
        symbol = ciphertext[symbol_index]
        unicode_index = ord(symbol)
        if symbol in alphabet or symbol in alphabet.upper():
            if symbol in alphabet:
                shift = ord(fill_str(keyword, len(ciphertext))[symbol_index]) - 97
                if unicode_index - shift < 97:
                    unicode_index = unicode_index - shift + 26
                else:
                    unicode_index -= shift
                plaintext += chr(unicode_index)
            else:
                shift = ord(fill_str(keyword, len(ciphertext))[symbol_index]) - 65
                if unicode_index - shift < 65:
                    unicode_index = unicode_index - shift + 26
                else:
                    unicode_index -= shift
                plaintext += chr(unicode_index)
        else:
            plaintext += chr(unicode_index)
    return plaintext