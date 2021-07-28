
Hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
print("welcome to the user")
name= input("what is your name?\n")
print("hello,",name,"time to play hangman")
print("waiting............")
print("start guessing ......")
var=("holiday")
choices=('')
while True:
	a=1
	time=7
	while time>0:
		b=0
		for i in var:
			if i in choices:
				print(i)
			else:
				print("_")
				b+=1
		if b==0:
			print("you won")
			print("congratulation")
			break
		choice=input("guess choice a character:\n")
		choices+=choice

		if choice in choices:
			print("this character is already use")
		if choice not in var:
			time-=1
			print(Hangman[-a])
			a+=1
			print("you have",time,"more guesses")
			if time==0:
				print("you are lose")
	
	print("do you want play: y/n ")
	again=input()
	if again=="y":
		print("thank you")
	else:
		print("good bye")
		break
	choices=("_")