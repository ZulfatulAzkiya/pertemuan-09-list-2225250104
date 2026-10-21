
# Memfilter Nilai Kelulusan

nilai_mahasiswa = [80, 55, 75, 60, 90, 45, 85]

nilai_lulus = []

for nilai in nilai_mahasiswa:
    if nilai >= 60:
        nilai_lulus.append(nilai)

print("Semua nilai:", nilai_mahasiswa)
print("Nilai yang lulus:", nilai_lulus)
print("Jumlah mahasiswa lulus:", len(nilai_lulus))