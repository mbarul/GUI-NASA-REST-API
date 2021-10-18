import requests

queryUrl = 'https://api.nasa.gov/planetary/apod?'
queryKey = 'api_key=y5OyvRNFG94IQDiaxZujsubAK7AGihFMctb3WJGp'
queryDate = f'&date=2020-07-28&'

queryFull = queryUrl + queryKey + queryDate

title = 'Astronomy Picture of Day'


class AstronomyPicture:
    """
    A class to get data from NASA API.
    Astronomy picture of day

    Attributes
    ----------
    url : str
        url address of REST API

    Methods
    ----------
    .
    """

    def __init__(self, url):
        """
        Constructs all the necessary attributes for the Astronomy Picture object.

        Parameters
        ----------
            url : str
                url address of REST API

        """
        self.data = requests.get(url).json()
        self.picture = requests.get(self.data['hdurl'])
        self.date = self.data['date']
        self.explanation = self.data['explanation']
        self.title = self.data['title']


cosmos = AstronomyPicture(queryFull)
print(cosmos.data)
