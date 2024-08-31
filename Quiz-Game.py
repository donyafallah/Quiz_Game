print("Welcome to my Movie Quiz!")
start = input("Are you ready?    <choose a number> \t1)Yes \t2)No ")

if int(start) != 1:
    print("Exiting ...")
    quit()

print("Ok! Let's play")

score = 0  
total = [("*Who played Harry Potter in the movies?", "Daniel Radcliffe"),
         ("*In which year was the movie 'Titanic' released?", "1997"),
         ("*Who directed the movie 'Inception'?", "Christopher Nolan"),
         ("*Which actor played Iron Man in the Marvel movies?", "Robert Downey Jr."),
         ("*The series 'Game of Thrones' is based on the books by which author?", "George R.R. Martin")]

def Question():
    global score  
    global total  

    for question, answer in total:
        print(question)
        your_answer = input("Enter your response: ")
        if your_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect answer!")

Question()

print("Thank you for participating in this quiz")
print("Your Correct Answers: ", score, "from", len(total), "Questions")

