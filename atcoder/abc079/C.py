A, B, C, D = [int(x) for x in input()]

for op1 in ['+', '-']:
    for op2 in ['+', '-']:
        for op3 in ['+', '-']:
            formula = '{}{}{}{}{}{}{}'.format(A, op1, B, op2, C, op3, D)
            if eval(formula)==7:
                print('{}=7'.format(formula))
                exit(0)
