while True:
    try:
        berat_badan = int(input("Masukkan berat badan: "))
        if berat_badan <= 0:
            print("berat badan harus lebih dari 0")
            continue
        def rekomendasi_asupan_air(berat_badan):
             return berat_badan * 35 / 1000
        asupan = rekomendasi_asupan_air(berat_badan)
        print(f"Asupan air yang direkomendasikan adalah {asupan} liter." )
        break
    except ValueError:
        print("input tidak valid! harap masukkan angka.")
