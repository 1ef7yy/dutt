# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
import time
import server
import json
import requests
import weather

TOKEN = 'ODM0MDM4NDQxODUxMDkzMDUz.YH7E1A.X68nteEAg1T1Xyoc-OVziFbsxcg'

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('Бот готов')


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)}ms')


@client.command()
async def putin_pic(ctx):
    await ctx.send(
        f'https://cdn25.img.ria.ru/images/07e5/04/0e/1728256253_0:0:2971:1671_1920x0_80_0_0_afc9bb1388737b1ebbe1c379de61b2bb.jpg'
    )



@client.command()
async def currencies(ctx):
  link = 'https://www.cbr.ru/eng/currency_base/daily/'

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


  fullPage = requests.get(link, headers=headers)
  soup = BeautifulSoup(fullPage.content, "html.parser")
  zero = soup.findAll("td")
  string = f'{zero[54].text} USD\n{zero[59].text} EUR\n{zero[19].text} BYN'
  

  embed = discord.Embed(
    title = '1 RUB равен',
    description = string,
    colour = discord.Colour.from_rgb(255, 255, 0)
  )
  await ctx.send(embed=embed)

@client.command()
async def weather_now(ctx):
  appid='9a0e4ffe23b84856975e1e4a72d739bb'
  city_id = 1508291
  res_now = requests.get(f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&lang=ru&appid={appid}")
	#http://api.openweathermap.org/data/2.5/weather?id=1508291&units=metric&lang=ru&appid=9a0e4ffe23b84856975e1e4a72d739bb
  data_now = res_now.json()
  arr_now = [
  data_now['weather'][0]['description'], 
	data_now['main']['temp'],
	data_now['weather'][0]['icon']
	   ]
  F_CONST = 9/5
  fahr = int(arr_now[1])*F_CONST+32
  string_now = f'Сейчас в Челябинске {arr_now[1]} °C/{fahr} °F. В течение сегодняшнего дня будет {arr_now[0]}.'
  #string_next = f''
  await ctx.send(string_now)


@client.command()
async def weather_tomorrow(ctx):
  appid='9a0e4ffe23b84856975e1e4a72d739bb'
  city_id = 1508291
  res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})	
  data = res.json()
 # print(arr_now)
  #print(data)
  arr_next = data['list'][13] # tommorow midday
  #print(type(arr_next)) #<- dict
  temp_next = arr_next['main']['temp']
  descr_next = arr_next['weather'][0]['description']
  wind_next = arr_next['wind']['speed']
  F_CONST = 9/5
  fahr = round(temp_next)*F_CONST+32
  string = f'Завтра в Челябинске в 12:00 будет {round(temp_next)}°C/{fahr}°F, {descr_next}, скорость ветра будет {round(wind_next)} м/c'
  await ctx.send(string)

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.command(pass_context=True)
async def message_role(ctx, role: discord.Role, *, message):
  for member in ctx.guild.members:
    if role in member.roles:
      await member.send('xyu')

@client.command()
async def list_members(ctx):
  for guild in client.guilds:
    for member in guild.members:
      await ctx.send(member)




@client.command()
async def react_test(ctx):
  emoji = "😀"
  await ctx.message.add_reaction(emoji)
  time.sleep(10)
  await ctx.message.clear_reactions()
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


@client.command()
async def create_channel(ctx, name:str, t:str):
  # t это type
  guild = ctx.message.guild
  if t == 'text':
    await guild.create_text_channel(name)
  elif t == 'voice':
    await guild.create_voice_channel(name)
  else:
    await ctx.send('Ошибка обработки типа канала')


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    print(emoji)
    if user.bot:
      return

    

    # if emoji == "emoji 1":
    #     fixed_channel = bot.get_channel(channel_id)
    #     await fixed_channel.send(embed=embed)
    # elif emoji == "emoji 2":
    #     #do stuff
    # elif emoji == "emoji 3":
    #     #do stuff
    # else:
    #    return

@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')

    #Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON
    embed = discord.Embed(color=0xff9900, title='Random Fox')
    # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем


@client.event
async def on_command_error(ctx, error):
    print(error)
    # if isinstance(error, commands.MissingRequiredArgument):
    #     await ctx.send(
    #         'Ошибка доступа команды, проверьте свои привилегии и роли')
    # if isinstance(error, commands.CommandNotFound):
    #     await ctx.send("Такой команды, кажется, не существует")
    # else:
    #   print(error)


server.keep_alive()
client.run(TOKEN)
