J =int(input("Masukan bulan (1-12):"))
if J == 1 or J == 3 or J== 5 or J == 7 or J == 8 or J == 10 or J == 12 :
    print("Jumlah Hari: 31")
elif J == 4 or J == 6 or J == 9 or  J == 11 :
    print("Jumlah Hari: 30")
else:
    print("Jumlah Hari: 28")
    
