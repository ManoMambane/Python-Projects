import matplotlib.pyplot as plt

values = [16,18,4,8]
pielabels = ['Python', 'JS', 'Java', 'React']
piecolors = ['green','blue','black','maroon']
pieexplode = [0,0.1,0,0]

plt.pie(values, labels=pielabels,explode=pieexplode,colors=piecolors,startangle=0,shadow=True)
plt.title('Pie Chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='best')
plt.show()