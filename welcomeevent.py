#Discord.py welcome channel system
import random
@bot.event
async def on_member_join(member): #Event to run when a member joins
    if member.guild.id != 921530640510382100 and member.guild.id != 885191951182356511: #If the member joins a server that is not the main server/s
        return #Return
    if member.bot == True: #If the member is a bot
        return #Return
    channel = bot.get_channel(1234) #replace with channel id
    membername = str(member)
    joinmessage = [f"Welcome to the server {membername}!", f"Welcome {membername}!", f"Welcome to the server {membername}! Enjoy your stay!", f"Welcome {membername}! Hope you brought pizza!", f"Welcome {membername}! Leave your shoes at the door!", f"Welcome {membername}! Don't forget to bring a towel!", f"Welcome {membername}! Have a nice day!", f"Welcome {membername}! Go grab a cup of coffee!", f"Welcome {membername}! The party don't start till you walk in!"] #Possible status options
    embed = discord.Embed(
        title=f"__**{random.choice(joinmessage)}**__",
        description=f"> **ID:** {member.id}",
        color=discord.Color.random()
        )
    try:
        icon = member.avatar.url
        embed.set_thumbnail(url=icon)
        await channel.send(f"{member.mention}", embed=embed)
    except AttributeError:
        await channel.send(f"{member.mention}", embed=embed)
