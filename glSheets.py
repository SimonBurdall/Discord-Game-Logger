import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
import datetime

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(config.sheetsJson, scope)
client = gspread.authorize(creds)
sheet = client.open(config.sheetName).sheet1

def gameCheck(gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear, gameFirstPlayed):
    gameLog = sheet.get_all_records()
    
    foundTitle = False
    
    totalRows = sheet.row_count
    gameSinceRelease = f'=DATEDIF(F{totalRows+1},G{totalRows+1},"y")&" years, "&DATEDIF(F{totalRows+1},G{totalRows+1},"ym")&" months, and "&DATEDIF(F{totalRows+1},G{totalRows+1},"md")&" days"'
    
    for row in gameLog:
        if row['Title'] == gameTitle and row['First Release Date'] == gameReleaseYear:
            foundTitle = True
            print(f'{gameTitle} already exists.')
            break
    if not foundTitle:
        sheet.append_row([gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear, gameFirstPlayed, gameSinceRelease],value_input_option='USER_ENTERED')
        print(f'{gameTitle} added.')
