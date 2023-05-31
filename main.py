import random
import string

import discord
from discord.ext import commands

bot = discord.client
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
TOKEN = "MTEwNDQ0MDI3NTEzNDMxNjY4NA.G7zbIi.AujXs_IZl2fUfhIVfG7yuF_LdiRjJ65ofUaRkE"


@bot.event
async def on_ready():
    print('Logged on as {0} !'.format(bot.user))
    print("Logged and started")


# MJ Part
varTopic1Global = "0"
varTopic2Global = "0"
varTopic3Global = "0"
varTopic4Global = "0"
varTopic5Global = "0"
executedStartGame = 0


@bot.command(name="s")
async def s(ctx):
    testCommandAnouncement = "[Command Manger] Activated command : '{0}'".format(s)
    print(testCommandAnouncement)
    randomLetter = random.choice(string.ascii_uppercase)
    print(randomLetter)
    await ctx.send(testCommandAnouncement + "\n" + "[Start Game Command] State = 1 ; Generated letter : " + randomLetter
                   + "\n" + "Choisissez 5 sujets pour le petit bac en tapant : !topic1 ... or !topic2 ...")
    global executedStartGame
    executedStartGame = 1


@bot.command(name="topic1")
async def topic1(ctx, varTopic1):
    if executedStartGame != 0:
        if commands.Author == 744170130170445937 or 1104440275134316684:
            global varTopic1Global
            varTopic1Global = varTopic1
            print("[Star Game Command] Very Good !" + varTopic1)
        else:
            print("[Start Game Command] Not able to use this command !")
            await ctx.send("[Start Game Command] Not able to use this command !")
    else:
        print("[Start Game command] Major error, the first command wasn't executed ! Report !")


@bot.command(name="topic2")
async def topic1(ctx, varTopic2):
    if executedStartGame != 0:
        if commands.Author == 744170130170445937 or 1104440275134316684:
            global varTopic2Global
            varTopic2Global = varTopic2
            print("[Star Game Command] Very Good !" + varTopic2)
        else:
            print("[Start Game Command] Not able to use this command !")
            await ctx.send("[Start Game Command] Not able to use this command !")
    else:
        print("[Start Game command] Major error, the first command wasn't executed ! Report !")


@bot.command(name="topic3")
async def topic1(ctx, varTopic3):
    if executedStartGame != 0:
        if commands.Author == 744170130170445937 or 1104440275134316684:
            global varTopic3Global
            varTopic3Global = varTopic3
            print("[Star Game Command] Very Good !" + varTopic3)
        else:
            print("[Start Game Command] Not able to use this command !")
            await ctx.send("[Start Game Command] Not able to use this command !")
    else:
        print("[Start Game command] Major error, the first command wasn't executed ! Report !")


@bot.command(name="topic4")
async def topic1(ctx, varTopic4):
    if executedStartGame != 0:
        if commands.Author == 744170130170445937 or 1104440275134316684:
            global varTopic4Global
            varTopic4Global = varTopic4
            print("[Star Game Command] Very Good !" + varTopic4)
        else:
            print("[Start Game Command] Not able to use this command !")
            await ctx.send("[Start Game Command] Not able to use this command !")
    else:
        print("[Start Game command] Major error, the first command wasn't executed ! Report !")


@bot.command(name="topic5")
async def topic1(ctx, varTopic5):
    if executedStartGame != 0:
        if commands.Author == 744170130170445937 or 1104440275134316684:
            global varTopic5Global
            varTopic5Global = varTopic5
            print("[Star Game Command] Very Good !" + varTopic5)
            if varTopic1Global != "0" and varTopic2Global != "0" and varTopic3Global != "0" and varTopic4Global != "0" and varTopic5Global != "0":
                await topicsanouncementglobal(ctx)
            else:
                print("[Start Game Command] The topics aren't completed !")
                ctx.send("[Start Game Command] The topics aren't completed !")
        else:
            print("[Start Game Command] Not able to use this command !")
            await ctx.send("[Start Game Command] Not able to use this command !")
    else:
        print("[Start Game command] Major error, the first command wasn't executed ! Report !")


async def topicsanouncementglobal(ctx):
    print("[Start Game Command] The topics are the followings :\n"
          "1 - " + varTopic1Global + "\n"
                                     "2 - " + varTopic2Global + "\n"
                                                                "3 - " + varTopic3Global + "\n"
                                                                                           "4 - " + varTopic4Global + "\n"
                                                                                                                      "5 - " + varTopic5Global + "\n"
                                                                                                                                                 "Enjoy !")

    await ctx.send("[Start Game Command] The topics are the followings :\n"
                   "1 - " + varTopic1Global + "\n"
                                              "2 - " + varTopic2Global + "\n"
                                                                         "3 - " + varTopic3Global + "\n"
                                                                                                    "4 - " + varTopic4Global + "\n"
                                                                                                                               "5 - " + varTopic5Global + "\n"
                                                                                                                                                          "Enjoy !")


# Player Part
@bot.command(name="ans1")
async def ans1(ctx, ans1):
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))

@bot.command(name="ans1")
async def ans1(ctx, ans1):
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))

@bot.command(name="ans1")
async def ans1(ctx, ans1):
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))

@bot.command(name="ans1")
async def ans1(ctx, ans1):
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))

@bot.command(name="ans1")
async def ans1(ctx, ans1):
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))


bot.run(TOKEN)
