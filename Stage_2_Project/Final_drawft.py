#The parts which shall be replaceda
blank_list = ["__1__", "__2__", "__3__", "__4__"]

#The strings for the different difficultys
easy_questions = "The capital of Germany is __1__,\nThe capital of Italy is __2__,\nThe capital of France is __3__, \nThe capital of The Netherlands is __4__"

medium_questions = "The capital of Denmark is __1__,\nThe capital of China is __2__,\nThe capital of the USA is __3__,\nThe capital of Spain is __4__"

hard_questions = "The capital of Portugal is __1__,\nThe capital of Brasil is __2__,\nThe capiatl of Argentinien is __3__,\nThe capital of Mexico is __4__"

easy_answers = ["Berlin", "Rom", "Paris", "Den Haag"]
medium_answers = ["Kopenhagen", "Bejing", "Washington D.C.", "Madrid"]
hard_answers = ["Lisabon", "Brasilia", "Buenos Aires", "Mexico City"]


global counter
counter = 0
global limit_attempts
limit_attempts = 0

# Ask the user how many guesses he would like to have
def How_many_times():
	global wrong_limit
	wrong_limit = int(raw_input("How many guesses would you like per problem?(Maximum 5) ")) #Input: How many tries you think you need
	global chances #Putting the Input(tries) in the function wrong_limit and connect it with chances, so we can use it
	chances = wrong_limit
	difficulty_choice() #The Output of this function is the variable chances, after that it returns the function difficulty_choice



#This function prompts the user to pick a difficulty and returns the initiate_game function
def difficulty_choice():
	global difficulty
	choice = raw_input("Pick a difficulty by typing easy, medium, or hard.\n")
	difficulty = choice # The Input of this function is the difficulty, in which you want to play the game. Putting the answer in the variable choice
	if choice=="easy":
		return initiate_game(easy_questions, easy_answers)
	if choice=="medium":
		return initiate_game(medium_questions, medium_answers)
	if choice=="hard":
		return initiate_game(hard_questions, hard_answers) #After the Input of the user, the function checks and returns as Output the initiate_game function
	else:
		return difficulty_choice() #in case of a wrong answer the function returns to its beginning



#Function starts the game, and boxing the questions in the function final_text
def initiate_game(questions, answers):
		print "You choose difficulty " + difficulty + "\nGood luck!!!^^"
		final_text = questions
		game (final_text, answers, counter, chances) #leads to the next function game


#This function runs the game and loops through the whole thing
def game(final_text, answers, counter, chances):
		  while counter < len(blank_list): #loops through the blanks as long as there are blanks
				print "The current paragraph reads as such: " + final_text #shows the questions with the blanks
				user_answer=raw_input("What word replaces"+blank_list[counter]+"?\n") #asks the user what is the replacement
				if answer_check (user_answer, answers[counter]) == True: #is linked to the function answer_check which checks if the answer is valid
						  chances = wrong_limit
						  final_text = final_text.replace((blank_list[counter]), user_answer) #if the answer is true it replace the blank in the text with the answer
				else:
					chances = chances-1 #wrong answer costs you one trie...
					if  chances == limit_attempts: #if you reach the answer limit the game end
						 print "Game over..Thanks for playing!"
						 quit()
					else:
						 wrong_answer_countdown(chances) #if you have tries left, you can take another shoot
						 return game(final_text, answers, counter, chances)
				counter = counter+1 #was the answer correct, the count goes on and you move to the next question
		  if counter == len(blank_list): #if we reach the end of the list, the game is over
			  print final_text # prints the text with the correct answers in it
			  print "Congratulations\nThanks for playing!"

#This function takes the user's answer and checks it against the provided answers. Input is users guess and the answer for the blanks
def answer_check (user_answer, answer):
	   if user_answer.lower() == answer.lower(): #lower the input just in case ;)
			  print "\nCorrect!"
			  return True #output true
	   else:
			  return False #or output false

def wrong_answer_countdown(chances): #takes chances as input and show the user how many tries are left as a output
	if chances == (chances-1):
		print "Try again mate!\nYou have " + str(chances) + " more tries.."
	elif chances == (chances-2):
		print "Try again mate!\nYou have " + str(chances) + " more tries.."
	elif chances == (chances-3):
		print "Try again mate!\nYou have " + str(chances) + " more tries.."
	elif chances == (chances-4):
		print "Oh boy!!\nThat is your last try.."

#Introducting
Introducting = "Welcome to my Stage2 Project" # A little Introducting :)
print Introducting
How_many_times() #leads to the next function which prompts the user to beginn
