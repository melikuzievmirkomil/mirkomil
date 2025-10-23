from user_model import User, user_baza
from products_model import Products, product_baza

class Shop:
    def __init__(self,title):
        self.title=title
        self.baza=[]
        self.users=[]
        self.balance=0

    def add_products(self):
        title=input("Mahsulotning nomi: ")
        price=int(input("Mahsulotning narxi: "))
        quantity=int(input("Mahsulotning hajmi: "))
        p=Products(title, price, quantity)
        self.baza.append(p)

    def view_products(self):
        if not self.baza:
            print("Mahsulotlar mavjud emas!")
            return
        count=0
        for item in self.baza:
            count+=1
            print(f"{count}.",item.info())

    def delete_products(self):
        self.view_products()
        index=int(input("O'chiriladigan mahsulot raqamini kiriting: "))
        if 0<index<=len(self.baza):
            ind=self.baza.pop(index-1)
            print(f"{ind.title}  o'chirildi!")
        else:
            print("Noto'g'ri raqam kiritdingiz!")

    def edit_products(self):
        self.view_products()
        index=int(input("Tahrirlanadigan mahsulot raqamini kiriting: "))
        if 0<index<=len(self.baza):
            ind=self.baza[index-1]
            yangi_nomi=input("Mahsulotning yangi nomini kiriting: ")
            yangi_narxi=input("Mahsulotning yangi narxini kiriting: ")
            yangi_vazni=input("Mahsulotning yangi vaznini kiriting: ")
            if yangi_nomi:
                ind.title=yangi_nomi
            if yangi_narxi:
                ind.price=int(yangi_narxi)
            if yangi_vazni:
                ind.quantity=int(yangi_vazni)
            print("Mahsulot yangilandi!")
            print(ind.info())
        else:
            print("Noto'g'ri raqam kiritdingiz!")

    def login_users(self):
        username=input("Loginni kiriting: ")
        password=input("Parolni kiriting: ")
        user=User(username,None,None,False, password)
        for item in self.users:
            if item.name==username and item.password==password:
                return item
        return user

shop=Shop("Shop")
shop.users=user_baza
shop.baza=product_baza

def admin_manager(u: User, s: Shop):
    while True:
        kod=input("1.Mahsulotlarni ko'rish \n2.Mahsulotni qo'shish \n3.Mahsulotni o'chirish \n4.Mahsulotni tahrirlash \n5.Balansni ko'rish \n6.Chiqish \n<<<<>>>>: ")
        if kod=="1":
            s.view_products()
        elif kod=="2":
            s.add_products()
        elif kod=="3":
            s.delete_products()
        elif kod=="4":
            s.edit_products()
        elif kod=="5":
            print(f"Supermarket balansida: {s.balance} so'm mavjud")
        else:
            break

def user_manager(u: User, s: Shop):
    while True:
        kod=input("1.Mahsulotlarni ko'rish \n2.Savatni ko'rish \n3.Balans ustida amallar bajarish "
            "\n4.Xaridni yakunlash \n5.Savatni tahrirlash\n6.Chiqish<<<<>>>>: ")
        if kod=="1":
            s.view_products()
            index=input("Mahsulot raqamini tanlang: ")
            if index.isdigit() and 0 < int(index) <= len(s.baza):
                quantity=int(input("Mahsulot miqdorini yozing: "))
                p1=s.baza[int(index) - 1]
                if quantity > p1.quantity:
                    print("Kechirasiz, bu mahsulotdan yetarli miqdorda mavjud emas!")
                else:
                    jami_summa = p1.price * quantity
                    p2 = Products(p1.title, jami_summa, quantity)
                    u.basket.append(p2)
                    print(f"{p1.title} savatga qo‘shildi! {quantity} dona")
            else:
                print("Noto‘g‘ri raqam!")
        elif kod=="2":
            if u.basket:
                for idx, item in enumerate(u.basket, 1):
                    print(f"{idx}. {item.info()}")
                print(f"Jami summa: {sum(item.price for item in u.basket)} so‘m")
            else:
                print("Savat bo‘sh!")
        elif kod == "3":
            while True:
                kod1 = input("1.Balansni tekshirish \n2.Balansga pul qo'shish \n3.Chiqish \n<<<<>>>>: ")
                if kod1 == "1":
                    print(f"Sizning balansingizda: {u.balance} so'm mavjud")
                elif kod1 == "2":
                    pul = int(input("Qo'shiladigan pul miqdori(so'mda): "))
                    if pul > 0:
                        u.balance += pul
                        print(f"{pul} so'm pul balansga qo'shildi!")
                        print(f"Yangi balansingiz: {u.balance} so'm")
                    else:
                        print("Noto'g'ri pul miqdori kiritildi!")
                else:
                    break
        elif kod == "4":
            # ✅ Xarid yakunlanayotganda balans va mahsulot ombori tekshiriladi
            jami_summa = sum(item.price for item in u.basket)
            if u.balance >= jami_summa:
                # ✅ Ombordagi mahsulotlarni kamaytirish
                for basket_item in u.basket:
                    for shop_item in s.baza:
                        if basket_item.title == shop_item.title:
                            if shop_item.quantity >= basket_item.quantity:
                                shop_item.quantity -= basket_item.quantity
                            else:
                                print(f"{shop_item.title} mahsulotidan omborda yetarli emas!")
                                break
                u.balance-=jami_summa   # foydalanuvchi balansi kamayadi
                s.balance+=jami_summa   # do‘kon balansi ko‘payadi
                print(f"Xarid yakunlandi! Jami {jami_summa} so‘m sarflandi.")
                print(f"Sizning yangi balansingiz: {u.balance} so'm")
                u.basket.clear()
            else:
                print("Balansingizda yetarli mablag‘ mavjud emas!")
        elif kod=="5":
            if not u.basket:
                print("Savat bo‘sh! Tahrirlash mumkin emas.")
            else:
                for idx, item in enumerate(u.basket, 1):
                    print(f"{idx}. {item.info()}")
                index = int(input("Qaysi mahsulotni tahrirlaysiz (raqamni kiriting): "))
                if 0<index<=len(u.basket):
                    ind=u.basket[index-1]
                    yangi_nomi=input("Yangi nom (bo‘sh qoldirsangiz o‘zgarmaydi): ")
                    yangi_narxi=input("Yangi narx (bo‘sh qoldirsangiz o‘zgarmaydi): ")
                    yangi_miqdori=input("Yangi miqdor (bo‘sh qoldirsangiz o‘zgarmaydi): ")
                    if yangi_nomi:
                        ind.title=yangi_nomi
                    if yangi_narxi:
                        ind.price=int(yangi_narxi)
                    if yangi_miqdori:
                        ind.quantity=int(yangi_miqdori)
                    print("Mahsulot yangilandi!")
                    print(ind.info())
                else:
                    print("Noto‘g‘ri raqam!")
        else:
            break

def shop_manager(s:Shop):
    while True:
        kod=input("1.Kirish \n2.Chiqish \n<<<<<>>>>>: ")
        if kod=="1":
            user=s.login_users()
            if user.types=="admin":
                admin_manager(user, s)
            elif user.types=="user":
                user_manager(user, s)
            else:
                print("Login yoki parol xato!")
        else:
            break
