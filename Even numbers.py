start = int(input("Enter start: "))
end = int(input("Enter end: "))

total_sum = 0
text = ""
count = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        if count == 0:
            text = text + str(i)
        else:
            text = text + " " + str(i)
        total_sum += i
        count += 1

print(f"Even numbers from {start} to {end}: {text}")
print(f"Sum of even numbers: {total_sum}")