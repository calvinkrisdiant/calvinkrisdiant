import matplotlib.pyplot as plt
import numpy as np

# Data transaksi
data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [t[1] for t in data_transaksi]
jumlah_terjual = [t[2] for t in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.scatter(harga_produk, jumlah_terjual, color='blue', label='Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Scatter Plot Hubungan Harga dan Jumlah Produk Terjual')
plt.legend()
plt.show()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
produk_labels = [t[0] for t in data_transaksi]
plt.bar(produk_labels, pendapatan_produk, color='green', label='Pendapatan')
plt.xlabel('Produk')
plt.ylabel('Pendapatan')
plt.title('Bar Chart Pendapatan Produk')
plt.legend()
plt.show()
