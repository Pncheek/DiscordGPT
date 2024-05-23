
import discord
from discord.ext import commands
import openai
from openai import OpenAI

#initialazing the token and pasting API key
DISCORD_TOKEN = "YOUR BOT TOKEN"
OPENAI_API_KEY = "YOUR API KEY"

#connecting openAI
client = OpenAI(api_key=OPENAI_API_KEY)

#creating dicrod client
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#message about bot readiness
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
 
@bot.command()
async def chat(ctx, *, prompt):
#creating async function with bot prompt and it's answer
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
        style="natural",
        size="1024x1024",
        quality="standard",
        
    )
    await ctx.reply(response.data[0].url)
#for some reason do not work with DALL-E 3
    

bot.run(DISCORD_TOKEN)
