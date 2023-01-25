import requests
import config

api_key = config.giantBombKey

def gbCheck(gameTitle):
    gameTitle = gameTitle.replace(" ", "-")

    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'newcoder'
    }

    payloadSearch = {
        'api_key': api_key,
        'format': 'json',
        'query': gameTitle,
        'limit': '1'
    }

    urlSearch = 'https://www.giantbomb.com/api/search'
    urlGame = 'https://www.giantbomb.com/api/game/'
    response = requests.get(urlSearch, headers=headers, params=payloadSearch)

    if response.status_code == 200:
        results = response.json()
        for result in results['results']:
            gameID = result['guid']
            gameTitle = result['name']

            payloadGame = {
                'api_key': api_key,
                'format': 'json',
                'limit': '1'
            }

            responseGame = requests.get(urlGame + gameID, headers=headers, params=payloadGame)

            if responseGame.status_code == 200:
                gameInfo = responseGame.json()
                gameDeveloper = gameInfo['results']['developers']
                gamePublisher = gameInfo['results']['publishers']
                gameGenre = gameInfo['results']['genres']
                gamePlatform = gameInfo['results']['platforms']
                gameReleaseYear = gameInfo['results']['original_release_date']
                date_str_new = gameReleaseYear.split("-")
                gameReleaseYear = date_str_new[2] + "/" + date_str_new[1] + "/" + date_str_new[0]

                # If multiple developers or publishers exist
                if len(gameDeveloper) > 0:
                    gameDeveloper = [dev['name'] for dev in gameDeveloper]
                    gameDeveloper = ', '.join(gameDeveloper)
                else:
                    gameDeveloper = ''
                    
                if len(gamePublisher) > 0:
                    gamePublisher = [pub['name'] for pub in gamePublisher]
                    gamePublisher = ', '.join(gamePublisher)
                else:
                    gamePublisher = ''
                    
                if len(gameGenre) > 0:
                    gameGenre = [gen['name'] for gen in gameGenre]
                    gameGenre = ', '.join(gameGenre)
                else:
                    gameGenre = ''

                if len(gamePlatform) == 1:
                    gamePlatform = gamePlatform[0]['name']
                else:
                    gamePlatform = ''

                return gameTitle, gameDeveloper, gamePublisher, gameGenre, gamePlatform, gameReleaseYear