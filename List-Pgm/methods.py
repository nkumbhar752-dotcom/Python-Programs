# list Methods


x=[10,20,30]

# access value

print(x)
print(x[1])

# update :refvar[Index]=new_value
print(x[2])
x[2]=300
print(x[2])

# using loop

x=[10,20,30,40]
for item in x:
    print(item)

#add elements by taking user element.
x=[]
print(x)
for i in range(5):
    ip=input(f"enter {i+1} element:")
    x.append=(ip)
print(x)

# extend

x=[1,2]
print(x)
x.extend([3,4])
print(x)

# insert(index,value)

x=[11,13]
print(x)
x.insert(1,12)
print(x)

#remove(elemet)/pop(index) use clear to clear[] whole list.

x=[1,2,3,"hi",89,90]
print(x)
x.remove("hi")
print(x)
x.pop(4)
print(x)
x.clear()
print(x)

# count(value),index(vale),reverse(),copy,

x=[10,20,30,10,40,50,60,10]
print(x)
x.count(10)
print(x)
x.index(60)
print(x)
x.reverse()
print(x)
y=x.copy()
print(y)

# function

x=[30,40,50,60]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))


x=[10,30,40,50]
count=0
for i in x:
    count+=1
    print(count)

# maximum value using inbuild function

x=[10,30,40,50]
print(max(x))
max=0
for i in x:
    if i>max:
        max=i
print(max)

x=[10,20,30,40]
min=x[0]
for i in x:
    if i<min:
        min=i
print(min)

# real time example

student=[1,"sita",2,"ram",3,"pooja"]
print(student)
for i in range(len(student)):
    if i%2==0:
        print(student[i])

student=[1,"sita",2,"ram",3,"pooja"]
print(student)
for i in range(len(student)):
    if i%2!=0:
        print(student[i])

# using for loop to combine condition


student=[1,"sita",45,2,"ram",78,3,"pooja",90]
print(student)
for i in range(len(student)):
    if i%3==0:
        print(student[i])
for i in range(len(student)):
    if i%3==0:
        print(student[i+1])
for i in range(len(student)):
    if i%3==0:
        print(student[i+2])

# combine condition in one condition...

student=[1,"sita",45,2,"ram",78,3,"pooja",90];
for i in range(len(student)):
    if i%3==0:
        print(student[i])
        print(student[i+1])
        print(student[i+2])
        print("===================")

