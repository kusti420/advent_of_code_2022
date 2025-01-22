left = []                                               
right = []                                            
sm = 0                                                  
for line in data:
    line = [int(i) for i in line.split()]
    left.append(line[0])
    right.append(line[1])    
right.sort()                                            left.sort()                                                                            values = []                                             
for i in range(len(left)):                                  
    values.append(abs(left[i] - right[i]))              for i in left:                                             
    sm += i * right.count(i)                            print(sum(values), len(values))                         print(sm)
