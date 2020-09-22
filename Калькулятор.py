def ADD(x,y):
    return x + y
def MINUS(x,y):
    return x - y
def DIL(x,y):
    return x / y
def MUL(x,y):
    return x * y
i=1
try:
    x=float(input("Введите 1 число:"))
    z=str(input("Введите знак +, -, *, /:"))
    y=float(input("Введите 2 число:"))
except ValueError:
    print("Недьзя вводить буквы в число")
while i==1:
        if z=="+":
            k=ADD(x,y)
        elif z=="-":
            k=MINUS(x,y)
        elif z=="/":
            try:
                k=DIL(x,y)
            except ZeroDivisionError:
                print("Нельзя делить на ноль")
        elif z=="*":
            k=MUL(x,y)   
         
        try:
            print("Ответ: ",k)
            x=k
        except (ValueError,NameError):
            print("Нельзя вводить число в знак")
        z=str(input("Введите знак что бы продолжить или exit для выхода:"))
        if z=="exit":
            break
        try:
            y=float(input("Введите число:"))
        except ValueError:
            print("Недьзя вводить буквы в число")
        print("Для выходы введите exit или введите следующие число:")
