class RatePokemon:
    # Pokemon ordered by category, reverse mapping used for O(1) lookup efficiency.
    pokemon = {'Bulbasaur': 'Ingredients', 'Ivysaur': 'Ingredients', 'Venasaur': 'Ingredients',
               'Charmander': 'Ingredients', 'Charmeleon': 'Ingredients', 'Charizard': 'Ingredients',
               'Squirtle': 'Ingredients', 'Wartortle': 'Ingredients', 'Blastoise': 'Ingredients',
               'Caterpie': 'Berries', 'Metapod': 'Berries', 'Butterfree': 'Berries',
               'Rattata': 'Berries', 'Raticate': 'Berries',
               'Ekans': 'Berries', 'Arbok': 'Berries',
               'Pikachu': 'Berries', 'Raichu': 'Berries',
               'Jigglypuff': 'Skills', 'Wigglytuff': 'Skills',
               'Diglett': 'Ingredients', 'Dugtrio': 'Ingredients',
               'Meowth': 'Skills', 'Persian': 'Skills',
               'Psyduck': 'Skills', 'Golduck': 'Skills',
               'Mankey': 'Berries', 'Primeape': 'Berries',
               'Growlithe': 'Skills', 'Arcanine': 'Skills',
               'Bellsprout': 'Ingredients', 'Weepinbell': 'Ingredients', 'Victreebel': 'Ingredients',
               'Geodude': 'Ingredients', 'Graveler': 'Ingredients', 'Golem': 'Ingredients',
               'Slowpoke': 'Skills', 'Slowbro': 'Skills',
               'Magnemite': 'Skills', 'Magneton': 'Skills',
               'Doduo': 'Berries', 'Dodrio': 'Berries',
               'Gastly': 'Ingredients', 'Haunter': 'Ingredients', 'Gengar': 'Ingredients',
               'Cubone': 'Berries', 'Marowak': 'Berries',
               'Kangaskhan': 'Ingredients',
               'Pinsir': 'Ingredients',
               'Ditto': 'Ingredients',
               'Eevee': 'Skills', 'Vaporeon': 'Skills', 'Jolteon': 'Skills', 'Flareon': 'Skills',
               'Chikorita': 'Berries', 'Bayleef': 'Berries', 'Meganium': 'Berries',
               'Cyndaquil': 'Berries', 'Quilava': 'Berries', 'Typhlosion': 'Berries',
               'Totodile': 'Berries', 'Croconaw': 'Berries', 'Feraligatr': 'Berries',
               'Pichu': 'Berries',
               'Igglybuff': 'Skills',
               'Togepi': 'Skills', 'Togetic': 'Skills',
               'Mareep': 'Skills', 'Flaaffy': 'Skills', 'Ampharos': 'Skills',
               'Sudowoodo': 'Skills',
               'Espeon': 'Skills', 'Umbreon': 'Skills',
               'Slowking': 'Skills',
               'Wobbuffet': 'Skills',
               'Heracross': 'Skills',
               'Houndour': 'Berries', 'Houndoom': 'Berries',
               'Larvitar': 'Ingredients', 'Pupitar': 'Ingredients', 'Tyranitar': 'Ingredients',
               'Slakoth': 'Berries', 'Vigoroth': 'Berries', 'Slaking': 'Berries',
               'Sableye': 'Skills',
               'Gulpin': 'Skills', 'Swalot': 'Skills',
               'Swablu': 'Berries', 'Altaria': 'Berries',
               'Absol': 'Ingredients',
               'Wynaut': 'Skills',
               'Spheal': 'Berries', 'Sealeo': 'Berries', 'Walrein': 'Berries',
               'Bonsly': 'Skills',
               'Riolu': 'Skills', 'Lucario': 'Skills',
               'Croagunk': 'Ingredients', 'Toxicroak': 'Ingredients',
               'Magnezone': 'Skills',
               'Togekiss': 'Skills',
               'Leafeon': 'Skills', 'Glaceon': 'Skills', 'Sylveon': 'Skills',
               'Mime Jr.': 'Ingredients', 'Mr. Mime': 'Ingredients',
               'Cleffa': 'Berries', 'Clefairy': 'Berries', 'Clefable': 'Berries',
               'Shuppet': 'Berries', 'Banette': 'Berries',
               'Onix': 'Berries', 'Steelix': 'Berries',
               'Delibird': 'Ingredients',
               'Snover': 'Ingredients', 'Abomasnow': 'Ingredients'
               }

    # Nature rated by category. [0] = Berries, [1] = Ingredients, [2] = Skills.
    natures = {'Hardy': [1.00, 1.00, 1.00], 'Lonely': [1.00, 1.00, 0.67], 'Brave': [1.67, 1.67, 1.67],
               'Adamant': [3.00, -0.17, 0.67], 'Naughty': [1.83, 1.67, -0.17],
               'Bold': [-1.33, -1.33, -1.00], 'Docile': [1.00, 1.00, 1.00], 'Relaxed': [-0.67, -0.67, -0.33],
               'Impish': [1.50, -1.33, -0.17], 'Lax': [0.17, 0.17, -1.00],
               'Timid': [-1.00, -1.00, -1.00], 'Hasty': [0.33, 0.33, 0], 'Serious': [1.00, 1.00, 1.00],
               'Jolly': [2.17, -1.00, 0.17], 'Naive': [0.83, 0.58, -1.00],
               'Modest': [-1.67, 0.50, -0.33], 'Mild': [-1.00, 1.17, 0], 'Quiet': [-0.67, 2.00, 1.00],
               'Bashful': [1.00, 1.00, 1.00], 'Rash': [-0.50, 2.00, -0.67],
               'Calm': [-0.67, -0.67, 0.67], 'Gentle': [-0.33, 0.33, 1.33], 'Sassy': [0, 0.25, 1.67],
               'Careful': [1.50, -1.00, 1.33], 'Quirky': [1.00, 1.00, 1.00]}

    # Subskills rated by category. [0] = Berries, [1] = Ingredients, [2] = Skills.
    subskills = {'Berry Finding S': [5, 4, 5], 'Dream Shard Bonus': [2, 2, 2],
                 'Energy Recovery Bonus': [3, 3, 3], 'Energy Recovery S': [], 'Energy Recovery M': [],
                 'Helping Bonus': [5, 5, 5], 'Helping Speed S': [3, 3, 3], 'Helping Speed M': [4, 4, 4],
                 'Ingredient Finder S': [1, 4, 3], 'Ingredient Finder M': [1, 5, 4],
                 'Inventory Up S': [2, 3, 2], 'Inventory Up M': [3, 4, 3], 'Inventory Up L': [4, 5, 4],
                 'Research EXP Bonus': [2, 2, 2],
                 'Skill Level Up S': [3, 3, 4], 'Skill Level Up M': [4, 4, 5],
                 'Skill Trigger S': [3, 3, 4], 'Skill Trigger M': [4, 4, 5],
                 'Sleep EXP Bonus': [3, 3, 3]}

    def __init__(self, name='', nature='', skills=None):
        self.name = name
        self.nature = nature
        if skills is None:
            skills = []
        self.skills = skills
        self.skills_value = {}
        self.nature_rating = 0
        self.skills_rating = 0

    def get_stats(self):
        return self.name, self.nature, self.skills

    def find_specialty(self, results):
        for item in results:
            if item in self.pokemon:
                self.name = item
            if item in self.natures:
                self.nature = item
            if item in self.subskills:
                self.skills.append(item)
        print('!')
        return self.pokemon.get(self.name)

    def berries_subskills(self):
        for i in self.skills:
            self.skills_value[i] = RatePokemon.subskills[i][0]
            self.skills_rating += RatePokemon.subskills[i][0]
        return self.skills_rating

    def ingredients_subskills(self):
        for i in self.skills:
            self.skills_value[i] = RatePokemon.subskills[i][1]
            self.skills_rating += RatePokemon.subskills[i][1]
        return self.skills_rating

    def skills_subskills(self):
        for i in self.skills:
            self.skills_value[i] = RatePokemon.subskills[i][2]
            self.skills_rating += RatePokemon.subskills[i][2]
        return self.skills_rating

    def subskills_to_string(self):
        order = [0, 3, 1, 4, 2]
        prefixes = ["[Lv. 10]", "[Lv. 25]", "[Lv. 50]", "[Lv. 75]", "[Lv. 100]"]

        keys_list = list(self.skills_value.keys())
        formatted_output = []

        for i, idx in enumerate(order):
            key = keys_list[idx]
            formatted_output.append(f'{prefixes[i]} __{key}__: {self.skills_value[key]}')

        return '\n'.join(formatted_output)


    def grading_scale(self, grade):
        if grade <= 11.0:
            return '**F**! <a:torchheadbang:1150206226181918720>'
        elif 11.0 < grade <= 14.0:
            return '**D**! <:psyduck:1150207071468388432>'
        elif 14.0 < grade <= 17.0:
            return '**C**! <:flushedtomb:1150206887812419665>'
        elif 17.0 < grade <= 20.0:
            return '**B**! <a:squirtlevibe:1150206216451137586>'
        elif 20.0 < grade <= 23.0:
            return '**A**! <:raichudab:1150207082390368388>'
        else:
            return '**S**! <:gengarshades:1150207094297997332>'

    def rate_pokemon(self, results):
        specialty = self.find_specialty(results)
        if specialty == 'Berries':
            self.nature_rating = RatePokemon.natures[self.nature][0]
            grade = self.berries_subskills() + self.nature_rating
        elif specialty == 'Ingredients':
            self.nature_rating = RatePokemon.natures[self.nature][1]
            grade = self.ingredients_subskills() + self.nature_rating
        elif specialty == 'Skills':
            self.nature_rating = RatePokemon.natures[self.nature][2]
            grade = self.skills_subskills() + self.nature_rating
        else:
            return False
        return self.name, self.grading_scale(grade), self.skills_value, str(self.nature), str(self.nature_rating), str(grade)
        # return f'*Your Pokémon is rated {self.grading_scale(grade)}* \n\n``Subskills``\n{self.subskills_to_string()} ' \
        #        f'\n\n``Nature``\n__{str(self.nature)}__: {str(self.nature_rating)} \n\n``Total Score`` \n**{str(grade)}**'

        # self.subskills_to_string(), 


