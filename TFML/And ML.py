
def predict(A, B, WA, WB):
    result = A*WA + B*WB
    # if result < 0.5 :
    #     result = 0
    # else :
    #     result = 1
    return result

input = [[0,0],
         [0,1],
         [1,0],
         [1,1]]

expected_output = [0,0,0,1]
weight = [0,0]
flag = 1
i=0
lr = 0.1
while flag !=10:
    for i in range (len(input)):
        A,B = input[i]
        WA, WB = weight
        predicted = predict(A,B, WA, WB)
        error = expected_output[i] - predicted
        
        if error < 0:
            error = error * -1 
        if (predicted != expected_output[i]):
            WA = WA + (lr * error * A*B)
            WB = WB + (lr * error * A*B)
        i = i +1
        prev_weight = weight
        weight = [WA,WB]
        if prev_weight == weight:
            flag == 10
        

        
    
        print(f"Iteration {i}\n Weight = [{WA,WB}]")
    