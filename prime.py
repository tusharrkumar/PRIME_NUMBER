
## WAP to check given number is prime or not??

n=int(input("Enter The Number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime number")
