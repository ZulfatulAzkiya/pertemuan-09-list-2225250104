
# Praktik Analisis Nilai Mahasiswa

nama_mahasiswa = ["Andi", "Budi", "Citra", "Dina", "Eka"]
nilai_mahasiswa = [80, 55, 90, 65, 45]

print("=== ANALISIS NILAI MAHASISWA ===")

for i in range(len(nama_mahasiswa)):
    nama = nama_mahasiswa[i]
    nilai = nilai_mahasiswa[i]

    if nilai >= 60:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print(f"{nama}: {nilai} - {status}")

print("\nJumlah mahasiswa:", len(nilai_mahasiswa))
print("Rata-rata nilai:", sum(nilai_mahasiswa) / len(nilai_mahasiswa))
print("Nilai tertinggi:", max(nilai_mahasiswa))
print("Nilai terendah:", min(nilai_mahasiswa))