# =======================================================
# EXPERT SYSTEM: IT Help Desk Management
# Description: A rule-based system using IF-THEN logic
# =======================================================

def get_solution(problem_code):
    """
    This function acts as the Knowledge Base and Inference Engine.
    It takes the user's problem code and returns the appropriate solution.
    """
    if problem_code == '1':
        return "SOLUTION: Go to the login portal, click 'Forgot Password', and enter your email."
        
    elif problem_code == '2':
        return "SOLUTION: Check if your router is on. Restart it and wait for the green light."
        
    elif problem_code == '3':
        return "SOLUTION: Your hard drive might be full, or you have too many apps open. Clear your temp files."
        
    elif problem_code == '4':
        return "SOLUTION: Press and hold the power button for 10 seconds to force a hard reset."
        
    elif problem_code == '5':
        return "SOLUTION: Ensure the printer is turned on, has paper, and is on the same Wi-Fi network."
        
    else:
        return "ERROR: Invalid input. Please select a valid number from the menu."

def main():
    """
    This is the main loop that provides the User Interface.
    """
    print("*" * 50)
    print("   WELCOME TO THE IT HELP DESK EXPERT SYSTEM   ")
    print("*" * 50)
    
    # The while loop keeps the program running until the user types '0'
    while True:
        print("\nWhat kind of problem are you facing?")
        print("1. Cannot log into my account")
        print("2. Internet/Wi-Fi is not connecting")
        print("3. Computer is running very slow")
        print("4. Screen is frozen (Blue Screen)")
        print("5. Printer is not printing")
        print("0. EXIT the system")
        print("-" * 50)
        
        # Take input from the user
        user_choice = input("Enter the number of your problem (0-5): ")
        
        # Check if the user wants to exit
        if user_choice == '0':
            print("Thank you for using the IT Help Desk. Goodbye!")
            break  # This stops the loop
            
        # Get the solution from our function and print it
        result = get_solution(user_choice)
        print("\n-->", result)
        print("*" * 50)

# Run the program
if __name__ == "__main__":
    main()