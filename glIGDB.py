import requests
import datetime
import config

def gbCheck(searchGame):
    # Make the API request
    url = f"https://api.igdb.com/v4/"

    gameEndpoint = f"games/"
    platformEndpoint = f"platforms/"
    genreEndpoint = f"genres/"
    artworkEndpoint = f"artworks/"
    
    gameTitle = ""
    gamePlatform = None
    gameGenre = ""
    gameReleaseYear = ""
    gameArtwork = ""
    max_weight = 0
    glIGDBOutput = "N"

    headers = {
        "client-id": config.igdbClient_id,
        "Authorization": config.igbdAuth_token
    }

    searchParams = {"search": searchGame, "fields": "name,platforms,genres,remasters,remakes,first_release_date,release_dates.human,artworks"}
    idParams = {"fields": "name"}

    gameResponse = requests.get(url+gameEndpoint, headers=headers, params=searchParams)

    # Print the name and release date of the first game in the search results
    results = gameResponse.json()

    for gameResults in results:
        if gameResults['name'].lower() == searchGame.lower():
            gameTitle = gameResults['name']
            
            try:
                gameReleaseYear = datetime.datetime.fromtimestamp(gameResults["first_release_date"]).strftime("%d/%m/%Y")
                input_date = datetime.datetime.strptime(gameReleaseYear, "%d/%m/%Y")
                current_date = datetime.datetime.now()
                days_diff = (current_date - input_date).days
            except:
                gameReleaseYear = datetime.datetime.now()

            try:
                genres = gameResults['genres']
                if len(genres) > 1:
                    gameGenre = ""
                    for x in genres:
                        genres_response = requests.get(url + genreEndpoint + str(x), headers=headers, params=idParams)
                        genres_data = genres_response.json()
                        gameGenre += genres_data[0]['name'] + ", "
                    gameGenre = gameGenre[:-2]
                    print(gameGenre)
                else:
                    genres_response = requests.get(url + genreEndpoint + str(genres[0]), headers=headers, params=idParams)
                    genres_data = genres_response.json()
                    gameGenre = genres_data[0]['name']
            except:
                gameGenre = ""

            try:
                platforms = gameResults['platforms']
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
            except:
                gamePlatform = ""

            try:
                artworks = gameResults['artworks']
                for x in artworks:
                    artworks_response = requests.get(url + artworkEndpoint + str(x), headers=headers, params={"fields": "url"})
                    artworks_data = artworks_response.json()
                    for art in artworks_data:
                        gameArtwork = art["url"]
            except:
                gameArtwork = "media.discordapp.net/attachments/995592727368568894/1069720253300478084/SimonSponge_screenshot_of_the_most_generic_video_game_ever._d95b1eb4-5ca0-4264-a4f6-0e0fccd38a74.png"
        
        else:
            pass

        if gameTitle == None:
            glIGDBOutput = "N"
        else:
            glIGDBOutput = "Y"

    return gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameArtwork, glIGDBOutput
