# accessing and modifying list....

number = [34,54,2,65,43]
print(number[0])
print(number[4])
number[2] = 44
print(number)

#..........removing items......
# remove(item): removes first occurrence of an item
# pop(): removes item at a position (default last) and gives it to you
# clear(): removes all items

fruits = ["mango","pineapple","banana","orange"]
print(fruits)
fruits.remove("mango")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

#........ List slicing..............
# Meaning: Take a part of the list. Think of it as “cutting a piece” without touching original.
# Syntax: list[start:end] → includes start but excludes end.

name = ["ram","anchal","shekhar","lucky","harsh","parkash"]
print(name[1:4])  # ["anchal","shekhar","lucky"]
print(name[:3])   # first 3 items 
print(name[2:4])   # middle two names
 
#...........Sorting lists..........
# sort(): sorts the list permanently in ascending order
# sort(reverse=True): descending
# sorted(): temporary sort, original list stays the same  

points = [34, 656, 76, 83, 753, 65, 245]
print("Original list:", points)

# Sort ascending
points.sort()
print("Sorted ascending:", points)

# Sort descending
points.sort(reverse=True)
print("Sorted descending:", points)

# Using sorted() to create a new list
new_points = sorted([34, 76, 83, 65])
print("New sorted list:", new_points)


# List of strings
fruits = ["mango", "apple", "banana", "kiwi", "cherry"]
print("Original list:", fruits)

# Sort ascending (alphabetical order)
fruits.sort()
print("Sorted ascending:", fruits)

# Sort descending (reverse alphabetical order)
fruits.sort(reverse=True)
print("Sorted descending:", fruits)

# Using sorted() to create a new sorted list
new_fruits = sorted(["orange", "grape", "apple", "melon"])
print("New sorted list:", new_fruits)
