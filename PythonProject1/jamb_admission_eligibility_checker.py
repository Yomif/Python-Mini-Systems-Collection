# ==========================================
#     JAMB ADMISSION ELIGIBILITY CHECKER
# ==========================================

print("=========================================")
print("     WELCOME TO JAMB SCREENING PORTAL")
print("=========================================")

# Collect student information
student_name = input("Enter your full name: ")
school_name = input("Enter your school name: ")

print("\nEnter your JAMB subject scores below.")

# Error handling for score input
try:
    jamb_math = int(input("Mathematics Score : "))
    jamb_english = int(input("English Score     : "))
    jamb_biology = int(input("Biology Score     : "))

    # Validate scores
    if (
        jamb_math < 0 or jamb_math > 100 or
        jamb_english < 0 or jamb_english > 100 or
        jamb_biology < 0 or jamb_biology > 100
    ):
        print("\nInvalid score entered.")
        print("Scores must be between 0 and 100.")

    else:
        # Calculate total score
        total_score = jamb_math + jamb_english + jamb_biology

        # Calculate average score
        average_score = total_score / 3

        # Display student result
        print("\n=========================================")
        print("          JAMB SCREENING RESULT")
        print("=========================================")

        print(f"Student Name   : {student_name}")
        print(f"School Name    : {school_name}")
        print(f"Mathematics    : {jamb_math}")
        print(f"English        : {jamb_english}")
        print(f"Biology        : {jamb_biology}")
        print(f"Total Score    : {total_score}")
        print(f"Average Score  : {average_score:.2f}")

        # Eligibility check
        if total_score >= 200:
            print("\nSTATUS: ELIGIBLE FOR POST UTME")
            print(f"Congratulations {student_name}!")

        else:
            print("\nSTATUS: NOT ELIGIBLE FOR POST UTME")
            print(f"Sorry {student_name}, you did not meet")
            print("the required cutoff mark.")

# Handle invalid input
except ValueError:
    print("\nInvalid input detected.")
    print("Please enter numbers only for scores.")

print("=========================================")
print("        SCREENING PROCESS ENDED")
print("=========================================")