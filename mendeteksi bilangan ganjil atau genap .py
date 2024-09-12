def cek_genap_atau_ganjil(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Contoh penggunaan
bilangan = int(input("Masukkan sebuah bilangan: "))
hasil = cek_genap_atau_ganjil(bilangan)
print(f"Bilangan {bilangan} adalah {hasil}.")
