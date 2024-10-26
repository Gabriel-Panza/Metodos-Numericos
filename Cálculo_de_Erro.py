import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
    return x**2

def my_derivative(x):
    return 2*x

def ffd(func, x, h):
    return (func(x+h) - func(x))/h

def bfd(func, x, h):
    return (func(x) - func(x-h))/h

def cfd(func, x, h):
    return 0.5 * (func(x+h) - func(x-h))/h


x0 = 12.0
h = 1e-6
dx0 = ffd(my_func, x0, h)
my_type = np.float64

print("\n############################################### Derivada e Erro ###############################################\n")

print("Derivada Aproximada: ", dx0)
print("Derivada Exata", my_derivative(x0))

print("Erro exato total (Et): ", np.abs(my_derivative(x0) - dx0, dtype=my_type))
print("Erro exato relativo (Er): ", np.abs((my_derivative(x0) - dx0)/my_derivative(x0), dtype=my_type))

print("\n################################################ Vetor Base ####################################################\n")

h_vec = np.asarray([10**i for i in range(0,-10,-1)], dtype=my_type)

print(h_vec)

print("\n############################################ Derivada dos Vetores ###############################################\n")

dx0_vec_ffd = np.zeros(h_vec.shape[0], dtype=my_type)
dx0_vec_bfd = np.zeros(h_vec.shape[0], dtype=my_type)
dx0_vec_cfd = np.zeros(h_vec.shape[0], dtype=my_type)

for i in range(h_vec.shape[0]):
    dx0_vec_ffd[i] = ffd(my_func, x0, h_vec[i])
    dx0_vec_bfd[i] = bfd(my_func, x0, h_vec[i])
    dx0_vec_cfd[i] = cfd(my_func, x0, h_vec[i])
    
print("dx0 FFD: ", dx0_vec_ffd)
print("dx0 BFD: ", dx0_vec_bfd)
print("dx0 CFD: ", dx0_vec_cfd)

print("\n############################################## Erro dos Vetores ##################################################\n")
      
erro_ffd = np.zeros(h_vec.shape[0], dtype=my_type)
erro_bfd = np.zeros(h_vec.shape[0], dtype=my_type)
erro_cfd = np.zeros(h_vec.shape[0], dtype=my_type)

for i in range(h_vec.shape[0]-1):
    erro_ffd[i] = np.abs((dx0_vec_ffd[i+1] - dx0_vec_ffd[i]) / np.abs(my_derivative(x0)), dtype=my_type)
    erro_bfd[i] = np.abs((dx0_vec_bfd[i+1] - dx0_vec_bfd[i]) / np.abs(my_derivative(x0)), dtype=my_type)
    erro_cfd[i] = np.abs((dx0_vec_cfd[i+1] - dx0_vec_cfd[i]) / np.abs(my_derivative(x0)), dtype=my_type)

print("Erro FFD: ", erro_ffd)
print("Erro BFD: ", erro_bfd)
print("Erro CFD: ", erro_cfd)

print("\n##################################################### FIM #########################################################\n")

plt.loglog(h_vec, erro_ffd, color='blue', label='FFD')
plt.loglog(h_vec, erro_bfd, color='red', label='BFD')
plt.loglog(h_vec, erro_cfd, color='green', label='CFD')
plt.legend()
plt.show()