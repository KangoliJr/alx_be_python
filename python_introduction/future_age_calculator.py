current_age_str = input("How old are you?")
current_age = int(current_age_str)
target_year = 2050
assumed_current_year = 2023
years_to_add = target_year - assumed_current_year

future_age = current_age + years_to_add
print(f"in {target_year}, you will be {future_age} years old")