cricket = {}
with open("cricket.csv", "r") as f:
    for line in f:
        items = line.split(",")
        player = items[0]
        score = int(items[1])
        if player in cricket:
            cricket[player].append(score)
        else:
            cricket[player] = [score]


for player, scores in cricket.items():
    min_score = min(scores)
    max_score = max(scores)
    average = round(sum(scores)/len(scores), 2)
    print(f"{player}:\n\tMinimum Score: {min_score}\n\tHighest Score: {max_score}\n\tAverage: {average}")
