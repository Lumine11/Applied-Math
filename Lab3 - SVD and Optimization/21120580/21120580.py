#21120580 - Trần Thị Kim Trinh

import numpy as np
import math

def printM(A):
    rows = len(A)
    for i in range(0,rows):
        for j in range(0, len(A[0])):
            print( (round(A[i][j],3)) , end = ', ')
        print()
    print("- - - - -")

def sigmaPlus(A):
    A = np.transpose(A)
    for i in range(0,len(A)):
        if (A[i][i] != 0):
            A[i][i] = 1 / A[i][i];
    return A

def SingularValueToSigma(A, D):
    shape = A.shape
    m=shape[0] #Cho biet so dong cua A
    n=shape[1] #Cho biet so cot cua A
    result = np.zeros((m,n))
    i = len(D)
    for j in range(0,i):
        result[j][j] = D[j]
    return result

#khởi tạo ma trận M N để tìm nghiệm bình phương tối tiểu
M = np.array([[1971, 1], [1972, 1], [1974, 1], [1978, 1], [1982, 1], [1985, 1], [1989, 1], [1993, 1], [1997, 1], [1999, 1], [2000, 1], [2002, 1], [2003, 1]])
for i in range(len(M)):
    M[i][0] -= 1970

N = np.array([2250, 2500, 5000, 29000, 120000, 275000, 1180000, 3100000, 7500000, 24000000, 42000000, 220000000, 410000000])
N = [math.log10(xx) for xx in N]

#Phân tích kì dị ma trận M 
U, D, VT = np.linalg.svd(M) 
print("U:")
printM(U)
print("Σ:")
printM(SingularValueToSigma(M,D))
print("VT:")
printM(VT)

#tìm ma trận giả nghịch đảo (M+)
MPlus = np.transpose(VT) @ sigmaPlus(SingularValueToSigma(M,D)) @ np.transpose(U)
print("MPlus:")
printM(MPlus)

#tìm nghiệm bình phương tối tiểu
print("least square solution: ")
solution =MPlus@N
print(solution)
print("Phuong trinh hoi quy: ")
print("log10N = ", round(solution[0],4),"* (x-1970) + ", round(solution[1],4))

print("--- Du doan so bong ban dan trong bo vi xu ly duoc gioi thieu vao nam 2015 la: ")
log10y = solution[0]*(2015-1970) + solution[1]
print("log10N = ", log10y)
result = 10**log10y
print("So bong ban dan la: ",format(result, '.5f'))
chenhlech = result - 4000000000
print("Chenh lech giua tinh toan va thuc te la: ", chenhlech)
