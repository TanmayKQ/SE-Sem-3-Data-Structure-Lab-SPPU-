groupA=['Bruce', 'Thanos','Peter','Tony','Groot']
groupB=['Peter','Rocket','Samuel','Thanos','Jarvas']
groupC=['Gamora','Rocket','Peter','Groot']

#list of students who play both cricket and badminton
lena=len(groupA)
lenb=len(groupB)
print('list of students who play both cricket and badminton')
resultlistCB=[]
for i in range(lenb):
     for var in range (lena):
       if (groupB[i]==groupA[var]):
         resultlistCB.append(groupB[i]);
         break;
print(resultlistCB)

#number of student who play either cricket or badminton but not both
print('list of students who play either cricket or badminton but not  both')
resultlistCBN=[];
flag=0;

for i in range(lenb):
     for var in range (lena):
        if (groupB[i]==groupA[var]):
            flag=1;
     if (flag==0):    
         resultlistCBN.append(groupB[i]);
     flag=0;


for i in range (lena):  
    for var in range(lenb):
        if (groupA[i]==groupB[var]):
            flag=1;
    if (flag==0):
          resultlistCBN.append(groupA[i]);
    flag=0;

    
print(resultlistCBN)

#number of students who play neither crikcet nor badminton
print("Number of students who play neither cricket nor badminton")
resultlistCBNF=[];
lenc=len(groupC)
for i in range (lenc):
    for var in  range(lenc):
        if(groupC[i]==groupA[var]):
            flag=1
            break;
    for varl in range (lenb):
        if (groupC[i]==groupB[var]):
            flag=1;
            break;
    if (flag==0):
        resultlistCBNF.append(groupC[i]);
    flag=0;

print(len(resultlistCBNF))

#Number of students who play cricket and football but not badminton
print("Number of students who play cricket and football but not badminton")
resultlistCFNBN=[];
temp=[]
for i in range(lena):
    for j in range(lenc):
        if groupA[i]==groupC[j]:
            flag=1
            if flag==1:
                temp.append(groupA[i])
    flag=0
for i in range(len(temp)):
    for j in range(lenb):
        if temp[i]==groupB[j]:
            flag=1
            break
    if flag==0:
        resultlistCFNBN.append(temp[i])
    flag=0

print(len(resultlistCFNBN))
