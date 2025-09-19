def calculate(operation, first_num, second_num):
    if(operation == "addition"):
        return first_num + second_num
    elif(operation == "subtraction"):
        return first_num - second_num
    else:
        return;

add_operation = calculate("addition", 2, 3)
print(add_operation)

sub_operation = calculate("subtraction", 2, 3)
print(sub_operation)

