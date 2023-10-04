import os
import random
import string
import psutil

import discord
from discord.ext import commands


bot = discord.client
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = open("token.txt", "r")
TOKEN = token.read()


@bot.event
async def on_ready():
    print('Logged on as {0} !'.format(bot.user))
    print("Logged and started")


async def computeringReport():
    mem_usage = psutil.virtual_memory()
    print(f"Free: {mem_usage.percent}%")
    print(f"Total: {mem_usage.total / (1024 ** 3):.2f}G")
    print(f"Used: {mem_usage.used / (1024 ** 3):.2f}G")
    per_cpu = psutil.cpu_percent(percpu=True)
    # For individual core usage with blocking, psutil.cpu_percent(interval=1, percpu=True)
    for idx, usage in enumerate(per_cpu):
        print(f"CORE_{idx + 1}: {usage}%")
    my_process = psutil.Process(os.getpid())
    print("Name:", my_process.name())
    print("PID:", my_process.pid)
    print("Executable:", my_process.exe())
    print("CPU%:", my_process.cpu_percent(interval=1))
    print("MEM%:", my_process.memory_percent())


@bot.command(name="join")
async def join(ctx):
    filePlayersList = open("players.txt", "a")
    filePlayersList = open("players.txt", "r")
    player = str(ctx.message.author)
    if filePlayersList.read().__contains__(player):
        print("jtm")
    else:
        filePlayersList = open("players.txt", "a")
        filePlayersList.write(player + "\n")





# MJ Part
varTopic1Global = "0"
varTopic2Global = "0"
varTopic3Global = "0"
varTopic4Global = "0"
varTopic5Global = "0"
executedStartGame = 0


@bot.command(name="s")
async def s(ctx):
    await computeringReport()
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
    await computeringReport()
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
async def topic2(ctx, varTopic2):
    await computeringReport()
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
async def topic3(ctx, varTopic3):
    await computeringReport()
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
async def topic4(ctx, varTopic4):
    await computeringReport()
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
async def topic5(ctx, varTopic5):
    await computeringReport()
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
    await computeringReport()
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
    await computeringReport()
    fileAns1 = open("ans1.txt", "a")
    fileAns1 = open("ans1.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns1.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns1 = open("ans1.txt", "a")
        fileAns1.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans1))


@bot.command(name="ans2")
async def ans2(ctx, ans2):
    await computeringReport()
    fileAns2 = open("ans2.txt", "a")
    fileAns2 = open("ans2.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns2.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns2 = open("ans2.txt", "a")
        fileAns2.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans2))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans2))


@bot.command(name="ans3")
async def ans3(ctx, ans3):
    await computeringReport()
    fileAns3 = open("ans3.txt", "a")
    fileAns3 = open("ans3.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns3.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns3 = open("ans3.txt", "a")
        fileAns3.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans3))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans3))


@bot.command(name="ans4")
async def ans4(ctx, ans4):
    await computeringReport()
    fileAns4 = open("ans4.txt", "a")
    fileAns4 = open("ans4.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns4.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns4 = open("ans4.txt", "a")
        fileAns4.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans4))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans4))


