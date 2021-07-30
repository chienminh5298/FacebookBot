from FacebookBot import FacebookBot
import pyfiglet


def menuOptions(bot):
    options = ['Save all photos', 'Spam bot','Photo interacted analysis']
    print('\n')
    for i in range(len(options)):
        print('[' + str(i+1) + '] ' + options[i])

    yourChoice = input("\nEnter your choice: ")
    while True:
        if yourChoice == '1':
            bot.saveAllPhotos()
            break
        elif yourChoice == '2':
            bot.spamBot()
            break
        elif yourChoice == '3':
            bot.photoAnalyze()
            break
        else:
            print('Invalid input')
            yourChoice = input("\nEnter your choice: ")


def isExit():
    while True:
        wannaTry = input("\nWanna try another one(y/n) ?: ")
        if wannaTry == 'y' or wannaTry == 'Y' or wannaTry == 'Yes' or wannaTry == 'yes':
            return True
        elif wannaTry == 'n' or wannaTry == 'N' or wannaTry == 'No' or wannaTry == 'no':
            return False

def main():
    print("\nDesigned by:")
    print(pyfiglet.figlet_format("Chien Chi Bun\n"))
    facebookBot = FacebookBot()

    while True:
        menuOptions(facebookBot)
        quit = isExit()
        if quit == False:
            break
    
    facebookBot.quit()

main()
