def sort_add(str):
    lst = str.split('+')
    lst.sort()
    res = '+'.join(lst)
    return res
 
s = input()
result_string = sort_add(s)
 
print(result_string) 