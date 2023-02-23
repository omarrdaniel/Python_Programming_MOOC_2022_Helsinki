# Write your solution here
def who_won(game_board: list):
    points1 = 0
    points2 = 0
 
    for row in game_board:
        for square in row:
            if square == 1:
                points1 += 1
            elif square == 2:
                points2 += 1
    
    if points1 > points2:
        return 1
    elif points2 > points1:
        return 2
    else:
        return 0