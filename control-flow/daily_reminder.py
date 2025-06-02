task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

# initialize reminder message
reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
    case 'low':
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' is a task of unknown priority"

# time-bound
if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"
elif time_bound == 'no' and priority == 'low':
    reminder_message += ". Consider completing it when you have free time."
elif time_bound == 'no':
    reminder_message += "."
    
print(f"Reminder: {reminder_message}")