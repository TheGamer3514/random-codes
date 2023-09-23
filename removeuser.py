#Discord.py command that removes a user from all threads in channel
@bot.command()
async def removeuser(ctx, user: discord.Member):
    count = 0
    if ctx.message.author.id == 763471049894527006: #put your id here
        channel = bot.get_channel(1006122978842517534) #put the channel id here
        for thread in channel.threads:
            await thread.remove_user(user)
            count += 1
        embed = discord.Embed(
            title="**Silly Development**",
            description=f"Removed {user} From {count} Tickets",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
