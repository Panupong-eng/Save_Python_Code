#mapping pattern
customers = [
    {"name":"สมชาย", "email":"somchai@example.com", "type":"member"},
    {"name":"สมหญิง", "email":"somjing@example.com", "type":"general"},
    {"name":"สมศักดิ์", "email":"somSakd@example.com", "type":"general"}
]

id = int(input("Enter customer ID : "))
# print(customers[id]["name"]," ", customers[id]["email"], " ", customers[id]["type"])
print(f"Customer {id} : {customers[id]["name"]}")

match customers[id]:
    case {"type":"member"}:
        print("เป็นสมาชิก ได้รับส่วนลด 10%")
    case {"type":"general"}:
        print("เป็นลูกค้าทั่วไป ไม่ได้รับส่วนลด")
    case _: #ไม่เข้ากรณีใดๆ
        print("ไม่พบข้อมูลลูกค้า")