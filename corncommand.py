#Discord.py command that generates an image of corn
@bot.command()
async def corn(ctx):
    ACCESS_KEY = "get key: https://unsplash.com/developers"
    query = 'corn on the cob'
    url = f'https://api.unsplash.com/search/photos/?query={query}'
    headers = {
        'Authorization': f'Client-ID {ACCESS_KEY}'
    }
 
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            results = data['results']
            if results:
                num_results = len(results)
                random_index = random.randint(0, num_results - 1)
                random_image = results[random_index]['urls']['regular']
                embed = discord.Embed(title="Corn", description="An image of corn", color=discord.colour.Color.yellow())
                embed.set_image(url=random_image)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No corn images found.")
        else:
            await ctx.send(f"Error: {response.status_code} - {response.text}")
 
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
