
import discord
from discord.ext import commands
import openai
from openai import OpenAI

#Установка токена
DISCORD_TOKEN = "MTIyMjg3NjUxMDAzNDMyOTcyMQ.G7yJ-v.OP4YMpyaWfsdWX3nikyzjBlR2rkJI84TYjrp0w"
OPENAI_API_KEY = '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'

#Подключение openAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Создание клиента Discord
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#Уведомление о активации бота по его готовности
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

#Команда для отправки боту сообщения    
@bot.command()
async def chat(ctx, *, prompt):
#Создаём переменную ответа бота, в которой задаём промт поведения, промт помощника и в промт пользователся вписываем переменную, в которой хранится текст сообщения
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Тебе необходимо поддерживать диалог. Ты должен запоминать предедущие отправленные тебе сообщения и брать из них контекст для вопроса и/или ответа"},
            {"role": "assistant", "content": "Тебе необходимо следовать контексту предыдущих сообщений и не повторять вопросы"},
            {"role": "user", "content": prompt}],
        model="gpt-3.5-turbo-0125",
        temperature=1,
        max_tokens=2000
        )
    #Отсылаем ответ в качестве reply
    await ctx.reply(response.choices[0].message.content)


@bot.command()
async def image(ctx, *, prompt):
    response = client.images.generate(
        model="dall-e-2", #лимит 5 картинок в минуту
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        
    )
    await ctx.reply(response.data[0].url)
'''это не работает с dalle-3 (пишет, что слишком часто генерю картинки. 
У далли 3 частота не может быть выше 1 картинки в минуту на бесплатной версии. 
А я генерил 0, вообще, потому что программа не работала, 
а на вход в n подаётся количество картинок для генераци, она там одна и короче хз, не работает)'''
    
    

bot.run(DISCORD_TOKEN)
