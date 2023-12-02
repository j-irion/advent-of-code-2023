with open("input.txt") as f:
    data = f.read().strip()

max_cubes = {
    "red": 12, "green": 13, "blue": 14
}

def get_possible_games_sum(data):
    ls = data.split("\n")
    sum = 0
    for l in ls:
        min_cubes = {
            "red": 0, "green": 0, "blue": 0
        }
        game = l.split(":")[1]
        plays = game.replace(",", ";").split(";")
        plays = list(map(lambda play: play[1:].split(" ") , plays))
        for play in plays:
            if int(play[0]) > min_cubes[play[1]]:
                min_cubes[play[1]] = int(play[0])
        power = 1
        for cube in min_cubes.values():
            power *= cube
        sum += power             
    return sum

print(get_possible_games_sum(data))