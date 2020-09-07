from tkinter import *
from random import randint
import time
import tkinter.messagebox 

#Formats and sets the overarching game window
Game_Window = Tk()
Game_Window.title("Chris' Python Game-Pile")
HEIGHT = 500
WIDTH = 800
x = (Game_Window.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (Game_Window.winfo_screenheight() // 2) - (9*HEIGHT // 16)
Game_Window.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

class Players:
#initialises scores and names for the players involved in the game
	Player_1 = StringVar(value = "Player 1")
	Player_2 = StringVar(value = "Player 2")
	Player_3 = StringVar(value = "Player 3")
	#sets the remaining lives of each player to 100
	Player_1_mpscore = IntVar(value = 100)
	Player_2_mpscore = IntVar(value = 100)
	Player_3_mpscore = IntVar(value = 100)
	#sets the rounds survived highscores for multiplayer mode
	Player_1_mpHHscore = IntVar(value = 0)
	Player_2_mpHHscore = IntVar(value = 0)
	Player_3_mpHHscore = IntVar(value = 0)
	#sets the current scores for rounds survived in multiplayer mode
	Player_1_mpHscore = IntVar(value = 0)
	Player_2_mpHscore = IntVar(value = 0)
	Player_3_mpHscore = IntVar(value = 0)
	#sets the current score for rounds survived in singleplayer mode
	Player_1_spscore = IntVar(value = 0)
	#sets the rounds survived highscores for singleplayer mode
	Player_1_spHighscore = IntVar(value = 0)

class GameFunctions:
#set some required textvariables for multiple of the game features
	Countdown = IntVar(value = 3)
	targetNumber = IntVar(value = 100)
	Player1_guess = StringVar(value = "None")
	Player2_guess = StringVar(value = "None")
	Player3_guess = StringVar(value = "None")
	
class Windows:

	def MainMenu():
	#contains all the frames and widgets responsible for the main menu
		#begin by defining all of the necessary functions for the main menu
		def MainMenuClose():
			#this function closes all of the labels and frames from the main menu
			bg_frame.grid_forget()
			sb_frame.grid_forget()
			title_label.grid_forget()
			word_game_button.grid_forget()
			second_game_button.grid_forget()
			third_game_button.grid_forget()
			edit_players_button.grid_forget()
			scoreboard_label.grid_forget()
			p1_label.grid_forget()
			p1_mpscore_label.grid_forget()
			p1_spHighscore_label.grid_forget()
			p2_label.grid_forget()
			p2_mpscore_label.grid_forget()
			p3_label.grid_forget()
			p3_mpscore_label.grid_forget()

		def wg_open():
			#a shortcut function to close the main menu and open the word game menu
			MainMenuClose()
			Windows.wg_Menu()

		def SecondGameInstructions():
			#displays the pop-up note for the second game button
			tkinter.messagebox.showinfo("The Second Game", "Space here for a future second game")
		
		def ThirdGameInstructions():
			#displays the pop-up note for the third game button
			tkinter.messagebox.showinfo("The Third Game", "Space here for a future third game")

	#defines the necessary frames for the main menu

		#first of which is the background frame
		bg_frame = Frame(Game_Window, bg = "Dark Green", width = 800, height = 500)
		bg_frame.grid(rowspan = 10, columnspan = 3)

		#then we have the scoreboard frame
		sb_frame = Frame(Game_Window, bg = "#0055cc", width = 800, height = 150)
		sb_frame.grid(row = 8, rowspan = 2, columnspan = 3)

	#following this is the necessary labels and buttons for the main menu functionality

		#the title label
		title_label = Label(Game_Window, text = "Python Game-Pile", bg = "Dark Green", fg = "Black", bd = 1, font = ("Times New Roman", 75, "underline"))
		title_label.grid(row = 0, column = 1, sticky = S)

		#the word game button
		word_game_button = Button(Game_Window, text = "Word Game", bg = "Dark Green", font = ("Helvetica", 15), command = wg_open)
		word_game_button.grid(row = 2, column = 1)

		#the second game button
		second_game_button = Button(Game_Window, text = "Second Game", command = SecondGameInstructions, bg = "Dark Green", font = ("Helvetica", 15))
		second_game_button.grid(row = 3, column = 1)

		#the third game button
		third_game_button = Button(Game_Window, text = "Third Game", bg = "Dark Green", command = ThirdGameInstructions, font = ("Helvetica", 15))
		third_game_button.grid(row = 4, column = 1)

		#the edit players button
		edit_players_button = Button(Game_Window, text = "Edit Players", bg = "Dark Green", font = ("Helvetica", 15), command = Windows.editPlayerWindow)
		edit_players_button.grid(row = 5, column = 1)

		#the scoreboard labels
		scoreboard_label = Label(Game_Window, text = "Scoreboard:", bg = "#0055cc", font = ("Helvetica", 25, "underline"))
		scoreboard_label.grid(row = 8, column = 1, sticky = N)

		#player 1 name label
		p1_label = Label(Game_Window, textvariable = Players.Player_1, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p1_label.grid(row = 8, column = 1, sticky = S)

		#player 1 multiplayer highscore label
		p1_mpscore_label = Label(Game_Window, textvariable = Players.Player_1_mpHHscore, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p1_mpscore_label.grid(row = 9, column = 1, sticky = N)

		#player 1 singleplayer highscore label
		p1_spHighscore_label = Label(Game_Window, textvariable = Players.Player_1_spHighscore, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p1_spHighscore_label.grid(row = 9, column = 1, sticky = S)

		#player 2 name label
		p2_label = Label(Game_Window, textvariable = Players.Player_2, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p2_label.grid(row = 8, column = 1, sticky = SW)

		#player 2 multiplayer highscore label
		p2_mpscore_label = Label(Game_Window, textvariable = Players.Player_2_mpHHscore, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p2_mpscore_label.grid(row = 9, column = 1, sticky = NW)

		#player 3 name label
		p3_label = Label(Game_Window, textvariable = Players.Player_3, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p3_label.grid(row = 8, column = 1, sticky = SE)

		#player 3 multiplayer highscore label
		p3_mpscore_label = Label(Game_Window, textvariable = Players.Player_3_mpHHscore, bg = "#0055cc", font = ("Helvetica", 15, "bold"))
		p3_mpscore_label.grid(row = 9, column = 1, sticky = NE)
		
	def editPlayerWindow():
		#creates the window used to add/remove players
		optionsWindow = Tk()
		optionsWindow.title("Edit Players")
		WIDTH = 120
		HEIGHT = 110
		x = (Game_Window.winfo_screenwidth() // 2) - (WIDTH // 2)
		y = (Game_Window.winfo_screenheight() // 2) - (2*HEIGHT // 2)
		optionsWindow.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

		#adds a user input line
		playerEntry = Entry(optionsWindow)
		playerEntry.grid(row = 1)

		def addPlayer():
			#defines the function used to take the input entry and define it as the first/second/third player
			if Players.Player_1.get() == "Player 1":
				Players.Player_1.set(playerEntry.get())
			elif Players.Player_2.get() == "Player 2":
				Players.Player_2.set(playerEntry.get())
			elif Players.Player_3.get() == "Player 3":
				Players.Player_3.set(playerEntry.get())

		def removePlayer():
			#defines the function used to take the input entry and remove this player from the game
			if Players.Player_1.get() == playerEntry.get():
				Players.Player_1.set("Player 1")
			if Players.Player_2.get() == playerEntry.get():
				Players.Player_2.set("Player 2")
			if Players.Player_3.get() == playerEntry.get():
				Players.Player_3.set("Player 3")
			if Players.Player_1.get() == "Player 1" and Players.Player_2.get() != "Player 2":
				Players.Player_1.set(Players.Player_2.get())
				Players.Player_2.set("Player 2")
			if Players.Player_2.get() == "Player 2" and Players.Player_3.get() != "Player 3":
				Players.Player_2.set(Players.Player_3.get())
				Players.Player_3.set("Player 3")
			
		#adds the relevant buttons for adding players, removing players and closing the options window
		Adder = Button(optionsWindow, text = "Add Player", command = addPlayer).grid(row = 2)
		Remover = Button(optionsWindow, text = "Remove Player", command = removePlayer).grid(row = 3)
		Canceller = Button(optionsWindow, text = "Cancel", command = optionsWindow.destroy).grid(row = 4)

	def wg_Menu():
	#contains all the frames and widgets responsible for the word game menu
		#begins by defining the necessary functions for the word game menu
		def wgMenuClose():
			#this function closes all of the frames and labels associated with the word game menu
			bg_frame.grid_forget()
			title_label.grid_forget()
			instructions_button.grid_forget()
			singleplayer_button.grid_forget()
			multiplayer_button.grid_forget()
			edit_players_button.grid_forget()
			return_button.grid_forget()
		
		def MainMenuReturn():
			#this function closes the word game window and returns the user to the main menu
			wgMenuClose()
			Windows.MainMenu()

		def SinglePlayGame():
			#this function closes the word game menu and opens a singleplayer game
			wgMenuClose()
			Windows.wg_single()

		def MultiPlayGame():
			#this function closes the word game menu and opens a multiplayer game
			wgMenuClose()
			Windows.wg_multi()

		def Instructions():
			#this brings up a messagebox showing the instructions for the singleplayer and multiplayer word game
			tkinter.messagebox.showinfo("Singleplayer Instructions", "Singleplayer: \nGuess as many words as possible with scores which add up to the target number shown, where a = 1, b = 2 etc... Survive as long as you can: you start with 100 lives and lose one for each point value away from the target score.\n\nMultiplayer: \nRemaining lives are no longer visible. Play continues until all players have 0 lives; can you survive longer than the rest?")
			
	#defines all the necessary frames for the word game menu

		#first of which is the background frame
		bg_frame = Frame(Game_Window, bg = "Dark Green", width = 800, height = 500)
		bg_frame.grid(rowspan = 10, columnspan = 3)

	#following this is the necessary labels and buttons for the main menu functionality

		#the title label
		title_label = Label(Game_Window, text = "Word Game", bg = "Dark Green", font = ("Helvetica", 75, "underline"))
		title_label.grid(row = 0, column = 1, sticky = S)

		#the instructions button
		instructions_button = Button(Game_Window, text = "Instructions", bg = "Dark Green", font = ("Helvetica", 15), command = Instructions)
		instructions_button.grid(row = 2, column = 1)

		#the singleplayer button
		singleplayer_button = Button(Game_Window, text = "Singleplayer", bg = "Dark Green", font = ("Helvetica", 15), command = SinglePlayGame)
		singleplayer_button.grid(row = 3, column = 1)

		#the multiplayer button
		multiplayer_button = Button(Game_Window, text = "Multiplayer", bg = "Dark Green", font = ("Helvetica", 15), command = MultiPlayGame)
		multiplayer_button.grid(row = 4, column = 1)

		#the edit players button
		edit_players_button = Button(Game_Window, text = "Edit Players", bg = "Dark Green", font = ("Helvetica", 15), command = Windows.editPlayerWindow)
		edit_players_button.grid(row = 5, column = 1)

		#the return to main menu button
		return_button = Button(Game_Window, text = "Return to Main Menu", bg = "Dark Green", font = ("Helvetica", 15), command = MainMenuReturn)
		return_button.grid(row = 5, column = 1)


	def wg_single():
	#contains all the frames and widgets responsible for the word game singleplayer game
		#begins by defining the necessary functions for the singleplayer word game
		def wg_singleClose():
			#this function closes all of the frames and labels associated with the word game menu
			bg_frame.grid_forget()
			title_label.grid_forget()
			return_button.grid_forget()
			count_label.grid_forget()
			count_start_button.grid_forget()
			countdown_reset()

		def MainMenuReturn():
			#this function closes the word game window and returns the user to the main menu
			wg_singleClose()
			Windows.MainMenu()

		def mpScoreReset():
			#this function resets the number of lives remaining
				Players.Player_1_mpscore.set(100)

		def spScoreReset():
			#this function sets the singleplayer current score back to 0
				Players.Player_1_spscore.set(0)

		def startTimer():
			#this function reduces the value of the countdown timer and updates the screen to show it
			t = GameFunctions.Countdown.get()
			while t >= 0:
				Game_Window.after(1000, GameFunctions.Countdown.set(t))
				Game_Window.update()
				t -= 1

			spScoreReset()
			beginGame()

		def countdown_reset():
			#this function resets the countdown clock integer variable to 3 seconds
			GameFunctions.Countdown.set(3)

		def beginGame():
			#start by defining the functions needed to play the singleplayer word game
			def wg_singleCloseGame():
			#this function closes all the frames and labels associated with the game
				bg_frame.grid_forget()
				target_label.grid_forget()
				return_button_game.grid_forget()
				word_entry.grid_forget()
				target_explain_label.grid_forget()
				lives_explaining_label.grid_forget()
				lives_remaining_label.grid_forget()
				countdown_reset()

			def MMRet_game():
			#this function closes the word game window from within the game, and returns the user to the main menu
				wg_singleCloseGame()
				mpScoreReset()
				Windows.MainMenu()

			def CalculateScore():
				#starts off by clearing whats on the screen
				target_label.grid_forget()
				return_button_game.grid_forget()
				word_entry.grid_forget()
				target_explain_label.grid_forget()
				lives_explaining_label.grid_forget()
				lives_remaining_label.grid_forget()

				#then calculates the score achieved
				word = GameFunctions.Player1_guess.get()
				Letters = list(word.lower())
				total_score = 0
				for L in Letters:
					letter_score = ord(L) - ord("a") + 1
					total_score = total_score + letter_score

				Players.Player_1_mpscore.set(Players.Player_1_mpscore.get() - (abs(total_score - GameFunctions.targetNumber.get())))
				if Players.Player_1_mpscore.get() <= 0:
					if Players.Player_1_spscore.get() > Players.Player_1_spHighscore.get():
						Players.Player_1_spHighscore.set(Players.Player_1_spscore.get())
					MMRet_game()
				else:
					Players.Player_1_spscore.set(Players.Player_1_spscore.get() + 1)
					beginGame()

			def submitted(event):
				#this is what happens when the return key is pressed
				GameFunctions.Player1_guess.set(word_entry.get())
				CalculateScore()

			#this is the function that once again clears the screen, ready for the game to be played
			title_label.grid_forget()
			count_label.grid_forget()
			count_start_button.grid_forget()
			return_button.grid_forget()

			#next, the target number is randomised
			GameFunctions.targetNumber.set(randint(25, 150))

			#this random number is then displayed on the screen with an explanation label
			target_explain_label = Label(Game_Window, text = "Your target number is:", bg = "Dark Green", font = ("Helvetica", 50))
			target_explain_label.grid(row = 1, column = 1)
			target_label = Label(Game_Window, textvariable = GameFunctions.targetNumber, bg = "Dark Green", font = ("Helvetica", 75, "bold"))
			target_label.grid(row = 2, column = 1)

			#the input window is added to the screen
			word_entry = Entry(Game_Window)
			word_entry.grid(row = 3, column = 0, columnspan = 3, sticky = S)
			Game_Window.bind('<Return>', submitted)

			#the remaining lives label is added to the screen
			lives_explaining_label = Label(Game_Window, text = "Lives remaining: ", bg = "Dark Green", font = ("Helvetica", 20))
			lives_explaining_label.grid(row = 6, column = 1, sticky = S)
			lives_remaining_label = Label(Game_Window, textvariable = Players.Player_1_mpscore, bg = "Dark Green", font = ("Helvetica", 20))
			lives_remaining_label.grid(row = 7, column = 1, sticky = N)

			#the return button is added to the screen
			return_button_game = Button(Game_Window, text = "Return to Main Menu", bg = "Dark Green", font = ("Helvetica", 10), command = MMRet_game)
			return_button_game.grid(row = 9, column = 1, sticky = S)

			
	#begin by defining all the necessary frames for the word game menu

		#first of which is the background frame
		bg_frame = Frame(Game_Window, bg = "Dark Green", width = 800, height = 500)
		bg_frame.grid(rowspan = 10, columnspan = 3)

	#following this is the necessary labels and buttons for the main menu functionality

		#the title label
		title_label = Label(Game_Window, text = "Singleplayer", bg = "Dark Green", font = ("Helvetica", 50, "underline"))
		title_label.grid(row = 0, column = 1)

		#the countdown timer
		count_label = Label(Game_Window, textvariable = GameFunctions.Countdown, bg = "Dark Green", font = ("Helvetica", 25))
		count_label.grid(row = 4, column = 1)

		#the countdown starter button
		count_start_button = Button(Game_Window, text = "Start!", bg = "Dark Green", font = ("Helvetica", 20), command = startTimer)
		count_start_button.grid(row = 6, column = 1)

		#the return to main menu button
		return_button = Button(Game_Window, text = "Return to Main Menu", bg = "Dark Green", font = ("Helvetica", 10), command = MainMenuReturn)
		return_button.grid(row = 9, column = 1, sticky = S)

	def wg_multi():
	#contains all the frames and widgets responsible for the word game singleplayer game
		#begins by defining the necessary functions for the multiplayer word game
		def wg_multiClose():
			#this function closes all of the frames and labels associated with the word game menu
			bg_frame.grid_forget()
			title_label.grid_forget()
			return_button.grid_forget()
			count_label.grid_forget()
			count_start_button.grid_forget()
			countdown_reset()

		def MainMenuReturn():
			#this function closes the word game window and returns the user to the main menu
			wg_multiClose()
			Windows.MainMenu()

		def mpScoreReset():
			#sets the remaining lives of all of the players back to 100
				Players.Player_1_mpscore.set(100)
				Players.Player_2_mpscore.set(100)
				Players.Player_3_mpscore.set(100)

		def mpHScoreReset():
			#sets the survived rounds scores of all players back to 0
				Players.Player_1_mpHscore.set(0)
				Players.Player_2_mpHscore.set(0)
				Players.Player_3_mpHscore.set(0)

		def startTimer():
			#this function reduces the value of the countdown timer and updates the screen to show it
			t = GameFunctions.Countdown.get()
			while t >= 0:
				Game_Window.after(1000, GameFunctions.Countdown.set(t))
				Game_Window.update()
				t -= 1
			mpHScoreReset()
			beginGame()


		def countdown_reset():
			#resets the countdown timer to 3 seconds
			GameFunctions.Countdown.set(3)

		def beginGame():
			#defines the necessary functions to run the multiplayer word game
			def wg_multiCloseGame():
			#this function closes all the frames and labels associated with the game
				bg_frame.grid_forget()
				target_label.grid_forget()
				return_button_game.grid_forget()
				word_entry1.grid_forget()
				word_entry2.grid_forget()
				word_entry3.grid_forget()
				p1_label.grid_forget()
				p2_label.grid_forget()
				p3_label.grid_forget()
				target_explain_label.grid_forget()
											
				countdown_reset()

			def MMRet_game():
			#this function closes the word game window from within the game, and returns the user to the main menu
				wg_multiCloseGame()
				mpScoreReset()
				Windows.MainMenu()

			
			def CalculateScore1():
				#calculates the score achieved for player 1
				word1 = GameFunctions.Player1_guess.get()
				Letters1 = list(word1.lower())
				total_score_1 = 0
				for L in Letters1:
					letter_score_1 = ord(L) - ord("a") + 1
					total_score_1 = total_score_1 + letter_score_1
				Players.Player_1_mpscore.set(Players.Player_1_mpscore.get() - (abs(total_score_1 - GameFunctions.targetNumber.get())))
				if Players.Player_1_mpscore.get() > 0:
					Players.Player_1_mpHscore.set(Players.Player_1_mpHscore.get() + 1)
				if Players.Player_1_mpscore.get() <= 0:
					Players.Player_1_mpscore.set(0)
					
			def CalculateScore2():
				#calculation for the score achieved by player 2
				word2 = GameFunctions.Player2_guess.get()
				Letters2 = list(word2.lower())
				total_score_2 = 0
				for L in Letters2:
					letter_score_2 = ord(L) - ord("a") + 1
					total_score_2 = total_score_2 + letter_score_2
				Players.Player_2_mpscore.set(Players.Player_2_mpscore.get() - (abs(total_score_2 - GameFunctions.targetNumber.get())))
				if Players.Player_2_mpscore.get() > 0:
					Players.Player_2_mpHscore.set(Players.Player_2_mpHscore.get() + 1)
				if Players.Player_2_mpscore.get() <= 0:
					Players.Player_2_mpscore.set(0)
					
			def CalculateScore3():
				#calculation for the score achieved by player 3
				word3 = GameFunctions.Player3_guess.get()
				Letters3 = list(word3.lower())
				total_score_3 = 0
				for L in Letters3:
					letter_score_3 = ord(L) - ord("a") + 1
					total_score_3 = total_score_3 + letter_score_3
				Players.Player_3_mpscore.set(Players.Player_3_mpscore.get() - (abs(total_score_3 - GameFunctions.targetNumber.get())))
				if Players.Player_3_mpscore.get() > 0:
					Players.Player_3_mpHscore.set(Players.Player_3_mpHscore.get() + 1)
				if Players.Player_3_mpscore.get() <= 0:
					Players.Player_3_mpscore.set(0)

			def CalculateScores():
				#shortcut function to calculate the scores for all of the players in multiplayer mode
				CalculateScore1()
				CalculateScore2()
				CalculateScore3()
				#determines whether or not to exit to the main menu for gameover
				if Players.Player_1_mpscore.get() > 0 or Players.Player_2_mpscore.get() > 0 or Players.Player_3_mpscore.get() > 0: 
					target_explain_label.grid_forget()
					target_label.grid_forget()
					word_entry1.grid_forget()
					word_entry2.grid_forget()
					word_entry3.grid_forget()
					p1_label.grid_forget()
					p2_label.grid_forget()
					p3_label.grid_forget()
					return_button_game.grid_forget()

					beginGame()
				else:
					title_label.grid_forget()
					count_label.grid_forget()
					count_start_button.grid_forget()
					return_button.grid_forget()
					if Players.Player_1_mpHscore.get() > Players.Player_1_mpHHscore.get():
						Players.Player_1_mpHHscore.set(Players.Player_1_mpHscore.get())
					if Players.Player_2_mpHscore.get() > Players.Player_2_mpHHscore.get():
						Players.Player_2_mpHHscore.set(Players.Player_2_mpHscore.get())
					if Players.Player_3_mpHscore.get() > Players.Player_3_mpHHscore.get():
						Players.Player_3_mpHHscore.set(Players.Player_3_mpHscore.get())
					MMRet_game()

				
			def submitted(event):
				#defines what happens when the return button is pressed
				GameFunctions.Player1_guess.set(word_entry1.get())
				GameFunctions.Player2_guess.set(word_entry2.get())
				GameFunctions.Player3_guess.set(word_entry3.get())	
				CalculateScores()


			
			#this is the function that once again clears the screen, ready for the game to be played
			title_label.grid_forget()
			count_label.grid_forget()
			count_start_button.grid_forget()
			return_button.grid_forget()

			#next, the target number is randomised
			GameFunctions.targetNumber.set(randint(25, 150))

			#this random number is then displayed on the screen with an explanation label
			target_explain_label = Label(Game_Window, text = "Your target number is:", bg = "Dark Green", font = ("Helvetica", 50))
			target_explain_label.grid(row = 1, column = 1)
			target_label = Label(Game_Window, textvariable = GameFunctions.targetNumber, bg = "Dark Green", font = ("Helvetica", 75, "bold"))
			target_label.grid(row = 2, column = 1)

			#the input window is added to the screen
			word_entry1 = Entry(Game_Window)
			word_entry1.grid(row = 5, column = 1, sticky = W)

			word_entry2 = Entry(Game_Window)
			word_entry2.grid(row = 5, column = 1)
			
			word_entry3 = Entry(Game_Window)
			word_entry3.grid(row = 5, column = 1, sticky = E)

			#binds the return key to the submitted function
			Game_Window.bind('<Return>', submitted)
			
			#the return button is added to the screen
			return_button_game = Button(Game_Window, text = "Return to Main Menu", bg = "Dark Green", font = ("Helvetica", 10), command = MMRet_game)
			return_button_game.grid(row = 9, column = 1, sticky = S)

			#shows the player names for clarification in the multiplayer game
			p1_label = Label(Game_Window, textvariable = Players.Player_1, bg = "Dark Green", font = ("Helvetica", 25))
			p1_label.grid(row = 4, column = 1, sticky = W)
			p2_label = Label(Game_Window, textvariable = Players.Player_2, bg = "Dark Green", font = ("Helvetica", 25))
			p2_label.grid(row = 4, column = 1)
			p3_label = Label(Game_Window, textvariable = Players.Player_3, bg = "Dark Green", font = ("Helvetica", 25))
			p3_label.grid(row = 4, column = 1, sticky = E)

						
	#begin by defining all the necessary frames for the word game menu

		#first of which is the background frame
		bg_frame = Frame(Game_Window, bg = "Dark Green", width = 800, height = 500)
		bg_frame.grid(rowspan = 10, columnspan = 3)

	#following this is the necessary labels and buttons for the main menu functionality

		#the title label
		title_label = Label(Game_Window, text = "Multiplayer", bg = "Dark Green", font = ("Helvetica", 50, "underline"))
		title_label.grid(row = 0, column = 1)

		#the countdown timer
		count_label = Label(Game_Window, textvariable = GameFunctions.Countdown, bg = "Dark Green", font = ("Helvetica", 25))
		count_label.grid(row = 4, column = 1)

		#the countdown starter button
		count_start_button = Button(Game_Window, text = "Start!", bg = "Dark Green", font = ("Helvetica", 20), command = startTimer)
		count_start_button.grid(row = 6, column = 1)

		#the return to main menu button
		return_button = Button(Game_Window, text = "Return to Main Menu", bg = "Dark Green", font = ("Helvetica", 10), command = MainMenuReturn)
		return_button.grid(row = 9, column = 1, sticky = S)

#begins the game by opening the main menu
Windows.MainMenu()


Game_Window.mainloop()




		