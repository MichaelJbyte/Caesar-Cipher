
import time

print("------------------------------------")
print("Welcome to the Caesar Cipher Program")
print("------------------------------------")


def encrypt_cipher(plain_text, shift):
    # Encrypts text using a Caesar cipher shift.
    cipher_text = ""

    for char in plain_text:
        if "a" <= char <= "z":
            shifted_text = ord("a") + (ord(char) - ord("a") + shift) % 26
            cipher_text += chr(shifted_text)
        else:
            cipher_text += char  # if no else, return would kill for loop | keeps spaces

    return cipher_text


def decrypt_cipher(cipher_text, shift):
    # Decrypts cipher text
    plain_text = ""

    for char in cipher_text:
        if "a" <= char <= "z":
            shifted_text = ord("a") + (ord(char) - ord("a") - shift) % 26
            plain_text += chr(shifted_text)
        else:
            plain_text += char

    return plain_text


def main():

    is_running = True

    while is_running:

        while True:
            decision = input(
                "Would you like to encrypt or decrypt?: ").strip().lower()
            if decision in ("encrypt", "decrypt"):
                break
            else:
                print("Invalid input. Please type 'encrypt' or 'decrypt'.")

        if decision == "encrypt":
            while True:  # input validation
                plain_text = input(
                    "Enter the phrase you would like to encrypt: ").lower()

                if all(c.isalpha() or c.isspace() for c in plain_text):
                    break

                print("Please enter a PROPER phrase (Letters and Spaces Only).")

            while True:  # input validation
                try:
                    shift = int(input("Enter the shift amount (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Please enter a PROPER number (1-25).")
                except ValueError:
                    print("Please enter a PROPER number (1-25).")

            print("________________\nEncrypting text...")
            time.sleep(2)
            print(
                f"________________\nEncrypted Text: {encrypt_cipher(plain_text, shift)}")

        elif decision == "decrypt":
            while True:  # input validation
                cipher_text = input(
                    "Enter the phrase you would like to decrypt: ").lower()

                if all(c.isalpha() or c.isspace() for c in cipher_text):
                    break

                print("Please enter a PROPER phrase (Letters and Spaces Only).")

            while True:  # input validation
                try:
                    shift = int(input("Enter the shift amount (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Please enter a PROPER number (1-25).")
                except ValueError:
                    print("Please enter a PROPER number (1-25).")

            print("________________\nDecrypting text...")
            time.sleep(2)
            print(
                f"________________\nDecrypted Text: {decrypt_cipher(cipher_text, shift)}")

        try_again = input(
            "Would you like to run this program again? (Y/N): ").strip().upper()
        if try_again == "Y":
            continue  # may be problem with 2nd round
        else:
            is_running = False
            print("------------------------------------")
            print("Thank you for using the Caesar Cipher Program!")
            print("------------------------------------")


if __name__ == "__main__":
    main()
