import random
dice_values = [1,2,3,4,5,6]

n_iter = 1000000
win = 0

for _ in range(n_iter):

    # start from stair 0
    current_stair = 0

    # set number_move_up = 0
    number_move_up = 0

    while True:
        # get random dice_value
        rand_dice_value = random.choice(dice_values)
        
        if rand_dice_value in [1,2]:
            # move down 1 stair
            current_stair -= 1
            # if current_stair is 0 we still stay at stair 0
            current_stair = max(current_stair,0)
        elif rand_dice_value in [3,4,5]:
            # move up 1 stair
            current_stair += 1
            # update number_move_up
            number_move_up += 1
        else: # rand_dice_value == 6
            current_stair += random.choice(dice_values)

        if number_move_up == 100:
            # we stop the game
            if current_stair >= 60:
                win += 1
            break
        else:
            # we stop the game if we reach stair 60 or higher
            if current_stair >= 60:
                win += 1
                break
            else: # we continue the game
                pass

print('Winning probability is: ', win/n_iter)

        