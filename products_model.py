class Products:
    def __init__(self,title,price,quantity):
        self.title=title
        self.price=price
        self.quantity=quantity

    def info(self):
        return f"Mahsulotning nomi: {self.title}; Mahsulotning hozirgi narxi(1 kg uchun): {self.price} so'm; Mahsulotning hozirgi hajmi: {self.quantity} kg."

p1=Products("Olma",20000,100)
p2=Products("Nok",35000,100)
p3=Products("Banan",19000,100)
p4=Products("Limon",15000,100)
product_baza=[p1, p2, p3, p4]