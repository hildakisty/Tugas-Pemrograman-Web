#kelas luas segitiga
class LuasSegitiga:
    Alas = None
    Tinggi = None

#membangun intance/variable sebagai "objek nyata"
LS = LuasSegitiga()
LuasSegitiga.Alas=10
LuasSegitiga.Tinggi=8

hasil=0.5*LuasSegitiga.Alas*LuasSegitiga.Tinggi

#Output yang ditampilkan
print("Alas Segitiga : ", LuasSegitiga.Alas)
print("Tinggi Segitiga : ", LuasSegitiga.Tinggi)
print("Hasil Segitiga : ",hasil)