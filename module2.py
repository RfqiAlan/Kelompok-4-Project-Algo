def hitung_kalori():
    """
    MET adalah rasio laju energi yang dikeluarkan selama aktivitas dengan laju energi yang 
    dikeluarkan saat istirahat. Misalnya, 1 MET adalah laju pengeluaran energi saat istirahat.
    Aktivitas 4 MET mengeluarkan 4 kali energi yang digunakan oleh tubuh saat istirahat.  
    """
    while True:
        try:
            berat_badan = int(input("Masukkan berat badan (kg): "))
            if berat_badan <= 0:
                print("Berat badan harus lebih dari 0.")
                continue
            
            durasi = int(input("Masukkan durasi aktivitas (menit): "))
            if durasi <= 0:
                print("Durasi aktivitas harus lebih dari 0.")
                continue
            
            MET = float(input("Berikut informasi nilai MET yang harus dimasukkan berdasarkan aktivitas yang dilakukan\n"
                              "duduk di meja: 1 MET\n"
                              "berjalan santai: 2 - 3 MET \n"
                              "bersepeda ringan: 3.5 - 5.5 MET \n"
                              "jogging: 7 - 8 MET \n"
                              "berenang: 6 - 9 MET \n"
                              "lari cepat: 10 - 12 MET \n"
                              "Masukkan nilai MET aktivitas: "))
            if MET <= 0 or MET > 12:
                print("Mohon perhatikan, nilai MET yang dimasukkan harus antara 1 hingga 12.")
                continue
            
            kalori_terbakar = MET * berat_badan * (durasi / 60)
            return f"Kalori terbakar: {kalori_terbakar:.1f} kalori"
        
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")
        except NameError:
            print("Peringatan: Anda memasukkan variabel yang belum didefinisikan.")

print(hitung_kalori())
