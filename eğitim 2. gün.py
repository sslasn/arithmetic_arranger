
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        max_width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(max_width) + '    '
        second_line += operator + ' ' + num2.rjust(max_width - 2) + '    '
        dash_line += '-' * max_width + '    '

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line += ' ' + result.rjust(max_width) + '    '

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()
    if show_answers:
        arranged_problems += '\n' + answer_line.rstrip()

    return arranged_problems

result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)
print(result)
