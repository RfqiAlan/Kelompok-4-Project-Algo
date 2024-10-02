#Function 1 : Body Mass Index (BMI)
def hitung_bmi(tinggi_badan, berat_badan):
    bmi = berat_badan / tinggi_badan**2
    return bmi

def kategori_bmi(jenis_kelamin, bmi):
    if jenis_kelamin.lower() == "1":
        if bmi < 18:
            return "Underweight (Laki-laki)"
        elif 18 <= bmi <= 23.9:
            return "Normal (Laki-laki)"
        elif 24 <= bmi <= 26.9:
            return "Overweight (Laki-laki)"
        else:
            return "Obese (Laki-laki)"
    elif jenis_kelamin.lower() == "2":
        if bmi < 19:
            return "Underweight (Perempuan)"
        elif 19 <= bmi <= 24.9:
            return "Normal (Perempuan)"
        elif 25 <= bmi <= 27.9:
            return "Overweight (Perempuan)"
        else:
            return "Obese (Perempuan)"
    else:
        return "Jenis kelamin tidak valid"

# Memasukkan input dari pengguna
tinggi = float(input("Masukkan tinggi badan anda (dalam meter): "))
berat = float(input("Masukkan berat badan anda (dalam kg): "))
jenis_kelamin = input("Masukkan jenis kelamin anda (1 untuk laki-laki, 2 untuk perempuan): ")

# Menghitung BMI
bmi_result = hitung_bmi(tinggi, berat)

# Menentukan kategori berdasarkan jenis kelamin dan BMI
kategori = kategori_bmi(jenis_kelamin, bmi_result)

# Output hasil BMI dan kategori
print(f"Nilai BMI Anda adalah: {bmi_result:.2f}")
print(f"Kategori BMI Anda adalah: {kategori}")
    #          l       p
#150 - 159	60 - 65	57 - 62
#160 - 169	65 - 70	62 - 67
#170 - 179	70 - 75	67 - 72
#180 - 189	75 - 80	72 - 77
#190 - 199	80 - 85	77 - 82