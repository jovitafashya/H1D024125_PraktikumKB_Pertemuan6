# Import library
import numpy as np
import sys
import os

# Tambahkan path agar bisa import Backpropagation.py dari folder yang sama
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import Backpropagation as b

# Inisialisasi input dan target (bipolar)
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([[-1], [1], [1], [-1]])

# Pemanggilan model Backpropagation
model = b.Backpropagation(alpha=0.3, epoch=1000, target_error=0.001)
model.fit(X, t)
