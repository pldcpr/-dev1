giriş="""
(1) Bakiye Sorgulama
(2) Para Yatırma
(3) Para Çekme
"""
print(giriş)

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break
    elif soru=="1":
        print("Mevcut Bakiyeniz 53 TL'dir.")
    elif soru=="2":
        sayi1=int(input("Lütfen yatırmak istediğiniz tutarı girin: "))
        print("Yeni bakiyeniz: ", 53+sayi1)
    elif soru=="3":
        sayi2=int(input("Lütfen çekmek istediğiniz tutarı girin: "))
        print("Yeni bakiyeniz: ", 53-sayi2)
    else:
        print("Geçersiz işlem")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)