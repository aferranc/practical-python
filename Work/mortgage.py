# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 0
extra_payment_start_month = float(input("First month: "))
extra_payment_end_month = float(input("Last month: "))
extra_payment = float(input("Payment amount: "))


while principal > 0:
    month += 1
    payment = 2684.11
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment += extra_payment

    if principal < payment:
        total_paid = total_paid + principal
        principal = 0
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    
    print(f'{month:5d} ${round(total_paid, 2):0.2f} ${principal:0.2f}')

print(f"Total paid {round(total_paid, 2)} over {month} months")