#USE THE PYTHON^ !
red , blue , green , yan , normal = "\033[31m","\033[34m" , "\033[32m" , "\033[6m" , "\033[0m"
kupon = input("Denenecek Kupon : ")
from selenium import webdriver as wb
import os
from time import sleep
os.system("clear")
konum=os.getcwd()+"/chromedriver"
print(green+"Şimdi şöyle işliyor:\n"+normal+"Dosya konumunda 'linkler.txt' adlı bir dosya var .\nBu dosyanın içine denetlenecek linkleri örnekteki gibi atın . Sonunda / olmasına çok dikkat edin.\nArdından webdriver kullanrak udemy açılacak\nRobot doğrulaması verebilir , eğer verirse el ile geçin\nArdından oturum açmanız gerekli . Oturum açtıktan sonra [enter] layarak devam edelim\nTerminalde kodun çalıştığı linkler gelicektir . Iyi dersler .. \n\nHerlink 5 saniye ara ile kontrol edilecektir (udemy yönlendirmesi)\n")
input(green+"[ENTER]"+normal)
try:
    ekran = wb.Chrome(konum)
except:
    print("chromedriver da sorun var gibi gözüküyor !")
    exit()
ekran.get("https://udemy.com/")
if ekran.title == 'Access to this page has been denied.':
    print("Görünüşe göre doğrulamaya takıldık .")

print("\nLütfen giriş yapın \n")
input(green+"[OTURUM AÇILDIYSA [ENTER] ]"+normal)
with open("linkler.txt","r") as file:
    file = file.readlines()
for i in file:
    i = i + "?couponCode=" +kupon
    ekran.get(i)
    sleep(7)
    uzunluk=len(kupon)
    uzunluk_link = len("?couponCode=")+uzunluk
    print("\nDeneniyor --> "+i[28:-uzunluk_link])
    if ekran.current_url[-uzunluk:] == kupon:
        print(green+"\nbulundu !: "+normal+ekran.current_url+normal+"\n")
    else:
        print("Bulunamadı --> "+i[28:-uzunluk_link]+"\n")
        print("\n\033[31m-------------\033[0m\n")
ekran.close()
print("\nUmarım yararlı olmuştur\n")
exit()
