import requests
from io import BytesIO
from PIL import Image

address_url = 'https://api.nasa.gov/planetary/apod?api_key=y5OyvRNFG94IQDiaxZujsubAK7AGihFMctb3WJGp'
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
        self.picture = requests.get(self.data['url'])
        self.date = self.data['date']
        self.explanation = self.data['explanation']
        self.title = self.data['title']


cosmos = AstronomyPicture(address_url)
print(cosmos.data)
