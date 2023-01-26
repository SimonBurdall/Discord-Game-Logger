import glSheets, glGiantBomb
import datetime



gameTitle = input("Please enter a Game title: ")

gameFirstPlayed = input ("Please enter date First played, format DD/MM/YYYY, if not today: ")

if not gameFirstPlayed:
    date = datetime.datetime.now()
    gameFirstPlayed = date.strftime("%d/%m/%Y")
else:
    pass

gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear = glGiantBomb.gbCheck(gameTitle)
glSheets.gameCheck(gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear, gameFirstPlayed)