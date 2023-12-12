import numpy as np

# dot product for a single neuron
inputs = [1, 2, 3, 2.5]
weights =[0.2, 0.8, -0.5, 1.0]
bias = 2

output = np.dot(inputs, weights) + bias
print ("this is output using numpy",output)

# dot product for 3 neurons 

inputs = [1, 2, 3, 2.5]
weights_n1 =[[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases_n1 = [ 2, 3, 0.5]
output = np.dot(weights_n1, inputs) + biases_n1
print ("this is output using numpy",output)
