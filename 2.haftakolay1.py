array = (1,2,3,4,5)
secim = input("For veya While döngüsü seçiniz:")
if secim =="for":
    print("For loop çıktısı:")
    print("\n")
    for sayilar in array:
        print(sayilar)
elif secim =="while":
    print("While loop çıktısı:")
    print("\n")
    limit = len(array)
    i=0
    while (i<limit):
        print(array[i])
        i += 1
        print("\n")
else:
        print("Geçersiz döngü seçildi, lütfen for veya while seçiniz.")