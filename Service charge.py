bill = float(input("Enter bill amount: "))
print(f"Bill: {bill:.2f} บาท")

if bill >= 1000:
    service_charge = bill * 0.10
    print(f"Service charge (10%): {service_charge:.2f} บาท")
elif bill >= 500:
    service_charge = bill * 0.07
    print(f"Service charge (7%): {service_charge:.2f} บาท")
else:
    service_charge = bill * 0.05
    print(f"Service charge (5%): {service_charge:.2f} บาท")

print(f"Total: {bill + service_charge:.2f} บาท")