  
 # Feedback Management System

feedback = {}

def submit_feedback():

    sid = input("Enter Student ID: ")

    if sid in feedback:
        print("Feedback already submitted!")
        return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    message = input("Enter Feedback: ")

    confirm = input("Confirm Feedback Submission? (yes/no): ")

    if confirm.lower() == "yes":

        feedback[sid] = {
            "name": name,
            "department": department,
            "feedback": message
        }

        print("Feedback Submitted Successfully!")

    else:
        print("Submission Cancelled.")


def view_feedback():

    print("\n----- ALL FEEDBACK -----")

    if len(feedback) == 0:
        print("No Feedback Available")
        return

    for sid, details in feedback.items():

        print("\nStudent ID :", sid)
        print("Student Name :", details["name"])
        print("Department :", details["department"])
        print("Feedback :", details["feedback"])


def search_feedback():

    keyword = input("Enter Student ID or Department: ").lower()

    found = False

    for sid, details in feedback.items():

        if (keyword in sid.lower()
                or keyword in details["department"].lower()):

          
          print("\nSearch Result:")
            print("Student ID :", sid)
            print("Student Name :", details["name"])
            print("Department :", details["department"])
            print("Feedback :", details["feedback"])

            found = True

    if not found:
        print("No Feedback Found.")
def sentiment_analysis():

    sid = input("Enter Student ID: ")

    if sid not in feedback:
        print("Student not found!")
        return

    message = feedback[sid]["feedback"].lower()

    positive_words = [
        "good", "great", "excellent",
        "helpful", "nice", "best"
    ]

    negative_words = [
        "bad", "poor", "worst",
        "problem", "issue", "slow"
    ]


  
  positive = 0
    negative = 0
    for word in positive_words:

        if word in message:
            positive += 1

    for word in negative_words:

        if word in message:
            negative += 1

    if positive > negative:
        result = "Positive"

    elif negative > positive:
        result = "Negative"

    else:
        result = "Neutral"

    print("\n----- SENTIMENT ANALYSIS -----")
    print("Student ID :", sid)
    print("Feedback :", feedback[sid]["feedback"])
    print("Sentiment :", result)

    if result == "Negative":
        print("Warning! Negative Feedback Found.")

def feedback_category():

  
  sid = input("Enter Student ID: ")

    if sid not in feedback:
        print("Student not found!")
        return

    message = feedback[sid]["feedback"].lower()

    if "teacher" in message or "teaching" in message:
        category = "Teaching"

    elif "lab" in message or "classroom" in message:
        category = "Infrastructure"

    elif "placement" in message or "job" in message:
        category = "Placement"

    elif "canteen" in message or "food" in message:
        category = "Canteen"

    else:
        category = "Other"

    print("\n----- FEEDBACK CATEGORY -----")
    print("Student ID :", sid)
    print("Feedback Category :", category)
def feedback_analytics():

    positive = 0
    
negative = 0

    neutral = 0

    for sid, details in feedback.items():

        message = details["feedback"].lower()

        positive_words = [
            "good", "great", "excellent",
            "helpful", "nice", "best"
        ]

        negative_words = [
            "bad", "poor", "worst",
            "problem", "issue", "slow"
        ]

        p = 0
        n = 0

        for word in positive_words:

            if word in message:
                p += 1

        for word in negative_words:

            if word in message:
                n += 1

        if p > n:
           

 positive += 1
        elif n > p:
            negative += 1

        else:
            neutral += 1

    print("\n----- FEEDBACK ANALYTICS -----")

    print("Total Feedback :", len(feedback))
    print("Positive Feedback :", positive)
    print("Negative Feedback :", negative)
    print("Neutral Feedback :", neutral)


def feedback_report():

    print("\n----- FEEDBACK REPORT -----")

    if len(feedback) == 0:
        print("No Feedback Available")
        return

    for sid, details in feedback.items():

        print("\nStudent ID :", sid)
        print("Student Name :", details["name"])
        print("Department :", details["department"])
        print("Feedback :", details["feedback"])


 
   print("\nTotal Feedback :", len(feedback))
while True:

    print("\n===================================")
    print("     FEEDBACK MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Submit Feedback")
    print("2. View Feedback")
    print("3. Search Feedback")
    print("4. Sentiment Analysis")
    print("5. Feedback Category")
    print("6. Feedback Analytics")
    print("7. Feedback Report")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        submit_feedback()

    elif choice == "2":
        view_feedback()

    elif choice == "3":
        search_feedback()

    elif choice == "4":
        sentiment_analysis()

  

  elif choice == "5":
        feedback_category()
    elif choice == "6":
        feedback_analytics()

    elif choice == "7":
        feedback_report()

    elif choice == "8":
        print("Thank You For Using Feedback Management System")
        break

    else:
        print("Invalid Choice!")
