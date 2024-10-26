import numpy as np
import matplotlib.pyplot as plt

def bissecao(f,xl,xu,resid_max):
    a=f(xl)
    b=f(xu)
    if ((a<0 and b>0) or (a>0 and b<0)):
        xp = (xl+xu) * 0.5
        resid_atual = abs(f(xp))
        qntd_interacoes = 0
        while resid_atual > resid_max:
            qntd_interacoes += 1
            if ((b<0 and resid_atual>0) or (b>0 and resid_atual<0)):
                xl = xp
                if (xu == 0):
                    return xu
            else:
                xu = xp
                if (xl == 0):
                    return xl
            xp = (xl+xu) * 0.5
            if (xp == 0): 
                return xp
            resid_atual = abs(f(xp))
            print("Interacao ", qntd_interacoes, ": Residuo Atual = ", resid_atual, "\n")
        return xp
    return None
def func(x):
    return ((x**3) + 2)

xl = -2.0
xu = 1.0
bissecao(func,xl,xu,0.2)