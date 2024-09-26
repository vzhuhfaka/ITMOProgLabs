def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
    for symbol in plaintext:
        unicode_index = ord(symbol)
        if symbol in alphabet or symbol in alphabet.upper():
            if symbol in alphabet:
                if unicode_index + shift > 122:
                    unicode_index = unicode_index + shift - 26
                else:
                    unicode_index += shift
                ciphertext += chr(unicode_index)
            else:
                if unicode_index + shift > 90:
                    unicode_index = unicode_index + shift - 26
                else:
                    unicode_index += shift
                ciphertext += chr(unicode_index)
        else:
            ciphertext += chr(unicode_index)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
    for symbol in ciphertext:
        unicode_index = ord(symbol)
        if symbol in alphabet or symbol in alphabet.upper():
            if symbol in alphabet:
                if unicode_index - shift < 97:
                    unicode_index = unicode_index - shift + 26
                else:
                    unicode_index -= shift
                plaintext += chr(unicode_index)
            else:
                if unicode_index - shift < 65:
                    unicode_index = unicode_index - shift + 26
                else:
                    unicode_index -= shift
                plaintext += chr(unicode_index)
        else:
            plaintext += chr(unicode_index)

    return plaintext
