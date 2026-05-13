user_id=""
user_pass=""
atm_pin=0
balance=0
login_success = False
mini_statement= ""
count=0
todays_limit=100000
total_rewards = 0

while True:
    print("\n========== SMART ATM SYTEM ==========\n1 → Register\n2 → Login\n3 → Deposit Money\n4 → Withdraw Money\n5 → Check Balance\n6 → Mini Statement\n7 → Change PIN\n8 → Cashback Rewards\n9 → Logout\n0 → Exit")
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            user_id = input("Enter User Id: ").lower()
            user_pass = input("Enter User Password: ")
            atm_pin = int(input("Enter ATM PIN: "))
            balance = float(input("Enter Inital Amount: "))
            deposit = balance
            count+=1
            mini_statement = mini_statement + "\n"+str(count)+". Initialy_Deposited: " + str(deposit)+"$"
            if deposit>=10000:
                I_reward =deposit/50
                total_rewards += I_reward
                balance+=I_reward
                count+=1
                mini_statement = mini_statement + "\n"+str(count)+". Cashback Reward: " + str(I_reward)+"$"
                print("Congratulations! , 2% Cashback added!")
            else:
                print("Deposit atleast 10,000$, to get 2% cashback")
        case 2:
            if login_success==True:
                print("You are already logged in!")

            elif user_id == "":
                print("Please Register!")

            else:
                attempts = 3
                login_success = False

                while attempts > 0:

                    user1_id = input("Enter User Id: ").lower()
                    user1_pass = input("Enter User Password: ")
                    atm1_pin = int(input("Enter ATM PIN: "))

                    if (user_id, user_pass, atm_pin) == (user1_id, user1_pass, atm1_pin):

                        print("Login successful, You can proceed...")
                        login_success = True
                        break

                    else:
                        attempts -= 1
                        print(f"\nInvalid Credentials\n{attempts} attempts left!")

                if not login_success:
                    print("\nMaximum limit of attempts reached!")
                    print("Thank You for Visiting.")
                    break
        case 3:
            if login_success==False:
                print("Please Login and retry")
            else:
                deposit = float(input("Enter amount to Deposit: $"))
                balance+=deposit
                print(f"Successfully deposited {deposit}$ :)")
                count+=1
                mini_statement = mini_statement + "\n"+str(count)+". Deposited: " + str(deposit)+"$"
                if deposit>=10000:
                    print("Congratulations , 2% Cashback added!")
                    D_reward = deposit/50
                    total_rewards += D_reward
                    balance+=D_reward
                    count+=1
                    mini_statement = mini_statement + "\n"+str(count)+". Cashback Reward: " + str(D_reward)+"$"        
        case 4:
            if login_success==False:
                print("Please Login and retry")
            else:
                withdraw = float(input("Enter amount to Withdraw: $"))
                if withdraw > balance:
                    print("Insufficient balance.\nPlease recheck your amount!")

                elif withdraw > todays_limit:
                    print("Maximum withdrawal limit reached for today!")

                else:
                    balance -= withdraw
                    todays_limit -= withdraw

                    count += 1

                    mini_statement += "\n" + str(count) + ". Withdrawed: " + str(withdraw) + "$"

                    print(f"Successfully withdrawed {withdraw}$ ;)")
        case 5:
            if login_success==False:
                print("Please Login and retry")
            else:
                print(f"Balance: {balance}")
        case 6:
            if login_success==False:
                print("Please Login and retry")
            else:
                print("\n-----Mini Statement------",mini_statement)
        case 7:
            if login_success==False:
                print("Please Login and retry")
            else:
                pin_attempts=3
                while pin_attempts>0:
                    current_pin = int(input("Enter Current PIN: "))
                    if atm_pin==current_pin:
                        new_pin= int(input("Enter New PIN: "))
                        atm_pin = new_pin
                        print("PIN successfully updated!")
                        break
                    else:
                        pin_attempts-=1
                        print(f"Please Enter valid PIN\n{pin_attempts} attempts left!")
                if pin_attempts==0:
                    print("Invalid Login detected!")
                    break
        case 8:
            if login_success == False:
                print("Please Login and retry")

            else:
                print("\n----- Cashback Rewards -----")
                print(f"Total Cashback Earned: {total_rewards}$")
        case 9:
            if login_success == False:
                print("No active session found!")

            else:
                login_success = False
                print("Logged out successfully!")

                withdraw = 0
                deposit = 0
        case 0:
            print("\nSaving Session...")
            print("Exiting Smart ATM System")
            print("Thank You for Visiting!")
            break
        case _:
            print("Please enter valid choice")