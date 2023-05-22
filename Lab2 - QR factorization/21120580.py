import numpy as np
import math

def printM(A):
    rows = len(A)
    for i in range(0,rows):
        for j in range(0, len(A[0])):
            print( (round(A[i][j],3)) , end = ', ')
        print()
    print("- - - - -")

def readFile():
    with open('INPUT.txt') as f:
        data = []
        row,col = list(map(int, f.readline().split()))
        for i in range(0,row):
            data.append(list(map(int,f.readline().split()[:col])))
    return data


def innerproduct(v1, v2):
    if len(v1) != len (v2):
        return "Loi kich thuoc! ";
    s = 0
    for i in range(0,len(v1)):
        s += v1[i] * v2[i];
    return s

def transpose(A):
    #Khoi tao ma tran ket qua
    AT = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    m=len(A)#Cho biet so dong cua A
    n=len(A[0])#Cho biet so cot cua A
    for i in range(m):
        for j in range(n):
            AT[j][i]=A[i][j]
    return AT

def abs2(A):
    sum = 0
    for i in range(0,len(A)):
        sum += A[i]*A[i]
    return sum

def NhanMaTran(A, B):
    #Khoi tao ma tran ket qua
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    #Nhan hai ma tran
    m=len(A)#Cho biet so dong cua A
    n=len(B[0])#Cho biet so cot cua A

    cotB = []
    cotB = transpose(B) # do khi nhân lấy dòng i ma trận a nhân cột j, nên em dùng ma trận chuyển vị để thành dòng i x dòng j => dùng lại hàm nhân 2 vector

    for i in range(0,m):
        for j in range(0,n):
            C[i][j] = innerproduct(A[i], cotB[j])
    return C


def VectorbyNumber(a, V): #hàm nhân vector với một số
    temp = np.ones((len(V)))
    for i in range(0,len(V)):
        temp[i] = V[i] * a
    return temp

def QR_factorization(A):
    Q = transpose(A) #u
    temp = transpose(A) #v

    for k in range(0,len(temp)): #trực giao hóa
        sum = np.zeros((len(temp[0])))
        for i in range(0,k):
            sum = sum + VectorbyNumber(innerproduct(temp[k],Q[i]) / abs2(Q[i]), Q[i])
        Q[k] = temp[k] - sum

    for k in range(0,len(temp)): #trực chuẩn
        Q[k] = VectorbyNumber(1/math.sqrt(abs2(Q[k])), Q[k])

    
    print("Ma tran Q: ")
    Q = transpose(Q)
    printM(Q)
    print("Ma tran R: ")
    R = NhanMaTran(transpose(Q),A)
    printM(R)


A = []

A = readFile()
print("Ma tran A: ")
printM(A)
QR_factorization(A)