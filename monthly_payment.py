#KODSNUTT ATT BÖRJA MED
import os

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    periods = years * 12
    
    if monthly_rate == 0:
        return principal / periods
    
    numerator = principal * monthly_rate
    denominator = 1 - (1 + monthly_rate) ** (-periods)
    monthly_payment = numerator / denominator
    return monthly_payment


principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")