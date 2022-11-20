def greeting (name):
    return f"Hello, {name}!"

questions = ['What is the color of apple?', 'What is the color of orange?', 'What is the color of banana?']
answers = ['red', 'orange', 'yellow']

name = input("Enter your name: ")

print(greeting(name))

quiz = input("Do you wish to complete a quiz? Press '1', if you want: ")

if quiz == '1':
    print(questions[0])
    answer = input("Enter answer: ")
    if answer == answers[0]:
        print("Correct!")
        print(questions[1])
        answer = input("Enter answer: ")
        if answer == answers[1]:
            print("Correct!")
            print(questions[2])
            answer = input("Enter answer: ")
            if answer == answers[2]:
                print("Correct!")
            else:
                print("Incorrect!")
        else:
            print("Incorrect!")
    else:
        print("Incorrect!")
else:
    print("Thank you for visiting! Goodbye!")

print("Thank you for visiting! Goodbye!")
