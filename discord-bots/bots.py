import discord

TOKEN = "put you token"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!welcome'):
        await message.channel.send('Hello there!')

client.run(TOKEN)
