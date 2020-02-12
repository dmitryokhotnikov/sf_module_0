# 'guess a number' game imitation 
# rules:
# computer choose a number from range [a;b]
# "gamer" (algorithm) must guess that number

import numpy as np # import numpy library

# function returns mean of attempts to guess 
# a number from segment [seg] default = (1,100)
# using algorithm [game_algo] 
# with number of games [n_rep]

def test_algo(game_algo, n_rep, seg=(1,100)): 
    count_ls = []
    np.random.seed(1)  # fix random seed for predictable numbers
    random_array = np.random.randint(seg[0], seg[1]+1, size=n_rep) # create array with "random" numbers
    for number in random_array:
        count_ls.append(game_algo(number,seg)) # play the game and save current number of attempts
    score = int(np.mean(count_ls)) # mean of attempts calculate
    print(f"Algorithm guess conceived number for {score} attempts (in mean)")
    return(score)


# function returns number of attempts 
# for game with conceived number [number] from range [seg]
# uses bisection method [https://en.wikipedia.org/wiki/Bisection_method]  

def game_algo(number, seg):
    count = 1 # number of attempts 
    predict = np.random.randint(seg[0],seg[1]) # make a prediction
    left=seg[0] # left boundary
    right=seg[1]+1 # right boundary
    while number != predict: # if didn't guess
        count+=1
        if number < predict: 
            right=predict
            predict = int((right+left)/2)
        elif number > predict: 
            left=predict
            predict = int((right+left)/2)
    return(count) # return, if guess

# launch tests 
n_games = 1000 # number of games
segment = (1,100)
test_algo(game_algo, n_games, segment)