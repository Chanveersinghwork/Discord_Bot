import discord
import openai
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

openai.api_key = "YOUR_OPENAI_API_KEY"
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('!ask '):
        user_message = message.content[5:]
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
        await message.channel.send(reply)

client.run(DISCORD_TOKEN)
