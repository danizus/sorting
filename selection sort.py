list=[7,8,0,2,1,5]
for i in range(len(list)):
    min=i
    for j in range(i,len(list)):
        if list[min]>list[j]:
            min=j
    var=list[i]
    list[i]=list[min]
    list[min]=var
print(list)

    
input()