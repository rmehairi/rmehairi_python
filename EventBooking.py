class Artwork:
    """Artwork class"""
    def __init__(self, title, artist, dateOfCreation, historicalSignificance):
        # Initializing the attributes
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance

    def __str__(self):
        return f"Artwork: {self.title} by {self.artist}, created on {self.dateOfCreation}, significance: {self.historicalSignificance}"
    # Getters and Setters
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_dateOfCreation(self):
        return self.dateOfCreation

    def set_dateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

    def get_historicalSignificance(self):
        return self.historicalSignificance

    def set_historicalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance
