import discord
import os
from pokemon_db import db
from dotenv import load_dotenv
from pokemon import RatePokemon
from ocr import detect_text_uri

load_dotenv()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="rateps", description="Upload an image of your Pokémon to be rated.")
async def rateps(ctx, image: discord.Option(discord.Attachment, required=True)):
    if image:
        try:
            print(image)
            name, final_grade, skills_value, nature, nature_rating, grade = RatePokemon().rate_pokemon(
                detect_text_uri(image.url))
            embed = discord.Embed(
                title="Pokémon Evaluation",
                description=f"[*Your {name} is rated {final_grade}*]({image.url})",
                color=discord.Colour.green(),
            )
            embed.add_field(name="Subskills", value=f"{db.subskills_to_string(skills_value)}", inline=False)
            embed.add_field(name="Nature", value=f"{str(nature)}: {str(nature_rating)}", inline=False)
            embed.add_field(name="Total Score", value=f"{str(grade)}", inline=False)

            embed.set_author(name="Pokémon Sleep Rater", icon_url="https://i.imgur.com/xQ8V3OI.png")
            embed.set_thumbnail(url="https://i.imgur.com/Ox0DTqY.png")
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(
                "Pokémon not found. Please check image upload (name, nature, and subskills) or try again.")


bot.run(os.getenv('BOT_TOKEN'))
