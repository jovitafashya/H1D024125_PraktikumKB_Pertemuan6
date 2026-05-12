# Import library
import numpy as np
import sys
import os

# Tambahkan path agar bisa import Perceptron.py dari folder yang sama
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import Perceptron as p

# Inisialisasi input dan target (bipolar)
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([[1], [1], [1], [-1]])

# Pemanggilan model Perceptron
model = p.Perceptron(alpha=0.1, epoch=10)
model.fit(X, t)
