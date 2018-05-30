for i in range(5,9):
    for j in range(5,9):
        for k in range(5,9):
            if(i!=k)and(i!=j)and(j!=k):
                print(100*i+10*j+k) 
