import numpy as np
import random
 

def printM(A):
    rows = len(A)
    for i in range(0,rows):
        print(A[i])

def readFile():
    with open('INPUT.txt') as f:
        data = []
        row,col = list(map(int, f.readline().split()))
        for i in range(0,row):
            data.append(list(map(int,f.readline().split()[:col])))
    return data

def Gauss_elimination(A):
    rows = len(A)
    col = len(A[0])
    chuan = 0;
    row = 0
    while (row < rows) : #xét tưng dòng trong ma trận A
        if (chuan >= col):
            break
        if (A[row][chuan] == 0):
            rowA = row+1;
            for rowA in range(row+1,rows):
                if (A[rowA][chuan] != 0):
                    tmp = np.zeros((col))
                    for i in range(0,col):
                        tmp[i] = A[row][i]
                    for i in range(0,col):
                        A[row][i] = A[rowA][i]
                    for i in range(0,col):
                        A[rowA][i] = tmp[i]


        if (A[row][chuan] == 0):
            chuan = chuan + 1
            continue

        for rowA in range(row+1,rows): #xét theo cột dọc xuống
            if (A[rowA][chuan] != 0):
                    heso1 = A[rowA][chuan] #hệ số tại vị trí hiện tại
                    heso2 = -A[row][chuan] #hệ số tại vị trí của chuan
                    for i in range(0,col):
                        A[rowA][i] =  A[rowA][i] * heso2  + A[row][i] * heso1;

        chuan = chuan+1
        row += 1

    return A
def rank(A):
    Gauss_elimination(A)
    rows = len(A)
    rank = rows

    col = len(A[0])
    for i in range(0,rows):
        count = 0;
        for j in range(0,col):
            if (A[i][j] == 0):
                count +=1
        if count == col:
            rank = rank - 1
    return rank;

def back_substitution(A):
    Gauss_elimination(A)
    rows = len(A)
    col = len(A[0])

    temp = np.zeros((rows,col-1)) #ma trận hệ số
    for i in range(0,rows): #có được bằng cách chép lại toàn bộ ma trận A, nhưng bỏ cột cuối cùng
        for j in range(0,col-1):
            temp[i][j] = A[i][j]

    rankA = rank(A) #hạng của ma trận mở rộng
    rankTemp = rank(temp) #hạng của ma trận hệ số

    nghiem = np.zeros(col-1) #mảng để lưu nghiệm

    if rankA == rankTemp and rankA == col-1: #Nếu 2 hạng tính được ở trên bằng nhau và bằng số ẩn
        #pt có nghiệm duy nhất
        for i in range(rankA-1, -1,-1):
            nghiem[i] = A[i][col-1]
            for j in range(0,col-1):
                if i != j:
                    nghiem[i] -= A[i][j] * nghiem[j]
            nghiem[i] = nghiem[i] / A[i][i]

        return nghiem
    
    if rankA == rankTemp and rankA != col-1:
    #vô số nghiệm
        nghiemtudo = col- 1 - rankA # số ẩn tự do = số ẩn - hạng
        coso = np.zeros((nghiemtudo,col-1)) #1 cơ sở của tập vô nghiệm
        #dòng > cột 

        #dòng < cột => thêm dòng trống để dòng = cột
        temp = np.zeros((rows+nghiemtudo,col)) 
        for i in range(0,rows):
            for j in range(0,col):
                temp[i][j] = A[i][j]
        for i in range(rows,rows+nghiemtudo):
            for j in range(0,col):
                    temp[i][j] = 0
        dong_trong = rows
        rows = rows+nghiemtudo

        LaNghiem = np.zeros((col-1))
        for i in range(0,rows):
            for j in range(0,col-1):
                if temp[i][j] != 0 and LaNghiem[j] == 0:
                    LaNghiem[j] = 1
                    break

        for ii in range(0,nghiemtudo):
            for i in range(0,col-1):
                if LaNghiem[i] == 0:
                    temp[dong_trong][i] = 1
                    temp[dong_trong][col - 1] = random.randint(0,5)
                    dong_trong += 1
        
            # sở dĩ phải tạo thêm temp1 là vì nếu dùng trực tiếp trên temp,
            # sau ki giải xong 1 lần hệ phương trình sẽ bị biến thành dạng rút gọn, khó khăn cho các lần giải sau
            temp1 = np.zeros((len(temp),col)) 
            for i in range(0,rows):
                for j in range(0,col):
                    temp1[i][j] = temp[i][j]
            coso[ii] = back_substitution(temp1)
            dong_trong = rows-nghiemtudo 

        print("\nPhuong trinh co vo so nghien, co 1 co so la:") 
        return coso
    if rankA != rankTemp:
        return ("He pt tren vo nghiem! \n")

A = []
A = readFile()
print("Ma tran A: ")
printM(A)
print("Gauss_elimination(A): ")
printM(Gauss_elimination(A));     
print("Giai he pt tren, ta duoc: ")
print(back_substitution(A))


