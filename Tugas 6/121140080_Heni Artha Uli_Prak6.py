from abc import ABC, abstractmethod
import datetime

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
    
    def lihatsaldo(self):
        print(f"Saldo {self.nama}: Rp {self.saldo:,}")
        
    @abstractmethod
    def transfer(self, jumlah):
        pass
    
    @abstractmethod
    def lihatbunga(self):
        pass

class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 0
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihatsaldo()
            
    def lihatbunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if self.saldo >= 1000000000:
            if usia_akun >= 3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
        print(f"Suku bunga: {bunga*100:.2f}% per bulan")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 5000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihatsaldo()
    
    def lihatbunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if self.saldo >= 10000000:
            if usia_akun >=3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
        print(f"suku bunga: {bunga*100:.2f}%per bulan")
                
class AkunReguler(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 5000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihatsaldo()

    def lihatbunga(self):
        print("Akun regular tidak mendapatkan suku bunga.")

akun_regular = AkunReguler("Heni", 2020, 13500000)
akun_regular.lihatsaldo() 
akun_regular.transfer(80000)
akun_regular.lihatsaldo() 
akun_regular.lihatbunga() 
akun_silver = AkunSilver("Steven", 2019, 70000000)
akun_silver.lihatsaldo() 
akun_silver.lihatbunga() 
akun_silver.transfer(150000) 
akun_silver.lihatsaldo() 
akun_gold = AkunGold("Heaven", 2018, 1700000000)
akun_gold.lihatsaldo()
akun_gold.lihatbunga()
akun_gold.transfer(35000000) 
akun_gold.lihatsaldo()   
