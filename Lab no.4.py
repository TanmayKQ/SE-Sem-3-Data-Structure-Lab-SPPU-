matrixa=[]
matrixb=[]

row = int(input("Enter the number of rows on first matrix: ")) 
col = int(input("Enter the number of columns on frst matrix: "))

print("\nEnter the elements row wise")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrixa.append(a)

for i in range(row):
    for j in range(col):
        print(matrixa[i][j], end = " ")
    print()

matrixc=[]
for i in range(col):
    a=[]
    for j in range(row):
        a.append(0)
    matrixc.append(a)

for i in range(col):
    a=[]
    for j in range(row):
        matrixc[i][j]=matrixa[j][i]

print("Transpose: ")
for i in range(col):
    for j in range(row):
        print(matrixc[i][j], end = " ")
    print()

row2 = int(input("Enter the number of rows on second matrix: ")) 
col2 = int(input("Enter the number of columns on second matrix: "))

print("\nEnter the elements row wise")
for i in range(row2):
    a=[]
    for j in range(col2):
        a.append(int(input()))
    matrixb.append(a)

for i in range(row2):
    for j in range(col2):
        print(matrixb[i][j], end = " ")
    print()

if row==row2 and col==col2:
    resultmatrix=[]
    for i in range(row):
        a=[]
        for j in range(col):
            a.append(matrixa[i][j]+matrixb[i][j])
        resultmatrix.append(a)

    print("Addition is:")                
    for i in range(row): 
        for j in range(col): 
            print(resultmatrix[i][j], end = " ") 
        print()

    if row==row2 and col==col2:
        resultmatrix=[]
        for i in range(row):
            a=[]
            for j in range(col):
                a.append(matrixa[i][j]-matrixb[i][j])
            resultmatrix.append(a)

    print("Subtraction is:")                
    for i in range(row): 
        for j in range(col): 
            print(resultmatrix[i][j], end = " ") 
        print()

    print("\nFor Multiplication")

# Multiplication of two matrices

print("\nMultiplication")
row1 = int(input("Enter the number of rows:")) 
col1 = int(input("Enter the number of columns:")) 
c=0
# Initialize matrix 
matrixa = [] 
matrixb = [] 
resultmatrix=[]
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(row1):          # A for loop for row entries 
    a =[] 
    for j in range(col1):      # A for loop for column entries 
         a.append(int(input())) 
    matrixa.append(a) 
print(matrixa)
  
print("matrix is:")
# For printing first  matrix 
for i in range(row1): 
    for j in range(col1): 
        print(matrixa[i][j], end = " ") 
    print() 

row2 = int(input("Enter the number of rows:")) 
col2 = int(input("Enter the number of columns:")) 
    
for i in range(row2):          # A for loop for row entries 
    a =[] 
    for j in range(col2):      # A for loop for column entries 
         a.append(int(input())) 
    matrixb.append(a) 


print("matrix is:")
# For printing second  matrix 
for i in range(row2): 
    for j in range(col2): 
        print(matrixb[i][j], end = " ") 
    print() 
    
# For matrix multi
for i in range(row1):
    a =[] 
    for j in range(col2):
        
        for k in range(row2):
            c = c+ matrixa[i][k] * matrixb[k][j]
        
        a.append(c)
        c=0
    resultmatrix.append(a)

print("Result matrix is:")                 
# For printing the result matrix 
for i in range(row1): 
    for j in range(col2): 
        print(resultmatrix[i][j], end = " ") 
    print()
