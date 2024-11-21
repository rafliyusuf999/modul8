def rekursif(jumlah_angka, total=0): 
    if jumlah_angka > 0: 
        angka = float(input(f"masukkan angka ke {jumlah_angka} "))
        total += angka
        return rekursif(jumlah_angka - 1, total) 
    else:
        return total

masukan = int(input("Jumlah angka: "))
if masukan > 0:
    hasil = rekursif(masukan)
    print(f"hasil: {hasil}")
else:
    print("hasil: 0")