baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz    : "))

toplam = 0



for i in range(baslangic, bitis,2):
    print(i)
    toplam = toplam + i

print("Toplam: ", toplam)