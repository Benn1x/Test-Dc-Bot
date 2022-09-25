
# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTAyMzU1OTY2NTEyNjIyMzk1Mg.GcCu83.pkUmv2pF7a86-G-otVbtjBSv8cAie7g9qQ38nQ')
