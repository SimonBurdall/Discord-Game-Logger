# Game-Logger
Unlock a whole new level of logging with this Discord bot! Keep track of all your gaming activity in a sleek spreadsheet.

## Discord Setup

### Discord Setup | Installation and Bot Configuration

1. First install Discord.py library by entering the following command in the command prompt or terminal.

        pip install discord.py

2. Next, create a Discord Bot Account by navigating to the Discord Developer Portal and sign in with your Discord account. Then select "Applications" section and then click on the "New Application" button. Give a name to your bot and click on the "Create" button.

3. Once created go to the "Bot" section and click on the "Add Bot" button. This will the generate a Discord token, copy this token and added it to the 'config.py' file next to the discord_key variable.
    
        discord_Key = "[Discord Token]"

### Discord Setup | Application Setup and locating variables

1. Then create a new Discord Server just for you and the bot. This will make it easier to interact with the Bot when logging games. 

2. Invite the bot to your newly created server by clicking on the server settings, then on the "Members" tab.

3. Click the "Invite a member" button and then click "Invite a bot."

4. Type the Bot's name, select the appropriate permissions, and then click "Invite."

5. Finally, you will need to locate your Discord user ID, this is different to your Discord username. Navigate to the Discord settings and click on the "Appearance" section. Turn on the "Developer Mode" option. Right-click on your profile picture in a server and click on "Copy ID." Your Discord user ID will be copied to your clipboard, then paste this into the 'config.py' file next to the discordUser_id variable.

        discordUser_id = [Discord User ID]

## Google Sheets Setup

You can find a template of the gameLog sheets at the link below, feel free to make a copy of the sheet.

    https://docs.google.com/spreadsheets/d/1CPl108qohfMr5sUOJ6k_jnXtwMF4X7js1d38jUbCv0c/edit?usp=sharing

## Internet Gaming Database Setup

1. Navigate to the following link, and follow the 'Get Started' guide to generate the API key. 

        https://www.igdb.com/api
        
2. Once you have generated the API key, you should have an Client ID and a Access Token. Add the two the 'ćonfig.py'. Also, ensure that 'Bearer' is present in the string with a captailised 'B'. 

        igdbClient_id = "[Client ID]"
        igbdAuth_token = "Bearer [Access Token]"
        
## Toggle Setup

Currently not implemented, will add at a later date.

# Discord Bot commands

Below is a list of bot commands that you can use within the server or via DM.

/log    Manually add a game to the log.         Arguements: "[game title]"      Example: /log "Halo Infinite" 
