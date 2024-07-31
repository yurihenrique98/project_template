def menu():
    print("""Please enter the letter which corresponds with your desired menu choice:\n
    [A] View Data
    [B] Visualise Data
    [C] Export Data   
    [X] Exit
     """)
    selection = input("Enter your choice:\n")
    return selection.upper()


def submenu_a():
    print(""""Please enter one of the following options:\n
    [A] View Reviews by Park
    [B] Number of Reviews by Park and Reviewer Location
    [C] Average Score per year by Park
    [D] Average Score per Park by Reviewer Location
   """)
    choice = input("Enter your choice:\n")
    return choice.upper()


def submenu_b():
    print(""""Please enter one of the following options:\n
    [A] Most Reviewed Parks
    [B] Average Scores
    [C] Park Ranking by Nationality
    [D] Most Popular Month by Park
     """)
    choice = input("Enter your choice:\n")
    return choice.upper()

def export_menu():
    print("Export Menu")
    print("A. Export to TXT")
    print("B. Export to CSV")
    print("C. Export to JSON")
    print("D. Return to main menu")
    choice = input("Enter your choice:\n ")
    return choice.upper()
