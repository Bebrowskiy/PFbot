import disnake 
from disnake.ext import commands 

intents = disnake.Intents.all()

bot=commands.Bot(command_prefix=commands.when_mentioned_or("."), intents=intents)


class abot(disnake.Client):
    def __init__(self):
        super().__init__(intents = disnake.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = disnake.Object(id=1028442802251640924)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True

class Select(disnake.ui.Select):
    def __init__(self):
        options=[
            disnake.SelectOption(label="Каналы",emoji="<:bluearrow:1034158076489650196> ",description="О наших каналах!"),
            disnake.SelectOption(label="Администрация",emoji="<:bluearrow:1034158076489650196> ",description="Наша администрация!"),
            disnake.SelectOption(label="Сайт",emoji="<:bluearrow:1034158076489650196> ",description="Наш сайт сервера!")
            ]
        super().__init__(placeholder="Выберите нужное",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: disnake.Interaction):
        if self.values[0] == "Каналы":
            embed = disnake.Embed(title='Информация о каналах!',description="Всё в скоре будет")
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif self.values[0] == "Администрация":
            await interaction.response.send_message("Даже это будет",ephemeral=True)
        elif self.values[0] == "Сайт":
            await interaction.response.send_message("И даже больше этого",ephemeral=True)

class SelectView(disnake.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@bot.command()
async def menu(ctx):
    embed = disnake.Embed(title='Информация о сервере!',description="Мы очень рады, что ты зашел на наш сервер. Мы надеемся, что ты приятно проведешь время и позовешь сюда своих друзей. А узнать больше о нас внизу!",
                          color=ctx.author.color)
    embed.set_image(url=f'https://i.gifer.com/PFNA.gif')
    await ctx.send(embed=embed,view=SelectView())

@bot.event
async def on_ready():
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = disnake.Activity(
        type = disnake.ActivityType.watching,

        #Bot status
        name = f'{members} зайчиков!'

    ))
    print("Руководство по ботам")
    print(f'Вы вошли как \033[1m\033[31m{bot.user}\033[0m')

@bot.slash_command()
async def buttons(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        "Нужна помощь?",
        components=[
            disnake.ui.Button(label="Да", style=disnake.ButtonStyle.success, custom_id="yes"),
            disnake.ui.Button(label="Нет", style=disnake.ButtonStyle.danger, custom_id="no"),
        ],
    )


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["yes", "no"]:
        # We filter out any other button presses except
        # the components we wish to process.
        return

    if inter.component.custom_id == "yes":
        await inter.response.send_message("Напишите нам: https://vk.com/postfinem", ephemeral=True)
    elif inter.component.custom_id == "no":
        await inter.response.send_message("Приятного дня!")

@bot.command()
async def havev(ctx):
	await ctx.send("HAVEV")
token="OTQzMDAwMjUyOTQ3MDAxNDY1.GebwiW.pnS6CyD-x2ZjceuoU4VYlNFo2CFYyF7Cqflg0Q"
bot.run(token) 