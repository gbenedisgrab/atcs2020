import time

coins = [1,2,5,10,20,50,100,200]

def count_coin_solutions(goal):
    solutions = [1] + ([0]*goal)
    for coin in coins:
        for j in range(coin, goal+1):
            solutions[j] += solutions[j-coin]
    return solutions[goal]

def get_val(amounts):
    return sum([coins[i]*amounts[i] for i in range(len(coins))])

def next_combo(combo,goal):
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
        amounts = next_combo(amounts,goal)

def build_solutions(goal):
    solutions = [[[]]] + [[] for _ in range(goal)]
    for coin in coins:
        for j in range(coin, goal+1):
            solutions[j].extend([combo+[coin] for combo in solutions[j-coin]])
    return solutions[goal]

def writeit(solutions, file_name):
    with open(file_name,'w') as f:
        for combo in solutions:
            f.write(','.join(map(str,combo))+'\n')

def main():
    value = 8

    start = time.time()
    print(count_coin_solutions(value),'time',time.time()-start)

    start = time.time()
    writeit(coin_combos(value),'combos1.txt')
    print('finished first method','time',time.time()-start)

    start = time.time()
    writeit(build_solutions(value),'combos2.txt')
    print('finished second method','time',time.time()-start)

main()
