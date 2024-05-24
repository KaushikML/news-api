import requests
from Send_email import  send_email
api="d491223464864fc68a9bb827ae675785"
topic="tesla"
url="https://newsapi.org/v2/everything?" \
    f"q={topic}&from=2024-04-24&sortBy=publishedAt&" \
    "apiKey=d491223464864fc68a9bb827ae675785&" \
    "language=en"
request=requests.get(url)
content=request.json()

body=" "
for article in content["articles"][:20]:
    if article["title"] is not None:
        body ="Subject: NEWS "+"\n"+ body + article["title"]   + "\n" + article["description"] + article["url"] + 2 * "\n"


body=body.encode("utf-8")
send_email(message=body)

