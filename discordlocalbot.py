import discord
from transformers import pipeline
token = 'paste you token here :'

generator = pipeline('text-generation', model='gpt2')# you can change model name

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        prompt = message.content
        response = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        await message.channel.send(response)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
