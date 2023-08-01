
def predict(A, B, WA, WB):
    result = A*WA + B*WB
    if result < 0.5 :
        result = 0
    else :
        result = 1
    return result
input = [[0,0],
         [0,1],
         [1,0],
         [1,1]]
expected_output = [0,0,0,1]
weight = [0,0]
flag = 0
i=0
lr = 0.1
j=0
while flag !=1:   
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
    print(f"Iteration {j}\n Weight = [{WA,WB}]")
    j=j+1
    prev_weight = weight
    weight = [WA,WB]
    if prev_weight == weight and flag == 0:
        flag = flag + 1
    elif prev_weight == weight and flag != 0 :
        break
    
        

        
    
       
    