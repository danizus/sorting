list=[2,0,4,1,5,15,45,87,9]

itr=0
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            var=list[j]
            list[j]=list[j+1]
            list[j+1]=var
            
print(list)

input()
