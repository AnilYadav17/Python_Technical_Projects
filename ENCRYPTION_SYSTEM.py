import base64
import hashlib

user_name = ""
user_pass = ""

login_success = False

history = ""

while True:

    print("\n========== CYBERSHIELD ENCRYPTION SYSTEM ==========")

    print("1 → Register")
    print("2 → Login")
    print("3 → Encrypt Message")
    print("4 → View Encryption History")
    print("5 → Logout")
    print("0 → Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        # REGISTER
        case 1:

            if user_name != "":
                print("Account already exists!")

            else:

                user_name = input("Create Username: ").lower()
                user_pass = input("Create Password: ")

                print("Registration Successful!")

        # LOGIN
        case 2:

            if login_success == True:
                print("Already logged in!")

            elif user_name == "":
                print("Please Register First!")

            else:

                attempts = 3

                while attempts > 0:

                    login_name = input("Enter Username: ").lower()
                    login_pass = input("Enter Password: ")

                    if (user_name, user_pass) == (login_name, login_pass):

                        print("Login Successful!")
                        login_success = True
                        break

                    else:

                        attempts -= 1

                        print("Invalid Credentials!")
                        print(f"{attempts} attempts left!")

                if login_success == False:
                    print("Maximum login attempts reached!")

        # ENCRYPT MESSAGE
        case 3:

            if login_success == False:
                print("Please Login and retry")

            else:

                text = input("\nEnter Message: ").upper()

                # CAESAR CIPHER
                shift = 3

                encrypted = ""

                for char in text:

                    if char.isalpha():

                        encrypted += chr(((ord(char) - 65 + shift) % 26) + 65)

                    else:

                        encrypted += char

                print(f"\nCaesar Cipher : {encrypted}")

                # REVERSE CIPHER
                reverse_text = encrypted[::-1]

                print(f"Reverse Cipher: {reverse_text}")

                # BASE64 ENCODING
                base64_text = base64.b64encode(reverse_text.encode()).decode()

                print(f"Base64 Encode : {base64_text}")

                # SHA256 HASHING
                hash_text = hashlib.sha256(base64_text.encode()).hexdigest()

                print(f"SHA256 Hash   : {hash_text}")

                # HISTORY
                history += "\nOriginal Message : " + text
                history += "\nEncrypted Output : " + hash_text
                history += "\n--------------------------------"

                print("\nMessage Encrypted Successfully!")

        # HISTORY
        case 4:

            if login_success == False:
                print("Please Login and retry")

            else:

                print("\n========== ENCRYPTION HISTORY ==========")

                if history == "":
                    print("No encryption history found!")

                else:
                    print(history)

        # LOGOUT
        case 5:

            if login_success == False:
                print("Already logged out!")

            else:

                login_success = False

                print("Successfully Logged Out!")

        # EXIT
        case 0:

            print("Exiting CyberShield Encryption System")
            print("Thank You!")
            break

        # INVALID
        case _:

            print("Invalid Choice!")