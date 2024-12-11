def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
      
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  

arr=[]
Num=int(input("Enter the number of students "))
for i in range (Num):
    per=float(input("Enter the percentage marks "))
    arr.append(per)

bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%f" %arr[i]),  

arr2=arr[::-1]
print("Top 5 Marks ")
if len(arr2) > 5:
    for i in range(5): 
        print("%f" %arr2[i])
else:
    for i in range(len(arr2)): 
        print("%f" %arr2[i])

def selectionSort(arr1):
    
    for i in range(len(arr1)): 
        min_idx = i 
        for j in range(i+1, len(arr1)): 
            if arr1[min_idx] > arr1[j]: 
                min_idx = j
                
              
    # Swap the found minimum element with  
    # the first element         
        arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i] 
  
arr1=[]
Num=int(input("Enter the number of students "))
for i in range (Num):
    per=float(input("Enter the percentage marks "))
    arr1.append(per)

selectionSort(arr1)
# Driver code to test above 
print ("Sorted array") 
for i in range(len(arr1)): 
    print("%f" %arr1[i])

arr2=arr1[::-1]
print("Top 5 Marks ")
if len(arr2) > 5:
    for i in range(5): 
        print("%f" %arr2[i])
else:
    for i in range(len(arr2)): 
        print("%f" %arr2[i])
