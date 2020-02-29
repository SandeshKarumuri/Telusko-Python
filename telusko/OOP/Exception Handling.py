a=5
b=2

try:
    print("Resource Open")
    print(a/b)
    k=int(input("Enter a number:"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a  number by zero",e)
except ValueError as e:
    print("Hey, You should enter a number")
except Exception as e:
    print("Something Went Wrong")
finally:
    print("Resource Closed")
print("Bye")