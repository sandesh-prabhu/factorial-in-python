while 1:
    def fact(n):
        if n<=1:
            return 1
        else:
            return n*fact(n-1)
    num=input("Enter a number(enter nothing to quit):")
    if num=="":
        break
    elif not num.isnumeric() or int(num)<0:
        print("Enter a positive integer")
    else:
        print(fact(int(num)))
