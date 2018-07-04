# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt 
import xlrd
import math
import csv

file_path = r'F:\LCC上下楼梯数据\LCC上下楼梯数据\BHV全局.xlsx'
#读取的文件路径

data = xlrd.open_workbook(file_path)
#获取数据
table = data.sheet_by_name('Scene_12BVH全局_Char00')
#获取sheet
R1_hip = np.zeros((3,3))
R2_hip = np.zeros((3,3))
R12_hip = np.zeros((3,3))

R1_knee = np.zeros((3,3))
R2_knee = np.zeros((3,3))
R12_knee = np.zeros((3,3))

R1_ankle = np.zeros((3,3))
R2_ankle = np.zeros((3,3))
R12_ankle = np.zeros((3,3))



def caculateR(R,w,x,y,z):
	R[0,0] = 1 - 2 * y[i]**2 - 2 * z[i]**2
	R[0,1] = 2 * (x[i] * y[i] - z[i] * w[i])
	R[0,2] = 2 * (x[i] * z[i] + y[i] * w[i])
	R[1,0] = 2 * (x[i] * y[i] + z[i] * w[i])
	R[1,1] = 1 - 2 * x[i]**2 - 2 * z[i]**2
	R[1,2] = 2 * (y[i] * z[i] - x[i] * w[i])
	R[2,0] = 2 * (x[i] * z[i] - y[i] * w[i])
	R[2,1] = 2 * (y[i] * z[i] + x[i] * w[i])
	R[2,2] = 1 - 2 * x[i]**2 - 2 * y[i]**2
	return R
	

def caculateR12(R1,R2):
	R12 = np.matmul(R1,np.linalg.inv(R2))
	return R12
	

def caculateTheta(R12,theta):
	w = math.sqrt(1 + R12[0,0] + R12[1,1] + R12[2,2]) / 2

	the = math.acos(w) * 2 * 180 / math.pi
	# the = math.acos(w) * 2
	theta.append(the)
	return theta


nrows = table.nrows
#获取总行数
print (nrows)
ncols = table.ncols
print (ncols)
#获取总列数


theta_hip = []
theta_knee = []
theta_ankle = []

v_hip = []
v_knee = []
v_ankle = []

a_hip = []
a_knee = []
a_ankle = []

for nr in range(0,nrows):
	table.row_values(nr)
#获取一行的数值
for nc in range(0,ncols):
	table.col_values(nc)
#获取一列的数值
col2 = table.col_values(22)
col3 = table.col_values(38)
col4 = table.col_values(54)
col1 = table.col_values(6)

w_1 = col1
x_1 = table.col_values(7)
y_1 = table.col_values(8)
z_1 = table.col_values(9)

w_2 = col2
x_2 = table.col_values(23)
y_2 = table.col_values(24)
z_2 = table.col_values(25)

w_3 = col3
x_3 = table.col_values(39)
y_3 = table.col_values(40)
z_3 = table.col_values(41)

w_4 = col4
x_4 = table.col_values(55)
y_4 = table.col_values(56)
z_4 = table.col_values(57)


for i in range(7,nrows):
	R1_hip = caculateR(R1_hip,w_1,x_1,y_1,z_1)
	R2_hip = caculateR(R2_hip,w_2,x_2,y_2,z_2)
	R12_hip = caculateR12(R1_hip,R2_hip)
	caculateTheta(R12_hip,theta_hip)

for i in range(7,nrows):
	R1_knee = caculateR(R1_knee,w_2,x_2,y_2,z_2)
	R2_knee = caculateR(R2_knee,w_3,x_3,y_3,z_3)
	R12_knee = caculateR12(R1_knee,R2_knee)
	caculateTheta(R12_knee,theta_knee)

for i in range(7,nrows):
	R1_ankle = caculateR(R1_ankle,w_3,x_3,y_3,z_3)
	R2_ankle = caculateR(R2_ankle,w_4,x_4,y_4,z_4)
	R12_ankle = caculateR12(R1_ankle,R2_ankle)
	caculateTheta(R12_ankle,theta_ankle)


for i in range(0,nrows-7):
	if i <= nrows - 9:
		v = (theta_hip[i+1] - theta_hip[i]) * 120
		v_hip.append(v)
	else:
		break

for i in range(0,nrows-7):
	if i <= nrows - 10:
		a = v_hip[i+1] - v_hip[i] * 120
		a_hip.append(a)
	else:
		break
	



x = []

for i in range(0,nrows-7):
	x.append(i) 



# with open("csvfile.csv","w",newline = '') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(["theta_hip","theta_knee","theta_ankle"])
# 	n = nrows - 7
# 	for i in range(n):
# 		writer.writerow(theta_hip[i])
# 		writer.writerow(theta_knee[i])
# 		writer.writerow(theta_ankle[i])
# 	csvfile.close()


plt.xlabel("fps") 
plt.ylabel("angle")
plt.plot(x,theta_knee,label = "knee angle",color = 'r')
plt.plot(x,theta_hip,label = "hip angle",color = 'g')
plt.plot(x,theta_ankle,label = "ankle angle",color = 'b')
# plt.plot(x[0:nrows-8],v_hip,label = "hip_v",color = 'y')
# plt.plot(x[0:nrows-9],a_hip,label = "hip_a",color = 'darkgrey')
plt.legend()
plt.show()
