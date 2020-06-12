a=7
b=2

try:
    print("resource open")
   # print(a/b)
    k=int(input("Enter a number:"))
    print(k)

except ZeroDivisionError as e:
    print("can't divide number by zero-", e)

except ValueError as e:
    print("Enter value-", e)

except Exception as e:
    print("Something went wrong!-",e)


finally:
    print("resource closed!")


