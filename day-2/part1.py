with open("input.txt") as f:
    data = f.read().strip()

max_cubes = {
    "red": 12, "green": 13, "blue": 14
}

def get_possible_games_sum(data):
    ls = data.split("\n")
    sum = 0
    for l in ls:
        game, plays = l.split(":")
        game_number = int(game.split(" ")[1])
        plays = plays.split(";")
        possible = True
        for play in plays:
            if possible == False:
                break
            cubes = list(map(lambda cube: cube[1:].split(" "), play.split(",")))
            for cube in cubes:
                if int(cube[0]) > max_cubes[cube[1]]:
                    possible = False
                    break
        if possible == True:
            print(game_number)
            sum += game_number
                
                    
    return sum

print(get_possible_games_sum(data))