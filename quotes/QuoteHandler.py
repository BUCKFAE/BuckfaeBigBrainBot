import csv
from datetime import date, time, datetime

from quotes.Quote import Quote

quote_command_add = "add"


class QuoteHandler:
    def __init__(self):

        self.quotes = []

        with open('data/quotes.csv', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for current_row in csv_reader:
                self.quotes.append(current_row)

    async def handle_quote(self, ctx):
        try:
            command = ctx.content.split(" ")[1]

            if command == quote_command_add:  # Adding a quote

                quote_text = ctx.content.split("\"")[1]  # Quote
                quote_author = ctx.author.name  # Author
                await self.add_quote(quote_text, quote_author, ctx)

            if command.isnumeric():  # Getting a quote with specific id

                # If there is a quote with the given ID
                if int(command) < len(self.quotes):
                    await self.get_quote(int(command), ctx)

                # The quote with the given ID does not exist
                else:
                    await ctx.channel.send("@{}: There is no quote with the ID {}".format(ctx.author.name, command))

        except IndexError:
            print("No command given")

    async def add_quote(self, quote_text, quote_author, ctx):
        self.quotes.append(quote_text)

        with open('data/quotes.csv', mode='a') as csv_file:

            fieldnames = ['Date', 'Time', 'Quote', 'Author']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            current_date = date.today().strftime("%d.%m.%Y")
            current_time = datetime.now().strftime("%H:%M:%S")

            writer.writerow({'Date': current_date, 'Time': current_time, 'Quote': quote_text, 'Author': quote_author})

        await ctx.channel.send("Quote added")

    async def get_quote(self, quote_id, ctx):
        await ctx.channel.send(self.quotes[quote_id])
        print(self.quotes[quote_id])

    def print_quotes(self):
        print(self.quotes)
