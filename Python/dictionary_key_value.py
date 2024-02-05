# Given a dictionary, extract and print values for a specific key.
# Handle the case where the key may not exist in the dictionary.

subjects = {
    "SP": 123,
    "CPS": 234,
    "SCD": 345,
    "IS": 456,
    "ABIS": 567,
    "HCI": 678
}

key = input("Enter subject name: ")
key = key.upper()
if key in subjects:
    print("Its code is ", subjects[key])
else:
    print("Subject does not found")
