import binascii
import base64
import json
def encryptDecrypt(text, key):
    output = ""

    for i in range(len(text)):
        xor_num = ord(text[i]) ^ ord(key[i % len(key)])
        output += chr(xor_num)

    return ''.join(output)


def main():
    original_text = json.dumps({"showpassword": "yes", "bgcolor": "#ffffff"})
    key = "qw8J"

    encrypted_text = encryptDecrypt(original_text, key)
    final_text = base64.b64encode(encrypted_text)
    print final_text

    pass


if __name__ == '__main__':
    main()

