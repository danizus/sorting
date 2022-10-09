def merge(list):
    if len(list)>1:
        left=list[:len(list)//2]
        right=list[len(list)//2:]
        merge(left)
        merge(right)
        i,j,k=0,0,0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i +=1
                k+=1
            else:
                list[k]=right[j]
                j +=1
                k+=1
        while i<len(left):
                list[k]=left[i]
                i=i+1
                k +=1
        while j<len(right):
                list[k]=right[j]
                j=j+1
                k +=1
                
    
    return(list)    
        

list=[1,100,4,2,3]
print(merge(list))




