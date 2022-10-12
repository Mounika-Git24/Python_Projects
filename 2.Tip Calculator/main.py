print("Welcome to the tip calculator!")

# total bill amount
bill = float(input("What was the total bill? ₹"))

# tip percentage 10% or 12% or 15%
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# number of persons to split the bill
people = int(input("How many people to split the bill? "))

# if the bill was ₹3500, split between 4 people, with 10% tip.
# final amount per person = ((3500 * 10 / 100) + 3500) / 4

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Rounded the result to 2 decimal places
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ₹{final_amount}")
