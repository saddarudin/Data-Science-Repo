# Create an empty dictionary and add at least 5 key-value pairs to it. Print the dictionary.
contacts = {
    "Saddar": 123,
    "Haseeb": 456,
    "Azhar": 789,
    "Faisal": 251,
    "Fardeen": 621
}

print("Contact:    Name:")
for key in contacts:
    print(contacts[key], "       ", key)
