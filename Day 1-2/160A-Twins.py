def split_coins(strn):
    coin = strn.split()
    coins = list(map(int, coin))
    coins.sort()
    res = []
    while(True):
        res.append(coins.pop())
        if sum(res) > sum(coins):
            return len(res)
        
a= int(input())
b= (input())
print(split_coins(b))