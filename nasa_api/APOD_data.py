import requests

address_url = 'https://api.nasa.gov/planetary/apod?api_key=y5OyvRNFG94IQDiaxZujsubAK7AGihFMctb3WJGp'


class AstronomyPicture:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.picture = self.data['url']
        self.date = self.data['date']
        self.explanation = self.data['explanation']
        self.title = self.data['title']


cosmos = AstronomyPicture(address_url)

print(cosmos.picture)
print(cosmos.title)
