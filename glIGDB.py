import requests
import datetime
import config

def gbCheck(searchGame):
    # Make the API request
    url = f"https://api.igdb.com/v4/"

    gameEndpoint = f"games/"
    platformEndpoint = f"platforms/"
    genreEndpoint = f"genres/"
    gameTitle = ""
    gamePlatform = None
    gameGenre = ""
    gameReleaseYear = ""
    max_weight = 0


    headers = {
        "client-id": config.igdbClient_id,
        "Authorization": config.igbdAuth_token
    }

    searchParams = {"search": searchGame, "fields": "name,platforms,genres,remasters,remakes,first_release_date,release_dates.human"}
    idParams = {"fields": "name"}

    gameResponse = requests.get(url+gameEndpoint, headers=headers, params=searchParams)

    # Print the name and release date of the first game in the search results
    results = gameResponse.json()

    for gameResults in results:
        if gameResults['name'].lower() == searchGame.lower():
            gameTitle = gameResults['name']
            platforms = gameResults['platforms']
            genres = gameResults['genres']

            gameReleaseYear = datetime.datetime.fromtimestamp(gameResults["first_release_date"]).strftime("%d/%m/%Y")
            input_date = datetime.datetime.strptime(gameReleaseYear, "%d/%m/%Y")
            current_date = datetime.datetime.now()
            days_diff = (current_date - input_date).days

            for x in genres:
                genres_response = requests.get(url+genreEndpoint+str(x), headers=headers, params=idParams)
                genres_data = genres_response.json()
                for genre in genres_data:
                    if len(genres_data) > 1:
                        gameGenre += genre["name"] + ", "
                    else:
                        gameGenre = genre["name"]

            for x in platforms:
                platforms_response = requests.get(url+platformEndpoint+str(x), headers=headers, params=idParams)
                platforms_data = platforms_response.json()

                for platform in platforms_data:
                    platform_name = platform["name"]

                    # Check if platform release is within three months of game release
                    if days_diff <= 90:
                        if platform_name in config.weighted_platforms:
                            weight = config.weighted_platforms[platform_name]
                            if weight > max_weight:
                                max_weight = weight
                                gamePlatform = platform_name
                    # Check if game release is before console release
                    elif platform_name in config.weighted_platforms:
                        weight = config.weighted_platforms[platform_name]
                        if weight > max_weight:
                            max_weight = weight
                            gamePlatform = platform_name

        else:
            pass

        return gameTitle, gamePlatform, gameGenre, gameReleaseYear