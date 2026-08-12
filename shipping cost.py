package = float(input("Enter package weight (kg): "))
distance = float(input("Enter distance (km): "))
if package <= 1:
    shipping_cost = 50
elif package <= 5:
    shipping_cost = 80
else:
    shipping_cost = 120
    
if distance <= 10:
    distance_cost = 0
elif distance <= 50:
    distance_cost = 20
else:
    distance_cost = 50

print(f"Base shipping cost: {shipping_cost} บาท")
print(f"Distance surcharge: {distance_cost} บาท")
print(f"Total shipping cost: {shipping_cost + distance_cost} บาท")