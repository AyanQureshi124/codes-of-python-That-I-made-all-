a = int(input('Enter your 1st number:'))
b = int(input('Enter your 2nd number:'))
c = int(input('Enter your 3rd number:'))

if a>b and a>c:
    print("a is the greater one:")

elif b>a and b>c:
    print("b is the greater one:")

elif c>a and c>b:
    print("c is the greater one:")
    
elif a==b and b==c and c==a:
    print("All values are equal")

