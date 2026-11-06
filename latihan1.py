a = int(input("masukkan angka pertama:"))
b = int(input("masukkan angka kedua:"))

if a>b:
    print("angka maksimal adalah:",a)
else:
    if b>a:
        print("angka maksimal adalah:",b)
    else:
        print("kedua angka sama")