#Group Profit Calc
#By Indict5
#Version: 1.0

# Take input for total_pay and fuel_req
total_pay = float(input("Enter the total pay: "))
fuel_req = float(input("Enter the fuel requirement (Gals): "))
fuel_price = float(input("Enter the fuel cost per gallon: "))
print("===================================")
# Calculate group_fees, pilot_pay, and ground_fees
group_fees = total_pay * 0.31
pilot_pay = total_pay * 0.69
ground_fees = total_pay * -0.10

# Calculate fuel_cost
fuel_cost = fuel_req * -fuel_price

# Calculate group_pay
group_pay = group_fees + ground_fees + fuel_cost

# Print the calculated values
print("Pilot Pay  :v$", round(pilot_pay, 2))
print(" ")
print("Group Fees :v$", round(group_fees, 2))
print(" ")
print("Trip Fuel Cost :v$", round(fuel_cost, 2))
print(" ")
print("Ground Fees:v$", round(ground_fees, 2))
print(" ")
print("Group Pay  :v$", round(group_pay, 2))
