# Kurt Zikaras
# Adenture Game
# Finished February 2017



# This is an adventure game in which your choices determine whether you win or lose
# It is a fun exercise in if/else statements and loops in Python



#this is the main module
def main():
	playAgain = "yes"
	while playAgain == "yes":
		playerScore = int(0)
		print("In this adventure game you make decisions which affect") #  Level One
		print("the progression of the game. But be careful! a wrong")
		print("decision can mean your death!")
		print("")
		print("You awake to news that your sister has been captured")
		print("and taken to an unknown location. Of course you need to")
		print("save your sister! You set out into the woods. While")
		print("wandering in the woods you come across a goblin!")
		print("")
		choiceLevelOne = input("Do you run or do you fight? (type run or fight) ")
		if choiceLevelOne == "fight":
			print("You were not strong enough. Your bravery will be remembered")
			playAgain = input("Play again? (enter yes to play again or no to quit)")
			print("")
		else:
			playerScore = playerScore + int(1) #  Level Two
			print("")
			print("Your score is:")
			print(playerScore)
			print("")
			print("You successfully snuck past the goblin! You learned much about")
			print("the goblin's skills by observing him. Maybe next time you can fight.")
			print("You continue your journey when suddenly you hear a howl in the")
			print("distance. It's a mutant wolf! You look around for something to fight")
			print("with and you notice a sharp stick on the ground. what do you do?")
			print("")
			choiceLevelTwo = input("(Type pickup or leave alone) ")
			if choiceLevelTwo == "leave alone":
				print("The wolf bested you. You should have defended yourself")
				playAgain = input("Play again? (enter yes to play again or no to quit) ")
				print("")
				
			else:
				playerScore = playerScore + int(1)  # Level Three
				print("")
				print("Your score is:")
				print(playerScore)
				print("")
				print("As the wolf made his attack you just barely dodged his bite.")
				print("You manage to stab the wolf in the neck with the sharp stick")
				print("You finally make your way through the end of the woods when")
				print("you reach a clearing and find an open field. You are unsure")
				print("whether you should run or sneak through the field. What do you")
				print("decide?")
				print("")
				choiceLevelThree = input("Enter run or sneak ")
				if choiceLevelThree == "run":
					print("While running across the field, another goblin notices")
					print("you. He charges towards you and initiates an attack")
					print("You are caught off guard and are killed by the goblin")
					playAgain = input("Play again? (enter yes to play again or no to quit) ")
					print("")
				else:
					playerScore = playerScore + int(1)  #Level Four
					print("")
					print("Your score is:")
					print(playerScore)
					print("")
					print("While sneaking across the field you spot a goblin in the distance.")
					print("You are able to sneak up on him and take him out silently")
					print("You continue through the field, silently making your way")
					print("to the dark castle where you suspect your sister is being held.")
					print("You stumble upon a pack of wolves who instantly notice you")
					print("What do you do?")
					print("")
					choiceLevelFour = input("Enter Run or Fight ")
					if choiceLevelFour == "fight":
						print("You made a foolish choice. You were overwhelmed by the")
						print("wolves.")
						playAgain = input("Play again? (enter yes to play again or no to quit) ")
						print("")
					else:
						playerScore = playerScore + int(1)   # Level Five
					
						print("")
						print("Your score is:", playerScore)
						print("You run as fast as you can and just narrowly escape the wolves")
						print("You finally are clear of danger, and can just make out the castle")
						print("ahead. As you approach an eerie feeling comes over you. You finally")
						print("reach the castle gates and they open to meet you. You step inside")
						print("to find an ungodly creature. It's the final boss battle!")
						print("The boss is a giant troll with more power than any foe you have")
						print("encountered so far. He lunges at you, you have but split seconds")
						print("to defend yourself")
						print("Do you fight the troll with the sharp stick you aquired? Or do you")
						print("attempt to dodge the attack? ")
						choiceBossOne = input("Enter Fight or Dodge ")
						if choiceBossOne == "Fight":
							print("The boss ran right through you. You are dead.")
							playAgain = input("Play again? (enter yes to play again or no to quit) ")
							print("")
						else:
							playerScore = playerScore + int(1)   # Level Six
							print("Your score is", playerScore)
							print("You successfully dodged the attack. The troll is now exposed")
							print("with it's back to you.")
							print("Now is your chance to finish him off!")
							print("What do you choose to do next?")
							print("Will you stab the giant troll in the back? or will you run away?")
							choiceBossTwo = input("Enter 'stab' or 'run' ")
							if choiceBossTwo == 'run':
								print("As you were escaping, one of the boss' minions catches you off")
								print("guard. You are killed in battle")
								playAgain = input("Play again? (enter yes to play again or no to quit) ")
							else:
								playerScore = playerScore + int(1)   # Level Seven
								print("You deliver a deadly blow to the troll's back and it begins to")
								print("bleed out. You run into the castle and free your sister.")
								print("Congratulations! You won the game!")
								print("Your score was", playerScore)
								playAgain = input("Play again? (enter yes to play again or no to quit) ")
		
					
					
	

	
main()
