from utama import main_menu
def bmi ():
    def hitung_bmi(tinggi_badan, berat_badan):
        bmi = berat_badan / tinggi_badan**2
        return bmi

    def kategori_bmi(jenis_kelamin, bmi):
        if jenis_kelamin == "1":
            if bmi < 18:
                return "Underweight (Laki-laki)"
            elif 18 <= bmi <= 23.9:
                return "Normal (Laki-laki)"
            elif 24 <= bmi <= 26.9:
                return "Overweight (Laki-laki)"
            else:
                return "Obesitas (Laki-laki)"
        elif jenis_kelamin == "2":
            if bmi < 19:
                return "Underweight (Perempuan)"
            elif 19 <= bmi <= 24.9:
                return "Normal (Perempuan)"
            elif 25 <= bmi <= 27.9:
                return "Overweight (Perempuan)"
            else:
                return "Obesitas (Perempuan)"
        else:
            return "Jenis kelamin tidak valid"

    
    while True :
        tinggi = float(input("Masukkan tinggi badan anda (dalam meter): "))
        berat = float(input("Masukkan berat badan anda (dalam kg): "))
        jenis_kelamin = input("Masukkan jenis kelamin anda (1 untuk laki-laki, 2 untuk perempuan): ")
        bmi_result = hitung_bmi(tinggi, berat)

        
        kategori = kategori_bmi(jenis_kelamin, bmi_result)

       
        print(f"Nilai BMI Anda adalah: {bmi_result:.2f}")
        print(f"Kategori BMI Anda adalah: {kategori}")
        kembali = input("Apakah mau kembali ke menu utama ya/tidak? :")
        if kembali != "ya":
            print("Terima kasih! Sampai jumpa!")


if __name__ == "__main__":
    main_menu()
