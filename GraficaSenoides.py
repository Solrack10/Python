import numpy as np
from matplotlib import pyplot as plt 
x=np.arange(0,np.pi*2,0.01)
y=np.cos(x)
x1=np.arange(0,np.pi*2,0.01)
y1=np.sin(x)
plt.title("Funciones Senoidales en el Dominio del Tiempo")
plt.plot(x,y,'x-', label='Coseno')
plt.plot(x1,y1,'o-', label='Seno')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()
