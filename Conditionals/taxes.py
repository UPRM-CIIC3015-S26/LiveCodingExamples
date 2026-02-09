income = float(input("Please enter your annual income in 2022: "))
civil_status = input("Please enter your civil status (single or married): ")

if civil_status == "single":
    if income <= 11000:
        taxes = income * 0.10
    elif income <= 44725:
        taxes = 1100 + (income - 11000) * 0.12
    else:
        taxes = 5147 + (income - 44725) * 0.22
else:
    if income <= 22000:
        taxes = income * 0.10
    elif income <= 89450:
        taxes = 2200 + (income - 22000) * 0.12
    else:
        taxes = 10294 + (income - 89450) * 0.22

print( f"Your taxes amount to {taxes} dollars")