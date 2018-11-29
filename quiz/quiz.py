def show_menu():
    print("1. Ask questions")
    print("2. Ad questions")
    print("3. Exit game")
    
    option = input("Enter option: ")        #option variable. input function to get the text. prompt "enter option"
    return option                                       #return option that user selects
    
#print(show_menu())  #test code so far using print function to call it. cd into quiz folder

def ask_questions():            #create 2 empty lists for Q & A
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()   #read file in and split the lines. put in variable lines
        
    for i, text in enumerate(lines):#enumerate function turns each list into a tuple.line num stored in i.text in text
        if i%2 == 0:
            questions.append(text)  #if line number is even..Q
        else:
            answers.append(text)
    
    #add functionality to check answers and keep score
    number_of_questions = len(questions) #check length of questions list
    questions_and_answers = zip(questions, answers) #var Q&A and call zip function on this
    
    score = 0       #initialize empty var called score set to zero
    
            
    # for question, answer in zip(questions, answers): #take Q&A and use zip function to put them together in tuple in memory
    #     guess = input(question + "> ")  #do an input with our guess
        
    for question, answer in questions_and_answers:  #this replaced above lines. replaced zip with Q&A function
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("right!")
            print(score)
        else:
            print("wrong!")
            
    print("You got {0} correct out of {1}".format(score, number_of_questions))
        
        

def add_question():
    print("")
    question = input("Enter a question\n> ")        #store in question variable using input
    
    print("")
    print("OK then, Tell me the answer")
    answer = input("{0}\n> ".format(question)) #store in answer variable using input. take question.blank line >prompt
               #using format method we insert question. user will be asked question when they go to submit the answer

    file = open("questions.txt", "a")                   #add this to questions.txt in append mode
    file.write(question +  "\n")                        #write question with new line at end
    file.write(answer + "\n")                           #write anser with new line at end
    file.close()   


def game_loop():
    while True:         #shortcut for loop forever unless theres a break
        option = show_menu()  #call show_menu function and store chosen option in option variable
        if option == "1":
             ask_questions()                                                            #print("You selected 'Ask questions'")
        elif option == "2":
            add_question()                                               # print("You selected 'Add a question'")
        elif option == "3":
            break                                   #quit game. breaks out of loop
        else:
            print("Invalid option")
        print("")                                   #print blank line


game_loop()

#use cat questions.txt to see contents of file in workspace

