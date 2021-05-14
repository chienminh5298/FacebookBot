from FacebookBot import FacebookBot
import pyfiglet


def mainMenu(bot):
    def showOptions():
        options = ['Save all photos']
        print('\n')
        for i in range(len(options)):
            print('[' + str(i+1) + '] ' + options[i])
        menu()

    def yesNoInput(user_input):
        while True:
            if user_input == "Yes":
                return True
            elif user_input == "No":
                return False
            else:
                print("Invalid input !!!")
                mainMenu()

    def menu():
        yourChoice = input("\nEnter your choice: ")
        while True:
            if yourChoice == '1':
                bot.saveAllPhotos()
                break
            else:
                print('Invalid input')
                yourChoice = input("Enter your choice: ")

    showOptions()
    
def main():
    print("\nDesigned by:")
    print(pyfiglet.figlet_format("Chien Chi Bun\n"))

    facebookBot = FacebookBot()

    # --- Menu ---
    mainMenu(facebookBot)


main()
