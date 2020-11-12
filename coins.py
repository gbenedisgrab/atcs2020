coins = [1,2,5,10,20,50,100,200]
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
    i = 0
    pass
    for i in range(len(combo)):
        combo[i]+=1
    
def coin_combinations(goal):
    solutions = []
    amounts = [0]*len(coins)
    



print(coins_solutions(coins,goal))
coin_combinations(coins,goal)
print(get_val(coins,[1]*len(coins)))

