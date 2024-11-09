# Write a program to update an existing dictionary with new key-value pairs.
# Ensure that it handles keys that may or may not already exist in the dictionary.

# existed dictionary
books = {
    "English": 500,
    "Physics": 700,
    "Maths": 1000,
    "Chemistry": 300,
    "Biology": 600
}

print(books)
# updating
subj = input("Enter new subject name to replace with Chemistry: ")
if subj not in books:
    price = int(input("Enter price for that book: "))
    del books["Chemistry"]
    books[subj] = price
else:
    print("This subject already exists in the dictionary")

print(books)
