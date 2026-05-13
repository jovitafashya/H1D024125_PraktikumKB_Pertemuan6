# Praktikum 6 - Jaringan Syaraf Tiruan (JST)

Praktikum ini membahas implementasi Jaringan Syaraf Tiruan menggunakan Python. Ada dua algoritma yang diimplementasikan yaitu Perceptron untuk menyelesaikan masalah OR dan Backpropagation untuk menyelesaikan masalah XOR.

---

## File yang Ada di Repositori

- `Perceptron.py` — berisi kelas Perceptron
- `Perceptron_or.py` — program utama untuk menjalankan masalah OR
- `Backpropagation.py` — berisi kelas Backpropagation
- `Backpropagation_xor.py` — program utama untuk menjalankan masalah XOR

---

## Library yang Dibutuhkan

```bash
pip install numpy matplotlib
```

---

## Cara Menjalankan

Jalankan Perceptron dulu:
```bash
python Perceptron_or.py
```

Lalu jalankan Backpropagation:
```bash
python Backpropagation_xor.py
```

---

## Dataset

**Masalah OR (Perceptron)**

| X1 | X2 | Target |
|----|----|--------|
| 1  | 1  | 1      |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |

Parameter yang digunakan: learning rate = 0.1, epoch = 10, bobot awal = 0

**Masalah XOR (Backpropagation)**

| X1 | X2 | Target |
|----|----|--------|
| 1  | 1  | -1     |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |

Parameter yang digunakan: learning rate = 0.3, epoch = 1000, target error = 0.001

---

## Hasil

Perceptron berhasil konvergen di epoch ke-3 dengan bobot akhir [0.2, 0.2] dan bias 0.2. Sedangkan Backpropagation berhasil mencapai target error di bawah 0.001.

Setiap kali program dijalankan akan menghasilkan file teks berisi log perhitungan dan grafik visualisasi.
