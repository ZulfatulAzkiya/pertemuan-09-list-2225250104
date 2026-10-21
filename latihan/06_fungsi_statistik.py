
# Fungsi Statistik Sederhana

def hitung_statistik(data):
    if len(data) == 0:
        print("Data masih kosong.")
        return

    print("Jumlah data:", len(data))
    print("Total nilai:", sum(data))
    print("Rata-rata:", sum(data) / len(data))
    print("Nilai tertinggi:", max(data))
    print("Nilai terendah:", min(data))


nilai = [80, 75, 90, 85, 70]

hitung_statistik(nilai)