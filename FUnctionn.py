#สร้างFunction

#ส่วนหัว  ชื่อฟังก์ชัน
def nameFunction():
    print("Hello World")
    #ส่วนเนื้อหาการทำงานของฟังก์ชัน
    
def helloname(name,age):
    print("Hello World",name, "Age:", age)

def dokjun():
    for i in range(50): 
        print("*", end="")



#--------------เรียกใช้งานฟังก์ชัน--------------
#          argument ส่งไปที่ parameter name
helloname("สมชาย",25) #ส่งชื่อขึ้นไปที่ตัวแปร name ของฟังก์ชัน helloname
helloname("สมหญิง",20)
dokjun()