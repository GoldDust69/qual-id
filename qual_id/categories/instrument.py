from ..category import Category


class Instrument(Category):
    def get_values(self):
        return [
            "banjo",
            "bass",
            "cello",
            "drumkit",
            "guitar",
            "harp",
            "organ",
            "piano",
            "ukelele",
            "violin",
        ]
