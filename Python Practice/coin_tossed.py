# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

results = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]
head = 0
for result in results:
    if result == 'heads':
        head = head+1

print(f"Total no of times head appeared in the above list is {head}")
