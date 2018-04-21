# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt 
import xlrd
import math

file_path = r'C:\Users\zyj\Desktop\BHV全局.xlsx'
#读取的文件路径

data = xlrd.open_workbook(file_path)
#获取数据
table = data.sheet_by_name('Scene_12BVH全局_Char00')
#获取sheet
nrows = table.nrows
#获取总行数
print (nrows)
ncols = table.ncols
print (ncols)
#获取总列数
col1 = []
col2 = []
col3 = []
col4 = []
for nr in range(0,nrows):
	table.row_values(nr)
#获取一行的数值
for nc in range(0,ncols):
	table.col_values(nc)
#获取一列的数值
col1 = table.col_values(22)
col2 = table.col_values(38)
col3 = table.col_values(54)
col4 = table.col_values(6)
#获取一个单元格的数值



x = []
y1 = []
y2 = []
y3 = []
for i in range(0,nrows-7):
	x.append(i) 
print (x)
for j in range(7,nrows):
	j = (math.acos(col1[j]) + math.acos(col2[j]))* 2 * 180 / math.pi - 180
	y1.append(j)
for k in range(7,nrows):
	k = (math.acos(col3[k]) - math.acos(col2[k]))* 2 * 180 / math.pi 
	y2.append(k)
for g in range(7,nrows):
	g = (math.acos(col1[g]) + math.acos(col4[g]))* 2 * 180 / math.pi - 180
	y3.append(g)
print (y1)
plt.xlabel("fps") 
plt.ylabel("angle")
plt.plot(x,y1,label = "knee angle",color = 'r')
plt.plot(x,y2,label = "ankle angle",color = 'b')
plt.plot(x,y3,label = "hip angle",color = 'g')
plt.legend()
plt.show()