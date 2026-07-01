class Product:
    def __init__(self,name,brand,mfg,expiry,quantity,price):
        self.name=name
        self.brand=brand
        self.mfg=mfg
        self.expiry=expiry
        self.quantity=quantity
        self.price=price
Brand1=Product("Shampoo","Dove","01/01/2024","01/01/2025",10,100)
Brand2=Product("Soap","No.1","10/05/2026","07/08/2026",10,200)
Brand3=Product("Facewash","Darma","20/01/2026","10/09/2026",10,4000)
Brand4=Product("FaceCream","Ponds","01/01/2024","05/07/2025",20,1000)
Brand5=Product("Conditioner","Dove","01/02/2023","01/01/2025",5,500)
Brand6=Product("Shampoo","Sunsilk","05/05/2024","01/01/2027",10,100)
all_products=[Brand1,Brand2,Brand3,Brand4,Brand5,Brand6]
# Display all products
print("------------ PRODUCT LIST ------------")
for i in all_products:
    print(i.name,i.brand,i.price,"Stock:",i.quantity)
bill=[]
grand_total=0
while True:
    search=input("\nEnter Product Name or Brand (or type Exit):")
    if search.lower()=="exit":
        break
    found = False
    for i in all_products:
        if search.lower() == i.name.lower() or search.lower() == i.brand.lower():
            found = True
            print("\nProduct Found")
            print("Name :", i.name)
            print("Brand :", i.brand)
            print("Price :", i.price)
            print("Available Stock :", i.quantity)
            qty = int(input("Enter Quantity : "))
            if qty <= i.quantity:
                total = qty * i.price
                i.quantity -= qty
                bill.append([i.name, qty, total])
                grand_total += total
                print("Added to Bill Successfully")
            else:
                print("Insufficient Stock")
            break
    if found == False:
        print("Product Not Found")
print("\n************ BILL ************")
for item in bill:
    print(item[0], " Qty:", item[1], " Amount:", item[2])
print("-----------------------------")
print("Grand Total :", grand_total)

