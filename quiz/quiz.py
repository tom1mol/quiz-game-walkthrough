def show_menu():
    print("1. Ask questions")
    print("2. Ad questions")
    print("3. Exit game")
    
    option = input("Enter option: ")        #option variable. input function to get the text. prompt "enter option"
    return option                                       #return option that user selects
    
#print(show_menu())  #test code so far using print function to call it. cd into quiz folder

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
            print("You selected 'Ask questions'")
        elif option == "2":
            add_question()                                               # print("You selected 'Add a question'")
        elif option == "3":
            break                                   #quit game. breaks out of loop
        else:
            print("Invalid option")
        print("")                                   #print blank line


game_loop()

#use cat questions.txt to see contents of file in workspace

