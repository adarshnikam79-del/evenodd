def evenodd(n):
    return n % 2 == 0

num = int(input("Enter a number: "))

if evenodd(num):
    print( "is an Even number." , num )
else:
    print( "is an Odd number." , num )