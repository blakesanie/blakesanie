import tweepy
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

bearer = os.getenv('TWITTER_BEARER_TOKEN')

print('bearer is', bearer)

client = tweepy.Client(
    bearer_token=bearer)

tweets = client.get_users_tweets(
    id=1440382840273731598, tweet_fields=['created_at'], max_results=5)

html = ""

for tweet in tweets.data:
    text = tweet.text
    date = tweet.created_at.strftime('%m/%d/%Y')
    link = 'https://twitter.com/BlakeSanie/status/' + str(tweet.id)
    html += f"""<li><a href='{link}' target='_blank'>{text} - {date}</a></li>
"""

html = f"""<ul>

{html}
</ul>

"""

readme = open("./README.md")
content = readme.read()
readme.close()

startMarker = '<!--Start Twitter-->'
endMarker = '<!--End Twitter-->'

content = content[:content.index(
    startMarker) + len(startMarker)] + html + content[content.index(endMarker):]

print('new content is', content)

readme = open("./README.md", 'w')
readme.write(content)
readme.close()
