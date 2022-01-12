def arithmetic_arranger(*args):

    # --- Parse parameters ---
    questions = [q.split() for q in args[0]] # '32 + 698' -> ['32', '+', '698']

    # Optional second argument
    if len(args) > 1:
        show_ans = args[1]
    else:
        show_ans = False

    # --- Input validation ---

    # Check num problems
    if len(questions) > 5:
        return 'Error: Too many problems.'

    for q in questions:
        # Check correct operator (+ or -)
        if q[1] not in ('+', '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'
        
        # Check numbers are bot digits
        if not q[0].isdigit() or not q[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        # Max 4 digits
        if len(q[0]) > 4 or len(q[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
    # --- If the input is validated ---

    # The individual lines
    l1, l2, l3, l4 = '', '', '', ''

    for index, q in enumerate(questions):

        # Give four spaces if not the first problem
        if index:
            l1 += ' ' * 4
            l2 += ' ' * 4
            l3 += ' ' * 4
            l4 += ' ' * 4

        # Width of the problem
        width = 2 + max(len(q[0]), len(q[2]))

        # First line
        l1 += q[0].rjust(width, ' ')

        # Second line
        l2 += q[1] + q[2].rjust(width - 1, ' ')

        # Third line
        l3 += '-' * width

        # Fourth line
        if q[1] == '+':
            ans = int(q[0]) + int(q[2])
        else:
            ans = int(q[0]) - int(q[2])
        l4 += str(ans).rjust(width, ' ')
        
    # Return
    if show_ans:
        return f'{l1}\n{l2}\n{l3}\n{l4}'
    else:
        return f'{l1}\n{l2}\n{l3}'

print(arithmetic_arranger(['24 + 8525', '3801 - 2', '45 + 43', '123 + 49'], True))