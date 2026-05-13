user_name = ""
user_pass = ""
login_success = False

score = 0
attempted = 0
correct_answers = 0
wrong_answers = 0

quiz_history = ""

while True:

    print("\n========== SMART QUIZ CHALLENGE SYSTEM ==========")

    print("1 → Register")
    print("2 → Login")
    print("3 → Start Quiz")
    print("4 → View Score")
    print("5 → Quiz History")
    print("6 → Reset Score")
    print("7 → Logout")
    print("0 → Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        # REGISTER
        case 1:

            if user_name != "":
                print("Account already registered!")

            else:
                user_name = input("Create Username: ").lower()
                user_pass = input("Create Password: ")

                print("Registration Successful!")

        # LOGIN
        case 2:

            if login_success == True:
                print("You are already logged in!")

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

                        print(f"Invalid Credentials")
                        print(f"{attempts} attempts left!")

                if login_success == False:
                    print("Maximum login attempts reached!")

        # START QUIZ
        case 3:

            if login_success == False:
                print("Please Login and retry")

            else:

                print("\n========== QUIZ STARTED ==========")

                # QUESTION 1
                print("\nQ1. What is Duck Number?")

                print("1. Number starting with zero")
                print("2. Number containing zero")
                print("3. Prime Number")
                print("4. Palindrome Number")

                ans1 = int(input("Enter option: "))

                attempted += 1

                if ans1 == 2:

                    print("Correct Answer!")

                    score += 1
                    correct_answers += 1

                    quiz_history += "\nQ1 Correct"

                else:

                    print("Wrong Answer!")

                    wrong_answers += 1

                    quiz_history += "\nQ1 Wrong"

                # QUESTION 2
                print("\nQ2. What is Tech Number?")

                print("1. Number divisible by 2")
                print("2. Number having even digits")
                print("3. Number whose split sum square equals original")
                print("4. Prime Number")

                ans2 = int(input("Enter option: "))

                attempted += 1

                if ans2 == 3:

                    print("Correct Answer!")

                    score += 1
                    correct_answers += 1

                    quiz_history += "\nQ2 Correct"

                else:

                    print("Wrong Answer!")

                    wrong_answers += 1

                    quiz_history += "\nQ2 Wrong"

                # QUESTION 3
                print("\nQ3. Which loop is infinite?")

                print("1. while True")
                print("2. for")
                print("3. if")
                print("4. else")

                ans3 = int(input("Enter option: "))

                attempted += 1

                if ans3 == 1:

                    print("Correct Answer!")

                    score += 1
                    correct_answers += 1

                    quiz_history += "\nQ3 Correct"

                else:

                    print("Wrong Answer!")

                    wrong_answers += 1

                    quiz_history += "\nQ3 Wrong"

                print("\nQuiz Completed!")

        # VIEW SCORE
        case 4:

            if login_success == False:
                print("Please Login and retry")

            else:

                print("\n========== SCORE BOARD ==========")

                print(f"Questions Attempted : {attempted}")
                print(f"Correct Answers     : {correct_answers}")
                print(f"Wrong Answers       : {wrong_answers}")
                print(f"Final Score         : {score}")

                if score >= 3:
                    print("Performance : Excellent")

                elif score == 2:
                    print("Performance : Good")

                else:
                    print("Performance : Needs Improvement")

        # QUIZ HISTORY
        case 5:

            if login_success == False:
                print("Please Login and retry")

            else:

                print("\n========== QUIZ HISTORY ==========")

                if quiz_history == "":
                    print("No quiz attempted yet!")

                else:
                    print(quiz_history)

        # RESET SCORE
        case 6:

            if login_success == False:
                print("Please Login and retry")

            else:

                score = 0
                attempted = 0
                correct_answers = 0
                wrong_answers = 0
                quiz_history = ""

                print("Quiz score reset successfully!")

        # LOGOUT
        case 7:

            if login_success == False:
                print("You are already logged out!")

            else:

                login_success = False

                print("Successfully Logged Out!")

        # EXIT
        case 0:

            print("Thank You for Using Smart Quiz Challenge System")
            break

        # INVALID CHOICE
        case _:

            print("Invalid choice! Please try again.")