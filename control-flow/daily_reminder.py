
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
if Time_Bound == "yes":
 match Priority:
    case "high":
     print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
    case "medium":
     print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
    case "low":
     print(f"Reminder: {Task} is a {Priority} priority task that requires attention today!")
if Time_Bound == "no":
 match Priority:
    case "low":
     print (f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.") 