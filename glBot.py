#Config Keys
import config
import time
import datetime

import discord
from discord.ext import commands, tasks

import glSheets, glGiantBomb

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
  print("Bot has started.")
  if not loop.is_running():
    loop.start()

@tasks.loop(seconds=1)
async def loop():
  previousActivity = None
  while True:
    user = await bot.fetch_user(config.userID)
    mutual_guild = user.mutual_guilds[0]
    member = mutual_guild.members[0] 
    rawOutput = member.activity

    if rawOutput != None and rawOutput.type == discord.ActivityType.playing:
      if rawOutput.name != previousActivity:
        gameTitle = rawOutput.name
        rawTime = rawOutput.start
        convertTime = datetime.datetime.fromtimestamp(rawTime.timestamp())
        startTime = convertTime.strftime('%d/%m/%Y %H:%M:%S')
        gameFirstPlayed = convertTime.strftime('%d/%m/%Y')

        previousActivity = gameTitle
        print(f"Title: {gameTitle}, Start: {startTime}")
      else:
        pass
    elif rawOutput == None and rawOutput != previousActivity:
      previousActivity = None
      currentTime = datetime.datetime.now()
      endTime = currentTime.strftime('%d/%m/%Y %H:%M:%S')
      print(f"Title: {gameTitle}, End: {endTime}")

      gameTitle, gameDeveloper, gamePublisher, gameGenre, gameReleaseYear = glGiantBomb.gbCheck(gameTitle)

      glSheets.gameCheck(gameTitle, gameDeveloper, gamePublisher, gameGenre, gameReleaseYear, gameFirstPlayed)
      
    else:
      print("Nothing")
      pass

    time.sleep(10)

bot.run(config.discordKey)