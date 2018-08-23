#question1

def areaOfSphere(radius):
    area=4/3 * 3.14 * (radius**2)
    return area
a=int(input ())
area=areaOfSphere(5)

print(area)

#question 2

def perfect(number):
      sum=0
      for i in range(1,number):
            if number%i is 0:
                  sum=sum+i

      if sum == number:
            return number
      else:
            return 0


for i in range(1,1001):
      p=perfect(i)
      if p is not 0:
            print(p)


#question 3

a=int(input("enter a number"))
for i in range(1,11):
      print(i*a)

#question 4

def power(n,m):
    if m is 1:
        return n
    else :
      a= power(n,m-1)
      return (n*a)
n=int(input("enter a number"))
m=int(input("enter a number"))
number=power(n,m)
print("n^m=",number)
