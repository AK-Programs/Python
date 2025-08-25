# Message Encrypter & Decrypter

# You can encrypt & decrypt messages and those will be saved in the encrypted message file.
# Make sure to create a characters.txt file and write the following content in it. (Don't copy # which is in the starting.):
    # chars:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    # key: F4kA9qRlt#8Gyb7aPpVEoIuYd3nH2xCvB1mJ0rTzS5eXc6wLgMf!@hsUjZKiN$Q%D^&*()_-+={}O|[]\:;"'<W,>.?/~`
# Make sure to create a encrpted_messages.txt file
# You will be prompt for your choice.
# If any problem is there in this code, then contact me via whatsapp.
# Enjoy secret message encrypting!
# Double click '❤️', if you like it!

def load_chars_and_key(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("chars: "):
                chars = line.split("chars: ")[1].strip()
            elif line.startswith("key: "):
                key = line.split("key: ")[1].strip()
    return chars, key

def encrypt_message(chars, key, message): 
    encrypted_message = ""
    for letter in message:
        if letter in chars:
            index = chars.index(letter)
            encrypted_message += key[index]
        else:
            encrypted_message += letter  # Handle characters not in chars
    return encrypted_message

def decrypt_message(chars, key, message): # type: ignore
    decrypted_message = ""
    for letter in message:
        if letter in key:
            index = key.index(letter)
            decrypted_message += chars[index] # type: ignore
        else:
            decrypted_message += letter  # type: ignore # Handle characters not in key
    return decrypted_message # type: ignore

def view_encrypted_messages():
    with open(r"F:\Personal Files\Naitik\Coding\Projects\Project-1 (Python)\encrypted_messages.txt", "r") as file:
        messages = file.readlines()
        if messages:
            index = 1  
            for message in messages:
                print(f"{index}. {message.strip()}")
                index += 1  
        else:
            print("No encrypted message.")

def clear_encrypted_messages():
    open(r"F:\Personal Files\Naitik\Coding\Projects\Project-1 (Python)\encrypted_messages.txt", "w").close()  # Clear the file
    print("Encrypted messages cleared.")

def main():
    file_path = r"F:\Personal Files\Naitik\Coding\Projects\Project-1 (Python)\characters.txt"
    chars, key = load_chars_and_key(file_path)
   
    while True:
        work = input("What would you like to do?\nEncrypt a message (A)\nDecrypt a message (S)\nView encrypted messages (D)\nClear encrypted messages (W)\nExit (Q)\nYour choice: ").lower()
       
        if work == "a":
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(chars, key, message)
            with open(r"F:\Personal Files\Naitik\Coding\Projects\Project-1 (Python)\encrypted_messages.txt", "a") as file:
                file.write(f"{encrypted_message}\n")
            print(encrypted_message)
        elif work == "s":
            message = input("Enter the message to decrypt: ")
            decrypted_message = decrypt_message(chars, key, message)
            print(f"{decrypted_message}")
        elif work == "d":
           view_encrypted_messages()
        elif work == "w":
            clear_encrypted_messages()  # Assuming a different file for encrypted messages
        elif work == "q":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()