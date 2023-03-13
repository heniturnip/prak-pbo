class Baju:
    def __init__(self, merk, jenis, harga):
        self.__merk = merk     # atribut private
        self._jenis = jenis    # atribut protected
        self.harga = harga     # atribut public
        self.__diskon = 0.3    # atribut private
    
    def info(self):
        print(f"Baju {self.__merk}, jenis {self._jenis}, harga awal {self.harga}")

    def harga_diskon(self):
        harga_diskon = 0
        harga_diskon = self.harga - (self.harga * self.__diskon)
        print(f"Harga setelah diskon: {harga_diskon}")

baju = Baju("H&M", "Dress", 450000)
baju.info() # Baju H&M, jenis Dress, harga 450000
print(baju._jenis)
print(baju.harga)
baju.harga_diskon()
print(baju.__diskon)
#print(baju.__merk)  # AttributeError: 'Baju' object has no attribute '__merk'

