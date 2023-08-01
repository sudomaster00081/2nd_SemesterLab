input = [[0, 0],
         [0, 1],
         [1, 0],
         [1, 1]]
expected_output = [0, 0, 0, 1]
weight = [0, 0]
lr = 0.1
iteration = 0

while True:
    flag = 0
    for i in range(len(input)):
        A, B = input[i]
        result = A * weight[0] + B * weight[1]
        
        error = expected_output[i] - result
        if error < 0:
            error = error * -1
        
        if result != expected_output[i]:
            weight[0] = weight[0] + (lr * error * A * B)
            weight[1] = weight[1] + (lr * error * A * B)
            
    iteration += 1
    print(f"Iteration {iteration}\nWeight = {weight}")
    
    if iteration > 1 and weight == prev_weight:
        break
        
    prev_weight = list(weight)
