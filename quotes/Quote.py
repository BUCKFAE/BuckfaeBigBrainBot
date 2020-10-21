class Quote:
    def __init__(self, date, time, text, author, approved):
        self.date = date
        self.time = time
        self.text = text
        self.author = author
        self.approved = approved

    def to_csv_string(self):
        return ""

    def to_string(self):
        return "{} ({} {}, hinzugefügt von {})" \
            .format(self.text, self.time, self.date, self.author)


def get_quote_from_csv_string(csv_string):
    split = str(csv_string).split(",")

    date = split[0]
    time = split[1]
    text = split[2]
    author = split[3]
    approved = split[4]

    return Quote(date, time, text, author, approved)



