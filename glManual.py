import glSheets, glGiantBomb
import datetime

date = datetime.datetime.now()
gameFirstPlayed = date.strftime("%d/%m/%Y")


gameTitle = input("Please enter a Game title: ")

gameTitle, gameDeveloper, gamePublisher, gameGenre, gameReleaseYear = glGiantBomb.gbCheck(gameTitle)
glSheets.gameCheck(gameTitle, gameDeveloper, gamePublisher, gameGenre, gameReleaseYear, gameFirstPlayed)