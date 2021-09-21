class VolumeBalok :
    Panjang =  None
    Lebar = None
    Tinggi = None

VB = VolumeBalok()
VolumeBalok.Panjang = 8
VolumeBalok.Lebar = 10
VolumeBalok.Tinggi = 12

Hasil = VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi

print("Panjang Balok :", VolumeBalok.Panjang)
print("Lebar Balok :", VolumeBalok.Lebar)
print("Tinggi Balok :", VolumeBalok.Tinggi)
print("Hasil Volume Balok:", Hasil)