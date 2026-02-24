# Sanremo Festival Discord Bot 🎵

A Discord bot that tracks the status of the Sanremo Music Festival (Festival della Canzone Italiana di Sanremo), one of Italy's most prestigious and longest-running music competitions.

## Features

- **Real-time Festival Status**: Check if the festival is currently happening, hasn't started yet, or has ended
- **Countdown Timer**: See exactly how much time remains until the festival starts or ends
- **Slash Command Interface**: Easy-to-use `/sanremo` command
- **Italian Language Support**: Messages in Italian for an authentic experience

## Installation

### Prerequisites

- Python 3.12 or higher
- pip package manager
- A Discord Bot Token ([create one here](https://discord.com/developers/applications))

### Setup

1. Clone the repository: 
```bash 
git clone https://github.com/yourusername/sanremo_discord_bot.git 
cd sanremo_discord_bot
```
2. Install required dependencies:
```bash 
pip install discord.py requests
```
3. Configure your bot token:
   - Create a `token.env` file in the project root
   - Add your Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_bot_token_here
   ```
4. Run the bot:
```bash
python SanremoFestivalBot.py
```


## Usage

Once the bot is added to your Discord server, use the following command:

- `/sanremo` - Check the current status of the Sanremo Festival

### Example Responses

**Before the festival:**
> 🎤 **Il Festival di Sanremo non è ancora iniziato** 🎤
> 
> Manca: 15 giorni, 8 ore e 30 minuti
> Inizio previsto: 24/02/2026 alle 20:30

**During the festival:**
> 🎵 **Il Festival di Sanremo è IN CORSO!** 🎵
> 
> Tempo rimanente: 2 giorni, 3 ore e 15 minuti

**After the festival:**
> 🎭 **Il Festival di Sanremo è terminato** 🎭
> 
> Tempo trascorso: 5 giorni, 10 ore e 45 minuti
> Concluso il: 28/02/2026 alle 23:59

## Festival Information

The bot is currently configured for the **2026 Sanremo Festival**:
- **Start**: February 10, 2026 at 20:30
- **End**: February 14, 2026 at 23:59

To update dates for future editions, modify the `SANREMO_2026_START` and `SANREMO_2026_END` constants in `SanremoFestivalBot.py`.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- Built with [discord.py](https://github.com/Rapptz/discord.py)
- Inspired by the legendary Sanremo Music Festival 🎶