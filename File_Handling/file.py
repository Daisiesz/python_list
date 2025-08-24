#Creating a new file. 
file = open("newdocument.txt", "w")

# Writing to the file
file.write("I'm learning Python.")

# Reading the file
file = open("newdocument.txt", "r")
print(file.read())

# Handling errors
try:
    file = open("newdocument.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
finally:
    file.close()
