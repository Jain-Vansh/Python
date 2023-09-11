#Accessing the keys and values in a dictionary

dict = {
    "name" : "Vansh",
    "age" : 20,
    "gender" : "Male"
}

print(dict.keys())
print(dict.values())
print(dict.items())

#Accessing the key value pairs using loop

for key, value in dict.items():
    print(f"The value for key '{key}' is '{value}'")