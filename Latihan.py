'''
#PERCOBAAN 1
import matplotlib.pyplot as plt

xpoints = [1, 8]
ypoints = [3, 10]

plt.plot(xpoints, ypoints)
plt.show()
'''
'''
#PERCOBAAN 2
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))
plt.plot(xpoints, ypoints, color='red', marker='o')
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Grafik Linier')
plt.show()
'''
'''
#PERCOBAAN 3
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 8])  # Garis ketiga

# Membuat plot untuk garis y1, y2, dan y3 dengan corak garis yang berbeda
plt.plot(y1, label='Garis 1', linestyle='-', color='blue')  # Garis solid biru
plt.plot(y2, label='Garis 2', linestyle='--', color='green')  # Garis putus-putus hijau
plt.plot(y3, label='Garis 3', linestyle=':', color='red')  # Garis titik-titik merah

# Menambahkan judul dan label sumbu
plt.title('Plot Tiga Garis')
plt.xlabel('Indeks Data')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()

plt.show()
'''

'''
#PERCOBAAN 4
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Menambahkan variasi warna dan ukuran marker
colors = ['red', 'green', 'blue', 'purple', 'orange']
sizes = [20, 50, 100, 150, 200]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, edgecolors='black', linewidth=1.5, label='Data Points')

# Menambahkan judul dan label sumbu
plt.title('Scatter Plot dengan Variasi')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan keterangan (legend)
plt.legend()

plt.show()
'''


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Menghasilkan sampel dari distribusi normal
sample = np.random.normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Data')  # Menambahkan histogram dari sampel data
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Normalized')

# Menghitung mean dan standard deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Membuat objek distribusi normal
dist = norm(sample_mean, sample_std)

# Membuat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]

# Menghitung probabilitas menggunakan metode pdf
probabilitas = [dist.pdf(value) for value in values]

# Menambahkan plot distribusi normal ke histogram
plt.plot(values, probabilitas, label='Distribusi Normal', color='red', linewidth=2)

# Menampilkan hasil
print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))
print("\nNilai Probabilitas:")
for value, prob in zip(values, probabilitas):
    print(f"Nilai: {value}, Probabilitas: {prob:.4f}")

# Menambahkan legenda
plt.legend()

plt.show()














