class User:
    def __init__(self, name, phone, balance, types, password):
        self.name=name
        self.phone=phone
        self.balance=balance
        self.types=types
        self.password=password
        self.basket=[]

    def info(self):
        return f"Ismi: {self.name}; Telefon raqami: {self.phone}; Balans miqdori: {self.balance}."

    def view_products(self):
        for item in self.basket:
            print(item.info())

admin=User("Admin",9927794,0,"admin", "1111")
user1=User("User1",9927795,2000000,"user", "2222")
user2=User("User2",9927796,1000000,"user", "3333")
user_baza=[admin, user1, user2]