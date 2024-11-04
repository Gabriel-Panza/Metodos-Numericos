import numpy as np

mat = [[3,-0.1,-0.2,7.85],[0.1,7,-0.3,-19.3],[0.3,-0.2,10,71.4]]
print(mat)

N = len(mat)

for k in range(N):
    for i in range(k+1,N):
        f = mat[i][k]/mat[k][k]
        for j in range(k+1,N+1):
            mat[i][j]=mat[i][j]-f*mat[k][j]
        mat[i][k] = 0
print(np.array(mat))

x = [0,0,0]
for k in range(N-1,-1,-1):
    print(".k="+str(k))
    for j in range(k+1,N):
        print(" j="+str(j))
        x[k] -= mat[k][j]*x[j]
    x[k] += mat[k][N]
    x[k] /= mat[k][k]
print(np.array(x))