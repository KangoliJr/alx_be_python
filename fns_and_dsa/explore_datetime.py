from datetime import datetime, date, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return
    current_date_obj = date.today()
    future_date = current_date_obj + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-m-%d")
    print(f"Future date: {formatted_future_date}")
    
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()