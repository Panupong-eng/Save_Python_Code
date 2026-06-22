#โปรแกรมตัดเกรด
#เพิ่มเติม
score = int(input("กรอกคะแนนของคุณ: "))
grade = None

if score >= 80 and score <= 100:#80-100
    grade="A"
elif score >= 70 and score <= 79:#70-79
    grade = "B"
elif score >=50 and score <= 69:#50-69
    grade ="F"
else:
    grade = "ได้เรียนบ้างไหม"

print("เกรดของคุณ =",grade)