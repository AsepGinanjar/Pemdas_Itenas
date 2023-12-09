import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for index, row in df.iterrows():
    df.at[index, 'Gaji_plus_5%'] = row['Gaji'] * 1.05
# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

print("\nRingkasan Perubahan:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

for index, row in df.iterrows():
    df.at[index, 'Gaji_plus_2%'] = (lambda x: x * 1.02 if row['Usia'] > 30 else x)(row['Gaji_plus_5%'])
# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df)

print("\nRingkasan Hasil:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")
print("Karyawan di atas 30 tahun mendapatkan peningkatan tambahan sebesar 2%.")

# # ---------------------------- #
# # Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# # https://gitlab.com/itenas/tugas_pemdas.git
# # ---------------------------- #

# # Catatan:

# # Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# # Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# # Tampilkan hasil dan ringkasan dengan jelas.
# # Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.