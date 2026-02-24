import discord
from discord import app_commands
from datetime import datetime, timedelta
import os

# Install required packages:
# pip install discord.py

# Sanremo Festival 2026 edition
# Dates: February 24-28, 2026
SANREMO_2026_START = datetime(2026, 2, 24, 20, 30)  # Evening start 
SANREMO_2026_END = datetime(2026, 2, 28, 23, 59)

class SanremoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands with Discord
        await self.tree.sync()
        print("Commands synced!")

# Initialize bot
bot = SanremoBot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

@bot.tree.command(name="sanremo", description="Check the status of the Sanremo Festival")
async def sanremo(interaction: discord.Interaction):
    """Responds with information about the Sanremo Festival"""
    
    now = datetime.now()
    
    # Check if the festival is currently happening
    if SANREMO_2026_START <= now <= SANREMO_2026_END:
        # Festival is currently on
        time_remaining = SANREMO_2026_END - now
        days = time_remaining.days
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        
        message = f"🎵 **Il Festival di Sanremo è IN CORSO!** 🎵\n\n"
        message += f"Tempo rimanente: {days} giorni, {hours} ore e {minutes} minuti"
        
    elif now < SANREMO_2026_START:
        # Festival hasn't started yet
        time_until = SANREMO_2026_START - now
        days = time_until.days
        hours = time_until.seconds // 3600
        minutes = (time_until.seconds % 3600) // 60
        
        message = f"🎤 **Il Festival di Sanremo non è ancora iniziato** 🎤\n\n"
        message += f"Manca: {days} giorni, {hours} ore e {minutes} minuti\n"
        message += f"Inizio previsto: {SANREMO_2026_START.strftime('%d/%m/%Y alle %H:%M')}"
        
    else:
        # Festival has ended
        time_since = now - SANREMO_2026_END
        days = time_since.days
        hours = time_since.seconds // 3600
        minutes = (time_since.seconds % 3600) // 60
        
        message = f"🎭 **Il Festival di Sanremo è terminato** 🎭\n\n"
        message += f"Tempo trascorso: {days} giorni, {hours} ore e {minutes} minuti\n"
        message += f"Concluso il: {SANREMO_2026_END.strftime('%d/%m/%Y alle %H:%M')}"
    
    await interaction.response.send_message(message)

def load_token_from_file(filename='token.env'):
    """Load Discord bot token from environment file."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if key.strip() == 'DISCORD_BOT_TOKEN':
                        token = value.strip()
                        if token and token != 'your_bot_token_here':
                            return token
        return None
    except FileNotFoundError:
        with open(filename, 'w') as f:
            f.write('DISCORD_BOT_TOKEN=your_bot_token_here\n')
        print(f"Created {filename} file. Please set your Discord bot token.")
        return None
    except Exception as e:
        print(f"Error reading token file: {e}")
        return None


# Run the bot
if __name__ == "__main__":
    TOKEN = load_token_from_file()

    if not TOKEN:
        print("Error: DISCORD_BOT_TOKEN not found or not set in token.env!")
        print("Please set your Discord bot token in the token.env file.")
        exit(1)

    bot.run(TOKEN)