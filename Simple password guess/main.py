password = "secret"

while True:
    answer = input("Enter password: ")
    if answer is not password:
        print("Incorrect.")

    if answer == password:
        f = open("file.txt", "r")
        print(f.read())
        break
