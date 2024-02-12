"""
We have the following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21

Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
a) print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
b) add: if user input add then it should further ask for a country name to add. If country already
exist in our dataset then it should print that it exist and do nothing. If it doesn('t then it asks '
'for population and add that new country/population in our dictionary and print it)
c) remove: when user inputs remove it should ask for a country to remove.
If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
Else print that country doesn't exist!
d) query: on this again ask user for which country he or she wants to query.
When user inputs that country it will print population of that country.
"""

population = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}

choice = int(input("1.Print\n2.add\n3.remove\n4.query\nselect any one: "))
if choice == 1:
    for country in population:
        print(f"{country} ==> {population.get(country)}")

elif choice == 2:
    country = input("Enter country name: ")
    if country not in population:
        num = int(input("Enter its population (in crores): "))
        population[country] = num
        for c in population:
            print(f"{c} ==> {population.get(c)}")

    else:
        print("This country already exists")
elif choice == 3:
    country = input("Enter country name to remove it: ")
    if country in population:
        del population[country]
        for c in population:
            print(f"{c} ==> {population.get(c)}")
    else:
        print("Country does not exits in our database")
elif choice == 4:
    country = input("enter country name: ")
    if country in population:
        print(f"{country} ==> {population[country]}")
    else:
        print("This country is not in our database")

