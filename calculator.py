import math
def calculater():
    for i in range(0,100):
        a=int(input("enter digit: "))
        b=int(input("enter digit: "))
        print("What type of opration do you want you perform")
        user_input=int(input("Enter 1/Addition, 2/Sub, 3/Divition, 4/Multiplaction, 5/power, 6/squar root: "))

        if user_input == 1:
            print(a+b)
        elif user_input == 2:
            print(a-b)
        elif user_input == 3:
            print(a/b)
        elif user_input == 4:
            print(a*b)
        elif user_input == 5:
            print(pow(a,b))
        elif user_input == 6:
            c=int(input("enter 1/a, 2/b: "))
            if c == 1:
                print(math.sqrt(a))
            elif c ==2:
                print(math.sqrt(b))
        else:    
            print("this fanction is not avileble")

        user_input=int(input("Are you want to continue your calculation, 1/no, 2/yes : "))

        if user_input == 1:
            print("Thankyou for using my calculator"),exit()
    
