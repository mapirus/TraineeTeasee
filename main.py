import thecampy
import discord
import re
from discord.ext import commands
from to import code
import requests

bot = commands.Bot(command_prefix='!')
p = re.compile('[^/]+/[^/]+/[^/]+')

soldier = thecampy.Soldier('이규진', '19990405', '20220411', '육군훈련소')
soldier.soldier_code = 1596695
#tc.get_soldier(soldier)
@bot.event
async def on_ready():
    print('Logging in...')
    print(f"Connecting with {bot.user.name}")
    print('Complete')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("탄소낭비율 ~1.25g/장"))

@bot.command(name='ㅇㅍ')
async def send(ctx, *, text):
    if p.match(text):
        curser = text.rfind('/')
        msg = thecampy.Message(text[:curser], text[curser + 1:])
        tc = thecampy.Client('mapirus7777@naver.com', 'tuna@7777')

        attachsize = len(ctx.message.attachments)
        if attachsize > 0:
            if attachsize > 1:
                await ctx.send("사진은 한 장만!")
                return

            print('이미지 첨부 메시지 전송')
            img = requests.get(ctx.message.attachments[0].url).content
            tc.send_message(soldier, msg, thecampy.images.ThecampyImage(img))
            await ctx.send("전송됨")
            return
        print('일반 메시지 전송')
        tc.send_message(soldier, msg)
        await ctx.send("전송됨")
    else:
        await ctx.send("다음과 같은 형식 : !ㅇㅍ 제목/글쓴이/내용")

bot.run(code)