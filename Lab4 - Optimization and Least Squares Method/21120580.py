#21120580 - Trần Thị Kim Trinh
import numpy as np
import matplotlib.pyplot as plt
import math


##Câu 1
#Tạo ma trận A
print("- - - - - - - - - - Câu 1 - - - - - - - - - ")

A = np.array([[1,-2,1],[-2,1,-2], [1,-2,1]])
print('Ma trận A: \n', A)

evalue = np.round(np.linalg.eig(A)[0], 3) #tìm các giá trị riêng
print('Các giá trị riêng của A: \n', evalue)

result = np.all(evalue >= 0) or np.all(evalue <= 0) #xét ma trận xác định dương hay xác định âm
if result == False:
        print("=> Hàm số không lồi không lõm")

##Tìm điểm dừng f = 0 <=> 2Ax + B = 0 <=> 2A = -B
B = np.array([1,2,-1])

try:
    solution = np.linalg.solve(2 * A, -B)
    print(solution)
except np.linalg.LinAlgError: #nếu văng lỗi thì in ra thông báo không giải được
    print("=> Hệ phương trình không có nghiệm duy nhất và Hàm số không có điểm dừng")


###Câu 2
#Phương trình tuyến tính có dạng y = A + Bx, chi tiết quá trình lập ma trận A và B em có trình bày trong báo cáo
print("- - - - - - - - - - Câu 2 - - - - - - - - - ")
A = np.array([[1,0],[1,1],[1,2],[1,3],[1,4]])
B = np.array([10,8,7,5,2])

#Áp dụng bình phương tối thiểu để tìm A B
X = np.matmul(np.transpose(A), A)
Y = np.matmul(np.transpose(A),B)
solution = np.round(np.matmul(np.linalg.inv(X),Y),3)
print('Nghiệm bình phuong tối thiểu (A B) là: ', solution)
print('Công thức giảm lượng thuốc đối với bệnh nhân theo thời gian: ')
print(f'y = {solution[0]} + {solution[1]}x')

## Câu 3
print("- - - - - - - - - - Câu 3 - - - - - - - - - ")
#các điểm x y theo đề
x = np.array([-2, 0, 1, 2, 4])
y = np.array([-1, 1.5, 3.1, 6.3, 11.1])

matrix = np.zeros((5, 3))
matrix[:, 0] = 1
matrix[:,1] = x
matrix[:,2] = [math.log(XX*XX + 1) for XX in x ]
A = matrix
B = y
print("A: \n",A)
print("B: \n", B)
X = np.matmul(np.transpose(A), A)
Y = np.matmul(np.transpose(A),B)
solution = np.matmul(np.linalg.inv(X),Y)
print('Nghiệm bình phương tối thiểu là: ',solution)

#dự đoán khi x = 6.5 thì y = ?
print('dự đoán khi x = 6.5 thì y = ?')
ketquadudoan = solution[0] + solution[1] * 6.5 + solution[2]*(math.log(6.5*6.5 + 1))
print('Với x = 6.5 thì y = ', round(ketquadudoan,4))



# your set of points
ToaDox = np.array([-2, 0, 1, 2, 4])
ToaDoy = np.array([-1, 1.5, 3.1, 6.3, 11.1])

# plot the points
plt.scatter(ToaDox, ToaDoy, color = 'purple')

# plot the line
x = range(-3, 10)
a,b,c = solution
y = [solution[0] + solution[1] * i + solution[2]*(math.log(i*i + 1)) for i in x]
plt.plot(x, y)

# plot a short line segment with the desired color and linestyle
plt.plot([], [], color='blue', linestyle='-')

# add the legend for the points and the line segment
plt.legend(['các điểm dữ liệu gốc', 'Mô hình y = 1.14 + 1.81 * x + 0.92 * ln(x*x + 1)'])

# show the plot
plt.title('Mô hình giảm trọng lượng hợp chất theo thời gian tiếp xúc với không khí')
plt.xlabel('Thời gian (năm)')
plt.ylabel('Độ giảm trọng lượng (gam)')
plt.show()

#Không nên dùng các mô hình y = a + bx + clnx hay y = a + bx + c/x vì các mô hình này không xác định trên tòn tập số thực
#chi tiết trong báo cáo em có giải thích thêm ạ

