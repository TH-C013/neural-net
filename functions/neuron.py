# 1 neuron with 3 inputs 
input_n1 = [1, 2, 3]
weights_n1 = [0.2, 0.8, -0.5]
bias_n1 = 2

output_n1 = input_n1[0]*weights_n1[0] + input_n1[1]*weights_n1[1] + input_n1[2]*weights_n1[2] + bias_n1
print('Output for 1 neuron with 3 inputs output_n1 = ',output_n1)

# 1 neuron with 4 inputs 
input_n2 = [1, 2, 3, 2.5]
weights_n2 = [0.2, 0.8, -0.5, 1.0]
bias_n2 = 2

output_n2 = input_n2[0]*weights_n2[0] + input_n2[1]*weights_n2[1] + input_n2[2]*weights_n2[2] + input_n2[3]*weights_n2[3] + bias_n2
print('Output for 1 neuron with 4 inputs output_n2 = ',output_n2)

# 3 neurons with 4 inputs 
input_n3 = [1, 2, 3, 2.5]
weights1_n3 = [0.2, 0.8, -0.5, 1.0]
weights2_n3 = [0.5, -0.91, 0.26, -0.5]
weights3_n3 = [-0.26, -0.27, 0.17, 0.87]

bias1_n3 = 2
bias2_n3 = 3
bias3_n3 = 0.5

output_n3 = [   input_n3[0]*weights1_n3[0] + input_n3[1]*weights1_n3[1] + input_n3[2]*weights1_n3[2] + input_n3[3]*weights1_n3[3] + bias1_n3,
                input_n3[0]*weights2_n3[0] + input_n3[1]*weights2_n3[1] + input_n3[2]*weights2_n3[2] + input_n3[3]*weights2_n3[3] + bias2_n3,
                input_n3[0]*weights3_n3[0] + input_n3[1]*weights3_n3[1] + input_n3[2]*weights3_n3[2] + input_n3[3]*weights3_n3[3] + bias3_n3 ]

print('Output for neuron 1 of 3 with 4 inputs output1_n3 = ',output_n3)

# 3 neuron with 4 input optimized 

input_n4 = [1, 2, 3, 2.5]

weights_n4 =[[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases_n4 = [ 2, 3, 0.5]

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights_n4,biases_n4):
    neuron_output = 0
    for n_input, weight in zip(input_n4,neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)


print('Output for 3 neuron with 4 inputs layer_outputs= ',layer_outputs)


lolol = [
        [[1,2],[3,4]],
        [[5,6],[7,8]],
        [[9,10],[11,12]] 
]