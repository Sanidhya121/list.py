# Create a list
my_list = [1, 2, 3, 4, 5]

# Add an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modify an element in the list
my_list[1] = 10
print("List after modifying an element:", my_list)

# Create a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Add a new key-value pair to the dictionary
my_dict["occupation"] = "Engineer"
print("Dictionary after adding a new key-value pair:", my_dict)

# Remove a key-value pair from the dictionary
del my_dict["age"]
print("Dictionary after removing a key-value pair:", my_dict)

# Modify the value of a key in the dictionary
my_dict["city"] = "Los Angeles"
print("Dictionary after modifying a value:", my_dict)

# Create a set
my_set = {1, 2, 3, 4, 5, 5}  # Duplicate elements are automatically removed

# Add an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Remove an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Modify an element in a set is not possible as sets are unordered and do not have indices
# my_set[1] = 10  # This will raise an error

# Create a new set with modified elements
new_set = {10, 2, 4, 5, 6}
print("New set with modified elements:", new_set)