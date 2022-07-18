 def flatten_list(n_list):
    result_list = []
    if not n_list:
        return result_list
    stack = [list(n_list)]
    print('stack:',stack)
    while stack:
        c_num = stack.pop()
        print('c_num:',c_num)
        next = c_num.pop()
        print('next',next)
        if c_num:
            stack.append(c_num)
            if isinstance(next, list):
                if next:
                    stack.append(list(next))
            else:
                 result_list.append(next)
            print('stack:',stack)
    result_list.reverse()
    return result_list
n_list = [0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
print('Original list',n_list)
print('\n Flatten list',flatten_list(n_list))
