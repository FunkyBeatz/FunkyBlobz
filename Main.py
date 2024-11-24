import discord
import secrets
import string
from discord.ext import commands
import requests
import random

# Discord bot token
TOKEN = 'MTI5ODc4MzY2MTk2NDkyMjkyMQ.GkV44p.zHf4yWqQWKn52z9qBEG1G9R6TOgSKzqpOzHxEA'

# Giphy API Key
GIPHY_API_KEY = 'KK4T8Kdh06MRrYwPy1Xnox6gn7I442Xz'

# Search queries for GIFs
GM_QUERIES = ["good morning", "morning sunshine", "rise and shine"]
GN_QUERIES = ["good night", "sleep well", "sweet dreams"]
FUNKY_QUERY = "feeling funky"  # Updated to only search for "feeling funky"
BLOB_GIF_URL = "https://gph.is/2Mtt5QL"  # Always return this GIF for !blob

# Predefined text messages
GM_MESSAGES = ["Guuuud morning!", "Rise and shine!", "Morning sunshine!"]
GN_MESSAGES = ["Guuuud night!", "Sweet dreams!", "Time to rest!"]
BLOB_MESSAGES = ["what's up with the Blob?", "Are you blobbing or what?"]  # Updated blob messages
FUNKY_MESSAGE = "Feeling Funky?!"  # Updated funky message

# Create a bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# Function to get a random gif from Giphy
def get_random_gif(query):
    print(f"Fetching GIF for query: {query}")  # Debugging log
    url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=10&rating=g"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gifs = data['data']
        if gifs:
            gif_url = random.choice(gifs)['url']
            print(f"GIF found: {gif_url}")  # Debugging log
            return gif_url
    print("No GIF found")  # Debugging log
    return None


# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Command: !gm
@bot.command()
async def gm(ctx):
    # Send message instantly
    await ctx.send(random.choice(GM_MESSAGES))

    # Fetch and send GIF afterward asynchronously
    gif_url = get_random_gif(random.choice(GM_QUERIES))
    if gif_url:
        await ctx.send(gif_url)


# Command: !gn
@bot.command()
async def gn(ctx):
    # Send message instantly
    await ctx.send(random.choice(GN_MESSAGES))

    # Fetch and send GIF afterward asynchronously
    gif_url = get_random_gif(random.choice(GN_QUERIES))
    if gif_url:
        await ctx.send(gif_url)


# Command: !blob (Always sends the predefined Blob GIF)
@bot.command()
async def blob(ctx):
    # Send random predefined Blob message
    await ctx.send(random.choice(BLOB_MESSAGES))

    # Send the predefined Blob GIF
    await ctx.send(BLOB_GIF_URL)


# Command: !funky (Searches for "feeling funky")
@bot.command()
async def funky(ctx):
    # Send funky message instantly
    await ctx.send(FUNKY_MESSAGE)

    # Fetch and send "feeling funky" GIF asynchronously
    gif_url = get_random_gif(FUNKY_QUERY)
    if gif_url:
        await ctx.send(gif_url)


# Error handler to catch command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found: {ctx.invoked_with}")
    else:
        await ctx.send(f"An error occurred: {str(error)}")





#Custom Activity Playing a game, streaming, watching,...
    
# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    # Set the bot's activity
    activity = discord.Activity(type=discord.ActivityType.feeling, name="Funky")  # Custom game/activity name
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is now showing activity!")

# Replace discord.Game with:

# discord.Game (name="Game Name")  Custom game/activity name

# discord.Streaming (name="Stream Title", url="Twitch URL") for Streaming.

# discord.Activity (type=discord.ActivityType.watching, name="Movie Title") for Watching.

# discord.Activity (type=discord.ActivityType.listening, name="Song Title") for Listening.


# Generate a random secret key

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Slash command to generate a key
@bot.tree.command(name="generate_key", description="Generate a random secure key")
async def generate_key(interaction: discord.Interaction):
    # Generate a random secure key with mixed case and numbers
    characters = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(characters) for _ in range(20))

    # Format the key (6-3-4-8)
    formatted_key = f"{random_key[:6]}-{random_key[6:9]}-{random_key[9:13]}-{random_key[13:21]}"

    # Respond with the key (ephemeral response)
    await interaction.response.send_message(
        content=f"Your secure key: `{formatted_key}`",
        ephemeral=True  # Only visible to the user who invoked the command
    )

# Sync commands with Discord (required for slash commands to work)
@bot.event
async def on_connect():
    try:
        await bot.tree.sync()
        print("Slash commands synced successfully!")
    except Exception as e:
        print(f"Error syncing commands: {e}")














# Run the bot
bot.run('MTI5ODc4MzY2MTk2NDkyMjkyMQ.GkV44p.zHf4yWqQWKn52z9qBEG1G9R6TOgSKzqpOzHxEA')
