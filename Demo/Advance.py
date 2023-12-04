import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]

# Misalnya interval ukuran per 10 sentimeter
interval_size = 10

# Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def group_into_intervals(data, interval_size):
    intervals = {}
    for height in data:
        key = (height // interval_size) * interval_size
        if key not in intervals:
            intervals[key] = 0
        intervals[key] += 1
    return intervals

# Menghitung frekuensi tinggi badan dalam interval
frekuensi_tinggi = group_into_intervals(tinggi_badan, interval_size)
print("Frekuensi Tinggi Badan dalam Interval:", frekuensi_tinggi)

# Visualisasi data dalam bentuk histogram dan kurva PDF
fig, ax1 = plt.subplots()

# Histogram
ax1.hist(tinggi_badan, bins=np.arange(min(tinggi_badan), max(tinggi_badan) + interval_size, interval_size), color='blue', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Tinggi Badan (cm)')
ax1.set_ylabel('Frekuensi', color='blue')
ax1.tick_params('y', colors='blue')

# Kurva PDF
ax2 = ax1.twinx()
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
ax2.plot(x, p, 'k', linewidth=2)
ax2.set_ylabel('PDF', color='black')
ax2.tick_params('y', colors='black')

plt.title('Histogram dan Kurva PDF Tinggi Badan')
plt.show()
