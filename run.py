import discord
from discord.ext import commands
from openai import OpenAI

#Установка токена
DISCORD_TOKEN = "MTIyMjg3NjUxMDAzNDMyOTcyMQ.GVPNL0.TbzsA9uwPNItSEqGMcd-K2wjkuZkPChaiaQT9U"
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
    

bot.run(DISCORD_TOKEN)
