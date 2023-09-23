#Discord.py suggestion command
@bot.tree.command(name="suggest", description="Suggest a feature!")
async def slashreport(interaction, suggestion: str):
    await interaction.response.defer()
    channelid = bot.get_channel(int(123456789))
    successembed = discord.Embed(description="Suggestion Submitted!",color=0x2ecc71)
    suggestembed = discord.Embed(title="New Suggestion!",description=f"**Submitter**\n{interaction.user} [{interaction.user.id}]\n**Suggestion**\n{suggestion}",color=discord.Colour.blurple())
    suggestembed.timestamp = datetime.utcnow()
    suggestembed.set_thumbnail(url=interaction.user.avatar.url)
    await interaction.followup.send(embed=successembed)
    msg = await channelid.send(embed=suggestembed)
    await msg.add_reaction("⬆️")
    await msg.add_reaction("⬇️")
