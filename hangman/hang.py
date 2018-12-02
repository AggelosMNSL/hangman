def user_input():
    done = True
    while done:
        x = input('Give a Letter: ')
        if len(x) == 1:
            for i in range(97,123):
                if chr(i) in x:
                    done = False
            for i in range(65,91):
                if chr(i) in x:
                    done = False
                    x = chr(i+32)
            if '1' in x:
                done = False
    return x
