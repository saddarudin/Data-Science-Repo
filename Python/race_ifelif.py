# Let's say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for i in range(4):
    print(f"You have covered {i+1}KM distance so far")
    reply = input("Are you tired? (y/n)")
    if reply == 'y':
        print("Ops!! You didn't finish the race")
        break
    if i == 3:
        print("Congratulations! You finished the race.")
