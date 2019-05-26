n=raw_input("Enter the number")
n=int(n)
i=1
count=0
sum=0
while i<=n:
    if n%i==0:
        print(i)
        sum=sum+i
        i+=1
        count+=1
    else:
        i+=1

print(count)
print(sum)
