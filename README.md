# Game-Logger
Unlock a whole new level of logging with this Discord bot! Keep track of all your gaming activity in a sleek spreadsheet.

## Discord Setup

### Discord Setup | Installation and Bot Configuration

1. Install the Discord.py library by running the following command in the command prompt or terminal:
        pip install discord.py

2. Create a Discord Bot Account on the Discord Developer Portal by signing in with your Discord account. Go to the "Applications" section and click on the "New Application." Give your bot a name and click "Create."

3. In the "Bot" section, click "Add Bot" to generate a Discord token. Copy the token and paste it in the config.py file next to the discord_key variable.
    
        discord_Key = "[Discord Token]"

### Discord Setup | Application Setup and locating variables

1. Create a new Discord server just for you and the bot to make it easier to interact with the bot during logging.

2. Invite the bot to your server by clicking on the server settings, then the "Members" tab, and then the "Invite a member" button. Choose "Invite a bot," type the bot's name, select the appropriate permissions, and then click "Invite."

3. To locate your Discord user ID, go to the Discord settings and click on the "Appearance" section. Turn on the "Developer Mode" option. Right-click on your profile picture in a server and click "Copy ID." Your Discord user ID will be copied to your clipboard. Paste this into the config.py file next to the discordUser_id variable.

        discordUser_id = [Discord User ID]

## Google Sheets Setup

### Google Sheets Template

Access a template of the Game-Log sheets at the following link and make a copy of it:

    https://docs.google.com/spreadsheets/d/1CPl108qohfMr5sUOJ6k_jnXtwMF4X7js1d38jUbCv0c/edit?usp=sharing

### Google Sheets Setup

1. Go to the Google API Console via the following link;
        
        https://console.developers.google.com/

2. Create a new project or select an existing project.

3. Enable the Google Sheets API by clicking on the "Enable APIs and Services" button.

4. In the API Library, search for "Google Sheets API" and select it.

5. Click the "Enable" button.

6. In the API Console, go to the "Credentials" tab.

7. Click the "Create credentials" button and select "Service account".

8. Fill in the required information and click the "Create" button.

9. Download the private key in JSON format and save it to a secure location.

10. Install the Google API Client Library for Python by running the following command in your terminal or command prompt:

        pip install --upgrade google-api-python-client

11. Add the JSON file to the root of the bot´s directory, and add the name of the JSON file into the 'Config.py' as a string;
        
        sheetsJson = "[File Name].json"
                
12. Add the name of your Google Sheets document to the 'Config.py' as a string;

        sheetName = "[Google Sheets name]"

## Internet Gaming Database Setup

1. Generate an API key by following the "Get Started" guide at the following link:

        https://www.igdb.com/api
        
2. Once you have generated the API key, you will receive a Client ID and Access Token. Add both to the config.py file, making sure "Bearer" is present in the string with a capital "B."

        igdbClient_id = "[Client ID]"
        igbdAuth_token = "Bearer [Access Token]"
        
## Toggle Setup

Currently not implemented, will add at a later date.

## Game Platform Weighting


# Discord Bot commands

Use the following commands within the server or via direct message (DM).

| Command  | Description | Argument  | Example |
| ------------- | ------------- |------------- | ------------- |
| /log  | Manually add a game to the log. The game will either be added to the log if it's not already in it, or its entry will be updated if it exists. | "[game title]"  | /log "Halo Infinite"  |