@bot.command(name="ans5")
async def ans5(ctx, ans5):
    await computeringReport()
    fileAns5 = open("ans5.txt", "a")
    fileAns5 = open("ans5.txt", "r")
    strAuthor = str(ctx.message.author)
    if fileAns5.read().__contains__(strAuthor):
        print("[Answer commands] You have already given an answer !")
        await ctx.send("[Answer commands] You have already given an answer !")
    else:
        fileAns5 = open("ans5.txt", "a")
        fileAns5.write("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans5))
        print("{0}".format(ctx.message.author) + " answered : {0}\n".format(ans5))


@bot.command(name="verify1")
async def verify1(ctx, i=0):
    global goodForAns1
    await computeringReport()
    fileAns1Verif = open("ans1.txt", "r")
    varVerifAns1 = fileAns1Verif.read()
    filePlayersList = open("players.txt", "r")
    filePlayersListLines = len(filePlayersList.readlines())
    filePlayersListLines - 1
    goodForAns1 = [filePlayersListLines]
    while i < filePlayersListLines:
        filePlayersList = open("players.txt", "r")
        fileAns1Verif = open("ans1.txt", "r")
        i = i + 1
        with open("players.txt", "r") as filePlayersList:
            ligne = filePlayersList.readline()
            while ligne != "":
                ligne = filePlayersList.readline()
        with open("ans1.txt", "r") as fileAns1Verif:
            ligne2 = fileAns1Verif.readline()
            while ligne2 != "":
                ligne2 = fileAns1Verif.readline()

        if ligne2.__contains__(ligne):
            print(ligne)
            print(ligne2)
            goodForAns1.append(i)
            goodForAns1Bol = True

    if goodForAns1[-1] == goodForAns1[0]:
        if goodForAns1Bol == True:
            print("[Verify Command] Answers for the question 1 : " + varVerifAns1)
            await ctx.send("[Verify Command] Answers for the question 1 : " + varVerifAns1)


@bot.command(name="verify2")
async def verify2(ctx):
    await computeringReport()
    fileAns2Verif = open("ans2.txt", "r")
    varVerifAns2 = fileAns2Verif.read()

    print("[Verify Command] Answers for the question 2 : " + varVerifAns2)
    await ctx.send("[Verify Command] Answers for the question 2 : " + varVerifAns2)


@bot.command(name="verify3")
async def verify3(ctx):
    await computeringReport()
    fileAns3Verif = open("ans3.txt", "r")
    varVerifAns3 = fileAns3Verif.read()

    print("[Verify Command] Answers for the question 3 :" + varVerifAns3)
    await ctx.send("[Verify Command] Answers for the question 3 : " + varVerifAns3)


@bot.command(name="verify4")
async def verify4(ctx):
    await computeringReport()
    fileAns4Verif = open("ans4.txt", "r")
    varVerifAns4 = fileAns4Verif.read()

    print("[Verify Command] Answers for the question 4 : " + varVerifAns4)
    await ctx.send("[Verify Command] Answers for the question 4 : " + varVerifAns4)


@bot.command(name="verify5")
async def verify5(ctx):
    await computeringReport()
    fileAns5Verif = open("ans5.txt", "r")
    varVerifAns5 = fileAns5Verif.read()

    print("[Verify Command] Answers for the question 5 : " + varVerifAns5)
    await ctx.send("[Verify Command] Answers for the question 5 : " + varVerifAns5)


@bot.command(name="addpoints")
async def addpoints(ctx, member, addedPoints, points=0):
    await computeringReport()
    filePoints = open("filepoints.txt", "r")
    addedPointsInt = int(addedPoints)
    points = points + addedPointsInt
    filePoints = open("filepoints.txt", "a")
    pointsString = str(points)
    filePoints.write(member + " has " + pointsString)


@bot.command(name="cleangame")
async def cleangame(ctx):
    await computeringReport()
    try:
        os.remove("ans1.txt")
    except FileNotFoundError:
        print("test4587")
    try:
        os.remove("ans2.txt")
    except FileNotFoundError:
        print("test4587")
    try:
        os.remove("ans3.txt")
    except FileNotFoundError:
        print("test4587")
    try:
        os.remove("ans4.txt")
    except FileNotFoundError:
        print("test4587")
    try:
        os.remove("ans5.txt")
    except FileNotFoundError:
        print("test4587")
    try:
        filePlayersList.close()
        os.remove("players.txt")
    except FileNotFoundError:
        print("test4587")


@bot.command(name="bu")
async def bu(ctx):
    bot.add_item(discord.ui.Button(Label="Test", urk="google.com"))


bot.run(TOKEN)
