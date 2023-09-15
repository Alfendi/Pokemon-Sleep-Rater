import discord
import os
from dotenv import load_dotenv
from pokemon import RatePokemon
from ocr import detect_text_uri


class PokemonSleepRatingBot(discord.Client):
    async def on_message(self, message):
        # Prevents bot from replying to itself.
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!rateps'):
            if message.attachments and any(
                    att.filename.endswith(('.png', '.jpg', '.jpeg')) for att in message.attachments):
                await message.reply(RatePokemon().rate_pokemon(detect_text_uri(message.attachments[0].url)))


intents = discord.Intents.default()
intents.message_content = True

client = PokemonSleepRatingBot(intents=intents)
client.run(os.getenv('BOT_TOKEN'))