# obj = RatePokemon(*detect_text_uri('https://cdn.discordapp.com/attachments/1056493099649597491/1149879618195685457/Screenshot_20230908_174928_Pokmon_Sleep.jpg'))
# name = 'Spheal'
# nature = 'Impish'
# skills = ['Energy Recovery Bonus', 'Inventory Up S', 'Helping Speed M', 'Inventory Up L', 'Skill Trigger S']
# obj = RatePokemon(name, nature, skills)
#
# print(obj.rate_pokemon())

# results = ['Frequency', 'Lv. 10', 'Main Skill & Sub Skills', 'ⒸLv. 50', 'Ingredient Finder S', 'RP 389', 'Swablu', 'Lv. 100', 'Inventory Up S', 'Charge Energy S', 'Restores 12 Energy to the user.', 'Helping Speed S', 'Nature', 'Additional Stats', 'Back', 'Adamant', 'Date Met', 'Every 1 hr 2 mins 14 secs', 'Place Met', 'Sleeping Time Shared', 'Lv. 25', 'Energy Recovery Bonus', 'ⒸLV. 75', 'Skill Trigger S', 'Speed of help ▲▲', 'Ingredient finding', 'Lv.1', 'August 31, 2023', 'Greengrass Isle', 'Zzz 12 hrs 10 mins', '|||']

# obj = RatePokemon()
# print(obj.rate_pokemon(results))
