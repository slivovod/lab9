def concatenation(first_number, second_number, string):
    con_result = string + str(first_number + second_number)
    return con_result

a = int(input("first number = "))
b = int(input("second number = "))
anything = str(input("enter string/text/anything: "))
print(concatenation(a, b, anything))