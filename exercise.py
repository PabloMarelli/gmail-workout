"""
All exercise files.
"""


class Exercise(object):
    """Object that defines the exercise to be done."""
    
    def __init__(self, name, url):
        """Constructs an Exercise object with a name and url.

        Args:
            name: `string` The name of the exercise.
            url: `string` A url to a video of the exercise to depict proper form.
        """
        self.name = name
        self.url = url
    
    def as_html(self):
        """Formats the exercise as an HTML link."""
        return f"{self.name} (<a ref=\"{self.url}\">example</a>)"

    def __str__(self):
        return self.as_html()


# Exercise definitions
DBShrugs = Exercise(
    "DB shrugs",
    "https://youtube.com/watch?v=g6qbq4Lf1FI")

BarbellShrugs = Exercise(
    "Barbell shrugs",
    "https://youtube.com/watch?v=NAqCVe2mwzM")

FlatDBBenchPress = Exercise(
    "Flat DB bench press (palms in or out)",
    "https://youtube.com/watch?v=omGiL5h2R_I")

InclineDBBenchPress = Exercise(
    "Incline DB bench press (palms in or out)",
    "https://youtube.com/watch?v=0G2_XV7slIg")

DBFloorPress = Exercise(
    "DB floor press (palms in)",
    "https://youtube.com/watch?v=A2dfGvoykPc")

BarbellFloorPress = Exercise(
    "Barbell floor press",
    "https://youtube.com/watch?v=9vYCwtHkWgI")