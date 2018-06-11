import numpy as np  # for matrix calculation
import matplotlib.pyplot as plt 

# load the CSV file as a numpy matrix
data_file = open(r'C:\Users\zyj\Desktop\机器学习作业\WaterMelon_3.0a.csv')
dataset = np.loadtxt(data_file)

# separate the data from the target attributes
X = dataset[:,1:3]
y = dataset[:,3]

# draw scatter diagram to show the raw data
f1 = plt.figure(1)       
plt.title('watermelon_3a')  
plt.xlabel('density')  
plt.ylabel('ratio_sugar')  
plt.scatter(X[y == 0,0], X[y == 0,1], marker = 'o', color = 'k', s=100, label = 'bad')
plt.scatter(X[y == 1,0], X[y == 1,1], marker = 'o', color = 'g', s=100, label = 'good')
plt.legend(loc = 'upper right')  
plt.show()