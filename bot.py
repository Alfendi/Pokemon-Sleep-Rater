import config
import discord
import crop
from pokemon import RatePokemon
from ocr import detect_text_uri


class PokemonSleepRatingBot(discord.Client):
    async def on_message(self, message):
        # Prevents bot from replying to itself.
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!rate'):
            if message.attachments and any(
                    att.filename.endswith(('.png', '.jpg', '.jpeg')) for att in message.attachments):
                # pokemon, nature, skills = detect_text_uri(message.attachments[0].url)
                # obj = RatePokemon(pokemon, nature, skills)
                # print(obj.rate_pokemon())
                await message.reply(RatePokemon(*detect_text_uri(message.attachments[0].url)).rate_pokemon())


intents = discord.Intents.default()
intents.message_content = True

client = PokemonSleepRatingBot(intents=intents)
client.run(config.BOT_TOKEN)
