import requests
from Send_email import send_email

api_key = "d491223464864fc68a9bb827ae675785"  # Use a variable for clarity
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-04-24&sortBy=publishedAt&apiKey={api_key}&language=en"

# Send request and get JSON content
response = requests.get(url)
content = response.json()

# Close the response object (recommended)
response.close()

body = "Subject: NEWS\n\n"  # Set subject line once

for article in content["articles"][:20]:
  if article["title"] is not None:
    body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"  # Use f-string for concatenation

# Send email with the formatted body
send_email(message=body.encode("utf-8") if not isinstance(body, bytes) else body)  # Encode only if not already bytes
