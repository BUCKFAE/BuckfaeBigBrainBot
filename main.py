import os
from datetime import date, datetime

from dotenv import load_dotenv
from twitchio import Client
from twitchio.ext import commands
from twitchio.ext.commands import CommandNotFound

from quotes.QuoteHandler import QuoteHandler

load_dotenv()

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    # Called once when the bot goes online.
    print(f"{os.environ['BOT_NICK']} is online!")


@bot.event
async def event_message(ctx):
    # Runs every time a message is sent in chat.

    # Logs the message
    with open("data/chatlog.txt", "a") as file_object:
        # Append 'hello' at the end of file
        current_date = date.today().strftime("%d.%m.%Y")
        current_time = datetime.now().strftime("%H:%M:%S")
        file_object.write(
            "User: {}\nDate: {}\nTime: {}\nMessage: {}\n\n".format(ctx.author.name, current_date, current_time, ctx.content))
        print("Logged message: {}".format(ctx.content))

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    # Quote
    if ctx.content.lower().startswith("!quote".lower()) \
            or ctx.content.lower().startswith("quote"):
        await ctx.channel.send("Zitate sind WIP!")
        #await quote_handler.handle_quote(ctx)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    quote_handler = QuoteHandler()
    bot.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
