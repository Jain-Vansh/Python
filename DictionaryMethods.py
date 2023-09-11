# Functioning of the dictionary methods

d1 = {
    "Name" : "Vansh",
    "Age" : 20,
    "Gender" : "Male"
}

d2 = {
    "Name" : "Natasha",
    "Age" : 20,
    "Gender" : "Female"
}

d1.update({"Name":"Nathan"})
print(d1)
d1.clear()
print(d1)
d2.pop("Age")
print(d2)
d2.popitem()
print(d2)
del d1



