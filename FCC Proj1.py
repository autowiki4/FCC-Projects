def arithmetic_arranger(problems, solve=None):
    global modified_i, solution
    global index
    global arranged_problems
    arranged_problems = ''
    arrange_problems = []

    # Test for maximum number of items in list
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in problems:
        # Index the addition or subtraction operator
        try:
            index = i.index('+')
        except:
            try:
                index = i.index('-')
            except :
                # Prevent the use of '*' or '/' operator
                if '*' in i or '/' in i:
                    return "Error: Operator must be '+' or '-.'"

        # Ensure numbers entered consist of digits
        int_1 = i[:index-1]
        int_2 = i[index+2:]
        if not int_1.isdigit() or not int_2.isdigit():
            return "Error: Numbers must only contain digits."

        # Ensure that numbers entered contain at most four(4) digits
        if len(int_1) > 4 or len(int_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            pass

        # solve the arithmetic operation using the optional variable
        if solve == True:
            solution = str(eval(i))
        else:
            pass

        if solve == True:
            # Code to represent the arithmetic operation in new lines
            if max(len(int_1), len(int_2)) == 1:
                modified_i = f'{int_1.rjust(3)}\n{i[index]} {int_2.rjust(1)}\n---\n{solution.rjust(3)}'
            elif max(len(int_1), len(int_2)) == 2:
                modified_i = f'{int_1.rjust(4)}\n{i[index]} {int_2.rjust(2)}\n----\n{solution.rjust(4)}'
            elif max(len(int_1), len(int_2)) == 3:
                modified_i = f'{int_1.rjust(5)}\n{i[index]} {int_2.rjust(3)}\n-----\n{solution.rjust(5)}'
            elif max(len(int_1), len(int_2)) == 4:
                modified_i = f'{int_1.rjust(6)}\n{i[index]} {int_2.rjust(4)}\n------\n{solution.rjust(6)}'
        else:
            # Code to represent the arithmetic operation in new lines
            if max(len(int_1), len(int_2)) == 1:
                modified_i = f'{int_1.rjust(3)}\n{i[index]} {int_2.rjust(1)}\n---'
            elif max(len(int_1), len(int_2)) == 2:
                modified_i = f'{int_1.rjust(4)}\n{i[index]} {int_2.rjust(2)}\n----'
            elif max(len(int_1), len(int_2)) == 3:
                modified_i = f'{int_1.rjust(5)}\n{i[index]} {int_2.rjust(3)}\n-----'
            elif max(len(int_1), len(int_2)) == 4:
                modified_i = f'{int_1.rjust(6)}\n{i[index]} {int_2.rjust(4)}\n------'

        arrange_problems.append(modified_i)

    if solve == True:
        # print the arithmetic in new lines
        first_lines = '    '.join(string.split('\n')[0] for string in arrange_problems)
        second_lines = '    '.join(string.split('\n')[1] for string in arrange_problems)
        third_lines = '    '.join(string.split('\n')[2] for string in arrange_problems)
        fourth_lines = '    '.join(string.split('\n')[3] for string in arrange_problems)
        arranged_problems = f'{first_lines}\n{second_lines}\n{third_lines}\n{fourth_lines}'
    else:
        # print the arithmetic in new lines
        first_lines = '    '.join(string.split('\n')[0] for string in arrange_problems)
        second_lines = '    '.join(string.split('\n')[1] for string in arrange_problems)
        third_lines = '    '.join(string.split('\n')[2] for string in arrange_problems)

        arranged_problems = f'{first_lines}\n{second_lines}\n{third_lines}'

    return arranged_problems

# Test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))