print(dir(str))

# Question 1: Create 3 variables to store street, city and country. Now create address
# variable to store entire address. Print address in such a way that all three variables
# are printed in separate lines

street = "Bukhari Colony"
city = "Dadu"
country = "Pakistan"
print(f"Street: {street}\nCity: {city}\nCountry: {country}")


# Question 2: Create a variable to store "The earth revolves around the sun"
# Print: "revolves" using slicing operator
# Print: "sun" using negative index

s = "The earth revolves around the sun"
# first find index of revolves
ri = s.index("revolves")
# Now we know that total characters in "revolves" are 8 so
revolves = s[10:18]
print(revolves)

# for "sun" using negative index
print(s[-3:])


# Question 3: Create two variable to store how many fruits and vegetable you eat in a day
# Now print "I eat x vaggies and y fruits daily" where x represents fruits and y represents vegetables

fruit = "oranges, mosami, banana, apple, cheeko"
vegetable = "potato, chola, mixSabzi, daal, palak"
print(f"I eat {fruit} fruits and \n{vegetable} vegetables daily")


# Question 4: I have a string variable called "Maine 200 banana khaye". This ofcourse is a wrong
# statement, the correct statement is "Maine 10 samosa khaye". Replace incorrect words in
# original string with new ones and print new string. Also try to do this in one line.

s = "Maine 200 banana khaye"
s = s.replace("200 banana", "10 samosa")
print(s)



# Question: Write a program that takes file name with extension as an input and prints only file name without extension
# You can assume that extenstion is three character long.

file_name = input("Enter file name with extension: ")
print(file_name[:len(file_name)-4])
