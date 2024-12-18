import pyttsx3

bot = pyttsx3.init()

bot.say("What would you like the pronunciation of?")
print("\nWhat would you like the pronunciation of?\n")
bot.runAndWait()

user_input = input("Enter: ")
bot.say("It is pronounced" + " " + user_input)

bot.runAndWait()
