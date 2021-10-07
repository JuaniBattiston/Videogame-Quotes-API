# Videogame quotes API

A simle API project to retrieve videogame quotes.

# How to run the API on your localhost

**Python 3.9 or higher is recommended**
```
$ pip install -r requirements.txt
$ python src/__main__.py
```
Clone repository:
```
$ git clone https://github.com/Batucho/Videogame-Quotes-API
```

# Request Examples

### Retrieve one random quote
```py
import requests

# Base url for localhost
base_url =  "http://127.0.0.1:8000/quotes"

request = requests.get(base_url)
req_content = request.json()
  
print(req_content)
print(req_content["quote"])
print(req_content["game"])
```

### [More examples here!](https://github.com/Batucho/Videogame-Quotes-API/tree/main/examples/)

# ⚠ Disclaimer ⚠

### This project is for educational purposes only. The sources from which the information was extracted will be attached here:

+ #####  [The Top 100 Video Game Quotes of All Time -  Bryan Wirtz](https://www.gamedesigning.org/gaming/video-game-quotes/)
+ #####  [Top 101 Inspirational Video Game Quotes All Young Gamers Should Read](https://kidadl.com/articles/top-inspirational-video-game-quotes-all-young-gamers-should-read)

**Feel free to contribute to the project by opening an issue!**
