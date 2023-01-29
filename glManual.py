import glSheets, glIGDB
import datetime

gameSearch = input("Please enter a Game title: ")

gameFirstPlayed = input ("Please enter date First played, format DD/MM/YYYY, if not today: ")

if not gameFirstPlayed:
    date = datetime.datetime.now()
    gameFirstPlayed = date.strftime("%d/%m/%Y")
else:
    pass

gameTime = ""
gameCompletionDate = ""
gameLastPlayed = ""

gameTitle, gamePlatform, gameGenre, gameReleaseYear = glIGDB.gbCheck(gameSearch)
glSheets.gameCheck(gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameTime, gameFirstPlayed, gameCompletionDate, gameLastPlayed)