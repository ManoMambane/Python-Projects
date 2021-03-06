import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'mo-', label='students')
plt.plot(x1, y2, 'go-', label='teachers')

plt.subplots_adjust(left=0.3, bottom=0.3)
plt.legend(loc='upper left')

plt.title('Your title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()
