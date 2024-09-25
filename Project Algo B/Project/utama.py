from welcome import welcome_page
from Project.BMI import bmi
def main_menu():
    while True:
        welcome_page("\nMenu Utama")
        print("1. Hitung BMI")
        print("2. Keluar")
        
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == '1':
            bmi()
        elif pilihan == '2':
            print("Terima kasih! Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")