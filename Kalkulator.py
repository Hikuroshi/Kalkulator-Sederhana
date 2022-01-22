#fungsi penjumlahan
def tambah(x, y):
    return x + y

#fungsi pengurangan
def kurang(x, y):
    return x - y

#fungsi perkalian
def kali(x, y):
    return x * y

#fungsi pembagian
def bagi(x, y):
    return x / y

def sisabagi(x, y):
    return x % y

def pangkat(x, y):
    return x ** y

#menu operasi
print("Pilih Operasi: ")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
print("5.Sisa Bagi")
print("6.Pemangkatan")

#meminta output dari pengguna
pilih = input ("Masukan pilihan operasi (1/2/3/4/5/6):")

num1 = int(input("Masukan bilangan pertama:"))
num2 = int(input("Masukan bilangan kedua:"))

if pilih == '1':
    print(num1,"+",num2,"=", tambah(num1,num2))

elif pilih == '2':
    print(num1,"-",num2,"=", kurang(num1, num2))

elif pilih == '3':
    print(num1,"*",num2,"=", kali(num1, num2))

elif pilih == '4':
    print(num1,"/",num2,"=", bagi(num1, num2))

elif pilih == '5':
    print(num1,"%",num2,"=", sisabagi(num1, num2))
    
elif pilih == '6':
    print(num1,"**",num2,"=", pangkat(num1, num2))

else:
    print("Input Salah")