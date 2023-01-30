import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(config.sheetsJson, scope)
client = gspread.authorize(creds)
sheet = client.open(config.sheetName).sheet1

def gameCheck(gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameTime, gameFirstPlayed, gameCompletionDate, gameLastPlayed):
    gameLog = sheet.get_all_records()
    
    foundTitle = False
    index = 0
    glSheetOutput = ''
    
    for row in gameLog:
        index = index + 1
        if row['Title'] == gameTitle and row['Platform'] == gamePlatform and row['Initial Release Date'] == gameReleaseYear:
            foundTitle = True
            sheet.update_cell(index+1, 8, gameLastPlayed)
            glSheetOutput = 'exists'
            return glSheetOutput
    if not foundTitle:
        sheet.append_row([gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameTime, gameFirstPlayed, gameCompletionDate, gameLastPlayed],value_input_option='USER_ENTERED')
        glSheetOutput = 'added'
        return glSheetOutput
