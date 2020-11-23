# Libraries for this section 
import numpy as np
import pandas as pd
import altair as alt
alt.themes.enable('dark')

x = np.array([[1],
              [2],
              [3]])


y = np.array([[5],[2],[3]])


print('the shape of the vector is = ',x.shape) 

print(f'A 3-dimensional vector:\n{x}')


z = np.add(x,y);

print('\n z = x + y \n',z)


alpha = 5; 

omega = 5 * z

print("omega = 5 * z\n ",omega)

x, y = np.array([[-2],[2]]), np.array([[4],[-3]])

print("inner product refers to dot product and it is transpose and multiplication between 2 vectors \n",x.T @ y)



print("Euclidean Norm of a vector:",np.linalg.norm(x,2))


print("Manhattan Norm of a vector:",np.linalg.norm(x,1))



print("Max norm of a vector:",np.linalg.norm(x,np.inf))



print("We calculated the norms of this vector x = \n",x)
print("y = ",y)


distance = np.linalg.norm(x-y, 2)

print("L_2 distance reffers to x-y and euclidean norm =  ",distance)



x, y = np.array([[1], [2]]), np.array([[5], [7]])

# here we translate the cos(theta) definition
cos_theta = (x.T @ y) / (np.linalg.norm(x,2) * np.linalg.norm(y,2))
print("Cauchy–Schwarz inequality")
print(f'cos of the angle = {np.round(cos_theta, 3)}')

cos_inverse = np.arccos(cos_theta)
print(f'angle in radiants = {np.round(cos_inverse, 3)}')

degrees = cos_inverse * ((180)/np.pi)
print(f'angle in degrees = {np.round(degrees, 3)}')



cos_inverse = np.arccos(cos_theta)
print(f'angle in radiants = {np.round(cos_inverse, 3)}')



df = pd.DataFrame({"x1": [0, 2], "y1":[8, 3], "x2": [0.5, 2], "y2": [0, 3]})
equation1 = alt.Chart(df).mark_line().encode(x="x1", y="y1")
equation2 = alt.Chart(df).mark_line(color="red").encode(x="x2", y="y2")
equation1 + equation2



























