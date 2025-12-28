def generate_lucky_num(n):
    lucky = []
    def new(x):
        if x>n:
            return
        if x>0:
            lucky.append(x)
        
        
        new(x*10+4)
        new(x*10+7)
    new(0)
    return lucky
def check(x):
    l = generate_lucky_num(x)
    print(l)
    for i in l :
        if x % i == 0:
            print("YES")
            return
    print("NO") 
a = int(input())
check(a)
