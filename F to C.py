f = float(input("Enter temperature in Fahrenheit: "))
c = float((f-32)*(5/9))
print(f"{f:.1f}°F = {c:.1f}°C")
if (c <= 0):
    print("State: น้ำแข็ง")
elif (c >= 100):
    print("State: น้ำเดือด")
else:
    print("State: อุณหภูมิห้อง")