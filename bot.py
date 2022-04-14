import discord
import os
from discord.ext import commands,tasks
import asyncio

#bot instance
bot = commands.Bot(command_prefix='.')  #roept bot aan
#Token van de bot
token = "OTYzOTIwMTQxNTg0ODM4NzU4.YldGlg.GkrhmXYHPNsl_BSsbXMfRptW88w"

#Als messages.txt niet bestaat maak er een aan
if not (os.path.isfile('messages.txt')):
    f= open("messages.txt","w+",encoding='utf-8')
    f.close()

#Als bot ready is print ready
@bot.event
async def on_ready():
    print("Ready!")

#Als iemand een berichtje stuurt in de chat
@bot.event
async def on_message(message):
    print(f"New message ->{message.content}")
    #open messages.txt voert berichtje in
    with open("messages.txt", "a",encoding='utf-8') as myfile:
        myfile.write(message.content+"\n")
        

bot.run(token) 