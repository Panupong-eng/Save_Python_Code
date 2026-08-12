start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
text = ""

print("Special numbers (divisible by 3 but not by 5):",end=" ")
for i in range(start, end + 1):
    if (i % 3 == 0) and (i % 5 != 0):
        if count == 0:
            text = text + str(i)
        else:
            text = text + ", " + str(i)
        count += 1

print(text)

if count > 0:
    print(f"Special numbers (divisible by 3 but not by 5): {text}")
    print(f"Count : {count}")
else:
    print("No special numbers found")