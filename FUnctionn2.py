# #แบบลำดับ *ชื่อ
# def one(*args):
#     print("Hello,", args[0])
#     print("Age:", args[1])
#     print("Location:", args[2])
    
# one("สมชาย",25, "กรุงเทพฯ")


# #แบบกำหนดชื่อ **ชื่อ
def two(**kwargs):
    print("Hello,", kwargs["name"])
    print("Age:", kwargs["age"] , "ปี")
    print("Location:", kwargs["location"])
    
two(name="สมพร", age=52, location="นครปฐม")