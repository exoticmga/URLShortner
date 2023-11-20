import pyshorteners
import requests

# Get API key from your chosen URL shortening service
api_key = "YOUR_API_KEY"

# Create an instance of the URL shortener
s = pyshorteners.Shortener(api_key=api_key)

# Get the URL to shorten from the user
url = input("Enter the URL to shorten: ")

# Shorten the URL
short_url = s.shorten(url)

# Print the shortened URL
print("Shortened URL:", short_url)

# Expand the shortened URL
expanded_url = requests.get(short_url).url

# Print the original URL
print("Original URL:", expanded_url)
