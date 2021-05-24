

def TreeConstructor(strArr):
  w=list()
  for i in range(0,len(strArr)):
    c=strArr[i]
    w.append(int(c[3])) #Store parent in a list
    if(i==len(strArr)-1): #This condition is true when all parent of tree stored in w
      
      for i in range(0,len(strArr)): #finding frequency of all parent
        count1=0
        k=w[i]
        
        for j in range(0,len(strArr)):
          if(k==w[j]):
            count1=count1+1
        if count1 > 2:
          return "false"
      return "true"    
         
     
         
         
       
 # code goes here
  
  

# keep this function call here 
print(TreeConstructor(input()))
