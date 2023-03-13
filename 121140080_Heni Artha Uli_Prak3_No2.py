class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")

    def tarik_tunai(self):
        jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if jumlah_tarik > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= jumlah_tarik
            print("Saldo berhasil ditarik!")

    def transfer(self):
        jumlah_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rek_tujuan = int(input("Masukkan no rekening tujuan: "))
        tujuan = None
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rek_tujuan:
                tujuan = pelanggan
                break
        if tujuan is None:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")
        else:
            if jumlah_transfer > self.__jumlah_saldo:
                print("Saldo tidak mencukupi untuk transfer!")
            else:
                self.__jumlah_saldo -= jumlah_transfer
                tujuan.__jumlah_saldo += jumlah_transfer
                print(f"Transfer Rp {jumlah_transfer} ke {tujuan._AkunBank__nama_pelanggan} sukses!")

Akun1 = AkunBank(1234, "Heni", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
nomor_input = int(input("Masukkan nomor input: "))
while nomor_input != 4:
    if nomor_input == 1:
        Akun1.lihat_saldo()
    elif nomor_input == 2:
        Akun1.tarik_tunai()
    elif nomor_input == 3:
        Akun1.transfer()
    else:
        print("Input tidak valid!")
    Akun1.lihat_menu()
    nomor_input = int(input("Masukkan nomor input: "))

print("Terima kasih")

