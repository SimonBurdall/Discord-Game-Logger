import config
import datetime

import discord
from discord.ext import commands, tasks

import glSheets, glIGDB

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='/', intents=intents)
bot.allowed_dm_commands = True

@bot.event
async def on_ready():
  print("Bot has started.")
  if not loop.is_running():
    loop.start()

@bot.command(name='log', help='Manually log a game you are playing.', aliases=['hi', 'hey'])
async def log(ctx, gameSearch: str):
  gameTime = ""
  gameCompletionDate = ""

  date = datetime.datetime.now()
  gameFirstPlayed = date.strftime("%d/%m/%Y")
  gameLastPlayed = date.strftime("%d/%m/%Y")

  gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameArtwork, glIGDBOutput = glIGDB.gbCheck(gameSearch)
  glSheetOutput = glSheets.gameCheck(gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameTime, gameFirstPlayed, gameCompletionDate, gameLastPlayed)

  if glSheetOutput == "added":
    embed = discord.Embed(title="Logging: Added New Game", description=":turtle::turtle::turtle::turtle::turtle::turtle::turtle::turtle::turtle:", color=0x00ff00)
    embed.add_field(name="**"+gameTitle+"**", value="Platform: "+gamePlatform+"\nRelease Date: "+str(gameReleaseYear)+"\nGenre: "+gameGenre+"\n\n First played on "+str(gameFirstPlayed), inline=False)
    embed.add_field(name="",value=":video_game::video_game::video_game::video_game::video_game::video_game::video_game::video_game::video_game:")
    embed.set_image(url="https:"+gameArtwork+"?width=1272&height=716")
  elif glSheetOutput == "exists":
    embed = discord.Embed(title="Logging: Updated Existing Game", description=":turtle::turtle::turtle::turtle::turtle::turtle::turtle::turtle::turtle:", color=0x00ff00)
    embed.add_field(name="**"+gameTitle+"**", value="Platform: "+gamePlatform+"\nRelease Date: "+str(gameReleaseYear)+"\nGenre: "+gameGenre+"\n\n Updated last played on "+str(gameLastPlayed), inline=False)
    embed.add_field(name="",value=":video_game::video_game::video_game::video_game::video_game::video_game::video_game::video_game::video_game:")
    embed.set_image(url="https:"+gameArtwork+"?width=1272&height=716")
  if ctx.guild is not None:
    await ctx.message.delete()
  await ctx.send(embed=embed)

@tasks.loop(seconds=1)
async def loop():
  previousActivity = None
  while True:
    user = await bot.fetch_user(config.discordUser_id)
    mutual_guild = user.mutual_guilds[0]
    member = mutual_guild.members[0] 
    rawOutput = member.activity

    if rawOutput != None and rawOutput.type == discord.ActivityType.playing:
      if rawOutput.name != previousActivity:
        gameSearch = rawOutput.name
        rawTime = rawOutput.start
        convertTime = datetime.datetime.fromtimestamp(rawTime.timestamp())
        startTime = convertTime.strftime('%d/%m/%Y %H:%M:%S')
        gameFirstPlayed = convertTime.strftime('%d/%m/%Y')

        previousActivity = gameSearch
        print(f"Title: {gameSearch}, Start: {startTime}")
      else:
        pass
    elif rawOutput == None and rawOutput != previousActivity:
      previousActivity = None
      currentTime = datetime.datetime.now()
      endTime = currentTime.strftime('%d/%m/%Y %H:%M:%S')
      print(f"Title: {gameSearch}, End: {endTime}")

      gameTime = ""
      gameCompletionDate = ""
      
      date = datetime.datetime.now()
      gameLastPlayed = date.strftime("%d/%m/%Y")

      gameTitle, gamePlatform, gameGenre, gameReleaseYear = glIGDB.gbCheck(gameSearch)
      glSheets.gameCheck(gameTitle, gamePlatform, gameGenre, gameReleaseYear, gameTime, gameFirstPlayed, gameCompletionDate, gameLastPlayed)
      
    else:
      pass
bot.run(config.discord_Key)