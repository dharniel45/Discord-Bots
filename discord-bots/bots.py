import discord

TOKEN = "OTQyMDQzNjIxNzk0OTA2MTYy.YgewfQ.5gY_EO4GHP-00FMV6IB5L_A3Q5Q"

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
