
first_name = "Master"
last_name = "Chief"

print("variable + variable")
print(first_name+" "+last_name)

first_name = "Spartan"
surname = "Oneoneseven"

print("using .format with variables")
print("My first name is {}. My family name is {}".format(first_name,surname))
print()

print("using fstrings with variables")
print(f"My first name is {first_name}. My family name is {surname}")
print()

my_int = 30
sentence = "The number I am thinking of is: "

print("string variable + int cast to string")
print(sentence + str(my_int))
print()

user = {"first_name":"Steven"}

print("dictionary object")
print(user)
print()

print("print dictionary[key]")
print(user["first_name"])
print()

user["family_name"] = "Laszloffy"
print("print dictionary after add entry")
print(user)
print()

user["first_name"] = "Stephanie"
print("print dictionary after edit entry")
print(user)
print()

del user["family_name"]
print("print dictionary after delete entry")
print(user)
print()

fruit = []
froot = ["apples","oranges","bananas"]

print("print list entry at index 1")
print(froot[1])
print()

print("print the number of items in the list")
print(len(froot))
print()

print("print item at end of list using index -1")
print(froot[-1])
print()

froot.append("kiwi")

print("print list after append 'kiwi'")
print(froot)
print()

froot.insert(2, "passion fruit")

print("print list after inserting 'passion fruit' at index 2")
print(froot)
print()

print("print sorted list")
print(sorted(froot))
print()

print("print list, note order hasn't changed")
print(froot)
print()

froot.sort()

print("print list after using sort() function. note order HAS changed")
print(froot)
print()

froot.reverse()

print("print reversed list. Note order HAS changed")
print(froot)
print()

del froot[1]

print("print list after deleting object at index 1")
print(froot)
print()

favourite_fruit = froot.pop(2)

print("print variable filled with list.pop[2].")
print(favourite_fruit)
print()

print("Note pop removes item from list")
print(froot)
print()

froot.remove('apples')

print("print list after .remove")
print(froot)
print()

my_var = "That is a nice boulder. I like that boulder."
print("print the type of variable using type()")
print(type(my_var))