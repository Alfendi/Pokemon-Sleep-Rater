# Pokémon Sleep Rater Discord Bot
A Discord bot that rates Pokémon from Pokémon Sleep! All you need to do is invite the bot to your server (link below) and use the slash command /rateps when you upload a screenshot. Be sure the screenshot contains the Pokémon's name (no nicknames, sorry!), nature, and subskills. The bot may fail if a screenshot is unclear or if too many requests are made at once.

<i>Currently awaiting Discord verification to join more servers!</i> Also transitioning to Cloud-hosting!

<p align="center">Example Output:</p>

<p align="center">
  <img src="https://i.imgur.com/dSDM6rh.png">
</p>

Scores for the subskills are credited to u/drake8thecake's top tier spreadsheet. Each Pokémon is graded differently according to their specialty.

<p align="center">
  <img src="https://i.imgur.com/ZLEUsjJ.png">
</p>

Scores for the nature are an aggregation calculated by SaintPebble from three different sources including u/PigsInTrees, u/drake8thecake, and the Discord [Sleep Mathcord](https://discord.gg/mphzREMkwe).

The bot combines all the raw scores and rates it on a grading scale proposed by SaintPebble. At the moment, it is:

S: 24+

A: 21 — 23

B: 18 — 20

C: 15 — 17

D: 12 — 14

F: 11 and under

The scale accounts for the varying min/max values of the three specialties: Berries: 6 — 25, Ingredients 11 — 24, and Skills 10.5 — 26. Accordingly, a Pokémon's specialty is the first value to be considered then rated in the proper category. All emojis used in the bot's final evaluation belong to their respective creators.

I realise that this grading scale as well as the values of each subskill and nature are highly subjective. I'd love to hear any opinions, suggestions, or changes that you may have—whether it be regarding the bot or the code @ alfendi on Discord. Many thanks!

# Links
- SaintPebble's spreadsheet: [Link](https://docs.google.com/spreadsheets/d/1HSEzTWlboKHFOV7piqsk82E1Wapa9J-dQmOOdY8RNJY/edit?usp=sharing)
- /u/drake8thecake's spreadsheet: [Link](https://www.reddit.com/r/PokemonSleep/comments/167tiuz/updated_pokemon_sleep_data_and_tier_list_incl/?rdt=39154)
- /u/PigsInTrees's infographic: [Link](https://www.reddit.com/r/PokemonSleep/comments/15wkab7/pigs_made_a_nature_infograph/)
- Bot Invite: [Link](https://discord.com/oauth2/authorize?client_id=1148461688690069628&permissions=412317240384&scope=bot)
- Reddit Post: [Link](https://www.reddit.com/r/PokemonSleep/comments/16eiidw/i_made_a_pok%C3%A9mon_sleep_rating_discord_bot/)

# Change Log

v1.0 Released
v1.1 Update: Added Mimes, changed library from discord.py to pycord, changed command from !rateps to /rateps, updated final evaluation look, added error validation, set-up PostgreSQL Cloud connection.
