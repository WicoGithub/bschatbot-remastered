# -*- coding: utf-8 -*-

# BSChatBot - Собственный чат-бот по игре Brawl Stars!
# Автор оригинального кода: YT|дима читер#0641
# Remastered By Wico

# Импортирование библиотек
try:
    import discord, random, config
    from discord.ext import commands
except: 
    print('<Ошибка> Не удалось импортировать библиотеки!')

bot = commands.Bot(command_prefix=None, intents=discord.Intents.default()) # Создаём переменную бота и включаем интенты

# Переменные
name_bot = config.name_bot

with open('token.txt', 'r') as f: token = f.read() # Читаем файл с токеном и записываем токен в переменную

# Слова, которые бот будет отправлять в чат, рекомендую не трогать
shelly = ["Пошли за ним", "Давайте сделаем это!", "Ха-ха!", "Золотце!", "Невероятно!", "Фантастика!", "Да!", "Ю-пи!", "Ву-ху"]
colt = ["Берегись, я иду!", "Я слишком хорош!", "Номер один!", "Прости, нуб.", "Какой хедшот!", "Да!"]
nita = ["Нита..!", "Да-а-а..!", "Мишка-а..!"]
bull = ["Эй, я здесь козырь!", "Не связывайся с Буллом!", "Тебе лучше в этом у-Булл-иться!", "И не вставай!", "Ты попал в меня...", "Буллдозее-ер!"]
dinamike = ["Я взрывоопасен!", "Птички поют.", "Кому еще тротила?", "Я сержусь.", "Прямо в карьер!"]
jessie = ["Джесс починит!", "Я номер один!", "Нет!", "Ха-ха-ха!", "Строю!"]
vosembit = ["Игрок ПЕРВЫЙ, будь ГОТОВ!", "Новый РЕКОРД!", "Игра НЕ окончена", "Иди к на-ам! Ням-ням!"]
emz = ["Посмотри на меня!.. Да не так!", "И я упс…", "OMG, ты так плох!", "Ты не получишь свой браслет дружбы!", "Попробуй новые духи!"]
sty = ["Кто хо~хо-хо~очет авто-о-о-граф?", "Ха-ХА-ха, я по-ПО-поймал тебя!", "Аварии, огонь! Починят — вернусь.", "Уи-и-и-и!..", "Я по-по-покажу тебе безумие."]
leon = ["Вперед!", "Леон главней!", "Да ну!", "Да-да-да!", "Нечестно!"]

# Эвенты
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=f"{len(bot.guilds)} сервер(-ов)! | {name_bot}", url = "https://www.youtube.com/watch?v=z2JmKR_STSw",type=3))
    print(f"<Информация> Бот запустился! Работаю на аккаунте: {bot.user}/{bot.user.id}")
    print(f"<Информация> Кол-во серверов: {len(bot.guilds)}")

@bot.event
async def on_guild_join(guild): await bot.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=f"{len(bot.guilds)} сервер(-ов)! | {name_bot}", url = "https://www.youtube.com/watch?v=z2JmKR_STSw",type=3))

@bot.event
async def on_guild_remove(guild): await bot.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=f"{len(bot.guilds)} сервер(-ов)! | {name_bot}", url = "https://www.youtube.com/watch?v=z2JmKR_STSw",type=3))

@bot.event
async def on_message(message):
    if message.content.lower() == "шейли": await message.channel.send(f"{random.choice(shelly)}")
    if message.content.lower() == "кольт": await message.channel.send(f"{random.choice(colt)}")
    if message.content.lower() == "нита": await message.channel.send(f"{random.choice(nita)}")
    if message.content.lower() == "булл": await message.channel.send(f"{random.choice(bull)}")
    if message.content.lower() == "диномайк": await message.channel.send(f"{random.choice(dinamike)}")
    if message.content.lower() == "джесси": await message.channel.send(f"{random.choice(jessie)}")
    if message.content.lower() == "8-бит": await message.channel.send(f"{random.choice(vosembit)}")
    if message.content.lower() == "эмз": await message.channel.send(f"{random.choice(emz)}")
    if message.content.lower() == "сту": await message.channel.send(f"{random.choice(sty)}")
    if message.content.lower() == "леон": await message.channel.send(f"{random.choice(leon)}")

try: bot.run(token) # Запускаем бота.
except: print('<Ошибка> Не удалось запустить бота!')