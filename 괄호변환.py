def check_right(string):
    stack = []
    for i in string:
        if not stack:
            stack.append(i)
        else:
            if (i == '(' and stack[-1] == ')') or (i == ')' and stack[-1] == '('):
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return True
    else:
        return False


def split_str(string):
    a = b = 0
    for i in range(len(string)):
        if string[i] == '(': a += 1
        if string[i] == ')': b += 1
        if a != 0 and a == b: return string[:i + 1], string[i + 1:]


def main(string):
    if not string: return ''
    U, V = split_str(string)
    if check_right(U):
        return U + main(V)
    else:
        revers_u = ''
        len_U = len(U)
        for i in range(1, len_U-1):
            if U[i]=='(': revers_u.append(')')
            else: revers_u.append('(')

        return '(' + main(V) + ')' + revers_u


def solution(p):
    answer = ''
    answer = main(p)

    return answer