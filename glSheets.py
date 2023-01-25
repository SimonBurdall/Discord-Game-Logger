import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(config.sheetsJson, scope)
client = gspread.authorize(creds)
sheet = client.open(config.sheetName).sheet1

def gameCheck(gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear, gameFirstPlayed):
    gameLog = sheet.get_all_records()
    
    foundTitle = False

    for row in gameLog:
        if row['Title'] == gameTitle and row['First Release Date'] == gameReleaseYear:
            foundTitle = True
            print(f'{gameTitle} already exists.')
            break
    if not foundTitle:
        sheet.append_row([gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear, gameFirstPlayed])
        print(f'{gameTitle} added.')
