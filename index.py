import pandas as pd

# 1. Ganti 'file_anda.xlsx' dengan nama file Excel Anda
# 2. Ganti 'Sheet1' dengan nama sheet spesifik yang ingin Anda ambil
df = pd.read_excel('../../../MASTER.xlsx', sheet_name='Material_Stock_Report')

# Konversi dan simpan ke file data.json
df.to_json('data.json', orient='records', indent=4)

print("Selesai! File 'data.json' berhasil dibuat.")