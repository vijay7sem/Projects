class item:
    def __init__(self,id,itemName,price):
        self.id=id
        self.itemName=itemName
        self.price=price
        
#Create Bill Display Function

def display(l , cName , cAddress):
    Total=0
    print("\n\n\n")
    print("\t\t VIJAY SWEETS")
    print("\t\t --------------")
    print(f"Name:{cName} \t Address:{cAddress}")
    for obj in l:
        print(f"Id:{obj.id} \t Item Name: {obj.itemName} \t price:{obj.price}")
        print("-------------------------------------------------")
        Total+=obj.price
        print(f"\t \t Total:{Total}")
        print("\n")


    
#Store Object Array
List = []

print("\n\n")
print("Hello Sir/Mam")
cName=input("Enter your Name: ")
cAddress=input("Enter your Address: ")
TotalItems=int(input("Enter total items: "))
print("\n")

#Take input item Details.
for i in range(0,TotalItems):
    id=i+1
    name=input("Enter item name: ")
    price=int(input("Enter price: "))
    List.append(item(id,name,price))
    
#Call Display Function.

display(List,cName,cAddress)
print("         Thank You! visit Again    ")
print("\n\n")
    


    
        