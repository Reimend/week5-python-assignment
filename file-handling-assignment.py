file= open("my_file.txt", "w")
file.write("I am raymond\n")
file.write("2023 was a great year\n")
file.write("1,2,3,4,5,6,7,8,9\n")

file = open("my_file.txt")
print(file.read())

file = open("my_file.txt", "a")
file.write("Nairobi is the capital city of Kenya\n")
file.write("Python is a good programming language\n")             
file.write("PowerlearnprojectAfrica\n")

file = open("my_file.txt")
print(file.read())


def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")



