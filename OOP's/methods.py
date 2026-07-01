# # class demo:
# #     @classmethod
# #     def greet(cls):
# #         return "hi"
# #     print(demo.greet())
# #     print(demo.ins)


# class demo:
#     #clas var
#     ins="hello"
#     @classmethod
#     def greet(cls):
#         return"hi"
#     @classmethod
#     def modify(cls,new_value):
#         cls.ins=new_value
#     print(demo.greet())
#     print(demo.ins)
#     demo.modify("linkcode")

# class demo1:
#     def  __init(self,name,age,id,marks):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.marks=marks

#     def welcome(self):
#         return "hello student"
#     def modify(self):
#         newvalue=input("enter the new name:")
#         ex_name=self.name
#         self.name=newvalue
#         print(f"existing name {ex_name}updated name{self.name}")
# s1=demo1("ram",21,101,90)
# print(s1.name,s1.age,s1.id,s1.marks)
# print(s1.welcome())
# s1.modify()


class bank:
    bankname="SBI"
    ifsc="SBIN0000123"

#instance variable

    def __init__(self,name,bal,mail):
        self.name=name
        self.bal=bal
        self.mail=mail
#method ins
    def show_details(self):
        print("Bank Name:",bank.bankname)
        print("IFSC Code:",bank.ifsc)
        print("Account Name:",self.name)
        print("Account balance:",self.bal)
        print("Account mail:",self.mail)
    def check_bal(self):
        print("available  blance is:",self.bal)
    user1=bank("ram",10000,"ram@example.com")
    user1.show_details()
    user1.check_bal()


