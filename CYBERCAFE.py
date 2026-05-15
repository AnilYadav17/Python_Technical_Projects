user_id = ""
user_pass = ""

wallet = 0
login_success = False
session_active = False

history = ""

count = 0
reward_points = 0

while True:

    print("\n========== SMART CYBER CAFE SYSTEM ==========")
    print("1 → Register")
    print("2 → Login")
    print("3 → Start Session")
    print("4 → End Session")
    print("5 → Add Wallet Balance")
    print("6 → Check Wallet")
    print("7 → Session History")
    print("8 → Change Password")
    print("9 → Reward Points")
    print("10 → Logout")
    print("0 → Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        case 1:

            if user_id != "":
                print("Account already exists!")

            else:

                user_id = input("Create Username: ").lower()
                user_pass = input("Create Password: ")

                wallet = float(input("Add Starting Balance: $"))

                count += 1
                history += "\n" + str(count) + ". Account Registered"

                print("Registration Successful!")

        case 2:

            if login_success == True:
                print("Already Logged In!")

            elif user_id == "":
                print("Please Register First!")

            else:

                attempts = 3

                while attempts > 0:

                    login_id = input("Enter Username: ").lower()
                    login_pass = input("Enter Password: ")

                    if (user_id, user_pass) == (login_id, login_pass):

                        login_success = True

                        print("Login Successful!")
                        break

                    else:

                        attempts -= 1

                        print(f"Invalid Credentials")
                        print(f"{attempts} attempts left!")

                if login_success == False:
                    print("Maximum attempts reached!")

        case 3:

            if login_success == False:
                print("Please Login First!")

            elif session_active == True:
                print("Session already running!")

            else:

                print("\n===== SESSION MENU =====")
                print("1 → 1 Hour  = 50$")
                print("2 → 2 Hours = 100$")
                print("3 → 5 Hours = 200$")

                session = int(input("Select Session: "))

                if session == 1:

                    amount = 50
                    session_name = "1 Hour Session"

                elif session == 2:

                    amount = 100
                    session_name = "2 Hour Session"

                elif session == 3:

                    amount = 200
                    session_name = "5 Hour Session"

                else:

                    print("Invalid Session!")
                    continue

                if wallet < amount:
                    print("Insufficient Wallet Balance!")

                else:

                    wallet -= amount
                    session_active = True

                    reward = amount // 10
                    reward_points += reward

                    count += 1
                    history += "\n" + str(count) + ". Started " + session_name

                    print(f"{session_name} Started Successfully!")
                    print(f"{amount}$ Deducted")
                    print(f"{reward} Reward Points Added")

        case 4:

            if login_success == False:
                print("Please Login First!")

            elif session_active == False:
                print("No Active Session!")

            else:

                session_active = False

                count += 1
                history += "\n" + str(count) + ". Session Ended"

                print("Session Ended Successfully!")

        case 5:

            if login_success == False:
                print("Please Login First!")

            else:

                recharge = float(input("Enter Recharge Amount: $"))

                wallet += recharge

                count += 1
                history += "\n" + str(count) + ". Wallet Recharged: " + str(recharge) + "$"

                print(f"{recharge}$ Added Successfully!")

                if recharge >= 1000:

                    bonus = recharge / 20

                    wallet += bonus

                    count += 1
                    history += "\n" + str(count) + ". Bonus Added: " + str(bonus) + "$"

                    print(f"Bonus {bonus}$ Added!")

        case 6:

            if login_success == False:
                print("Please Login First!")

            else:

                print(f"\nWallet Balance: {wallet}$")

        case 7:

            if login_success == False:
                print("Please Login First!")

            else:

                print("\n===== SESSION HISTORY =====")

                if history == "":
                    print("No History Found!")

                else:
                    print(history)

        case 8:

            if login_success == False:
                print("Please Login First!")

            else:

                attempts = 3

                while attempts > 0:

                    old_pass = input("Enter Current Password: ")

                    if old_pass == user_pass:

                        new_pass = input("Enter New Password: ")

                        user_pass = new_pass

                        print("Password Changed Successfully!")
                        break

                    else:

                        attempts -= 1

                        print(f"Wrong Password")
                        print(f"{attempts} attempts left!")

                if attempts == 0:
                    print("Security Warning Detected!")

        case 9:

            if login_success == False:
                print("Please Login First!")

            else:

                print(f"\nTotal Reward Points: {reward_points}")

        case 10:

            if login_success == False:
                print("Already Logged Out!")

            else:

                login_success = False
                session_active = False

                print("Logged Out Successfully!")

        case 0:

            print("\nSaving Session...")
            print("Exiting Smart Cyber Cafe System")
            print("Thank You For Visiting!")
            break

        case _:

            print("Invalid Choice! Please Try Again.")
