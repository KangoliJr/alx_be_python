#user entering their details
monthly_income_str = input("Enter your monthly income:")
monthly_income = float(monthly_income_str)

#total expenditure
monthly_expenses_str = input("Enter your total monthly expenses:")
monthly_expenses = float(monthly_expenses_str)

#calculating the savings
monthly_savings = monthly_income - monthly_expenses

#annual savings
#having an interest of 5%
annual_interest_rate = 0.05

#Now calculating the savings for one year without interest
savings_before_interest = monthly_savings * 12

#calculating the interest
interest_earned = savings_before_interest * annual_interest_rate

#calculating the projected savings
projected_savings = savings_before_interest + interest_earned

print(f"Your monthly savings are ${monthly_savings:.0f}.")

print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
