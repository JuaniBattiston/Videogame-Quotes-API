# Videogame Quotes API

**A cool API to retrieve random videogame quotes**

```py
import requests

request = requests.get("http://localhost:8000/quotes")
content = request.json()

print(content["quote"])  # 'FINISH HIM!'
print(content["game"])  # 'Mortal Kombat'
```

*(Find more ideas in
[`/examples`](https://github.com/Batucho/Videogame-Quotes-API/tree/main/examples)!)*

## Testing the API endpoints
Videogame Quotes API is now being hosted!
Check the docs and test the endpoints [here](https://videogame-quotes-api.herokuapp.com/docs).

## Running the API locally

Note: Python 3.9 or higher is recommended.

1. Clone the repository.
   ```sh
   $ git clone https://github.com/Batucho/Videogame-Quotes-API
   ```
2. Install the dependencies.
   ```sh
   $ pip install -r requirements.txt
   ```
3. Run the API!
   ```sh
   $ python src/__main__.py
   ```
4. Check it out at [`localhost:8000`](http://localhost:8000) or
   [`127.0.0.1:8000`](http://127.0.0.1:8000).

Feel free to contribute by opening an issue or pull request!

## Disclaimer

This project is for educational purposes only. The maintainers and contributors
of this project claim no ownership or credit for the quotes listed.

## Sources

Quotes have been retieved from the following sources:

-
  [The Top 100 Video Game Quotes of All Time -  Bryan Wirtz](https://www.gamedesigning.org/gaming/video-game-quotes/)
-
  [Top 101 Inspirational Video Game Quotes All Young Gamers Should Read](https://kidadl.com/articles/top-inspirational-video-game-quotes-all-young-gamers-should-read)
-
  [Random Video Game Quote Generator](https://codepen.io/AlexDr7/pen/LyOEBv)
-
  [The 100 best video game quotes of all time (Up to page 5)](https://www.gamesradar.com/au/best-video-game-quotes-all-time)
