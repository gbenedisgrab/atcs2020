coins = [1,2,5,10,20,50,100,200,500]
goal = 200

def coins_solutions(goal):
    solutions = [1] + ([0]*goal)
    for coin in coins:
        for j in range(coin, goal+1):
            solutions[j] += solutions[j-coin]
    return solutions[goal]

def get_val(amounts):
    return sum([coins[i]*amounts[i] for i in range(len(coins))])

def next_combo(combo):
    c = combo[:]
    for i in range(len(c)):
        c[i]+=1
        if get_val(c) > goal:
            c[i] = 0
        else:
            return c
    return False
    
def coin_combos(goal):
    amounts = [0]*len(coins)
    while amounts:
        if get_val(amounts) == goal:
            yield amounts
        amounts = next_combo(amounts)

print(coins_solutions(goal))

with open('combos.txt','w') as f:
    for combo in coin_combos(goal):
        f.write(','.join(map(str,combo))+'\n')

