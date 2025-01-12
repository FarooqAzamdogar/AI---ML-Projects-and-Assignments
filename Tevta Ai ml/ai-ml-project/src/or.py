#Implement OR using single perceptron

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0,0],[0,1],[1,0],[1,1]]) #Inputs features
y = np.array([0,1,1,1]) #Actual ouptut

# Initialize weights and bias
theta = np.random.randn(2)
bias = np.random.randn(1)
alpha = 0.01
iterations = 1000
m,col = X.shape
#Activation function
def step_function(x):
    return np.where(x >= 0,1,0)

#Training a perceptron
for _ in range(iterations):
    for i in range(m):
        #Compute the perceptron output
        prediction = step_function(np.dot(X[i],theta)+bias)
        #update weight and bias according to perceptron training rule
        error = y[i] - prediction
        theta += alpha * error * X[i]
        bias += alpha * error
#Print the updated weight and bias
print(f"updated weights {theta}")
print(f"updated bias {bias}")

#decision boundary
plt.figure(figsize=(6,4))
for i in range(len(y)):
    if y[i] == 0:
        plt.scatter(X[i,0],X[i,1],color = 'red')
    else:
        plt.scatter(X[i,0],X[i,1],color = 'blue')
x_values = np.linspace(0,1,100)

if theta[1] != 0:
    boundary = -(theta[0] + theta[1] * x_values) / theta[1]
    plt.plot(x_values, boundary, color='green', label='Decision Boundary')
else:
    print("Theta[1] is zero, boundary cannot be plotted.")

plt.title("OR gate decision boundary")
plt.xlabel("X1")
plt.ylabel("X2")
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)
plt.grid(True)
plt.legend()
plt.show()
plt.close()

#Making predictions
def prediction(x1,x2):
    x_input = np.array([x1,x2])
    output = step_function(np.dot(x_input,theta)+bias)
    return output

#get inputs from user
def get_and_out():
    print("Enter X1 and X2 value in range (0,1) to get gate output:")
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))
    if x1 not in [0,1] or x2 not in [0,1]:
        print("Invalid valued plz enter value in range of (0,1)")
        return
    output = prediction(x1,x2)
    print(f"OR gate output for input x1 = {x1} and x2 = {x2} is {output}")
get_and_out()

