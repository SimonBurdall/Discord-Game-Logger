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
                gameDeveloper = gameInfo['results']['developers'][0]['name']
                gamePublisher = gameInfo['results']['publishers'][0]['name']
                gameGenre = gameInfo['results']['genres'][0]['name']
                gameReleaseYear = gameInfo['results']['original_release_date']
                date_str_new = gameReleaseYear.split("-")
                gameReleaseYear = date_str_new[2] + "/" + date_str_new[1] + "/" + date_str_new[0]

                return gameTitle, gameDeveloper, gamePublisher, gameGenre, gameReleaseYear
