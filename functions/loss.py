import numpy as np 
import math 

softmax_output = [0.7, 0.1, 0.2]

target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print(loss)
print(-math.log(0.7))

print(-math.log(0.5))


softmax_output = np.array([ 
                    [0.7, 0.1, 0.2],
                    [0.1, 0.5, 0.4],
                    [0.02, 0.9, 0.08]
                ])
target_output = [1, 0, 0]

print(softmax_output[[0,1,2], target_output])