func1 = lambda x: x+1
func2 = lambda x: x+2

def func3(x):
    print(f"[in func3] current {x=}")
    return x+3

def func4(x):
    print(f"[in func4] current {x=}")
    return x+4

func_list = [func1, func2, func3, func4]

a = 0
# for each_func in func_list:
#     a = each_func(a) 


a = each_func(a) for each_func in func_list

print(a)
