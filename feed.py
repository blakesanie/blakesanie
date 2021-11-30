import feedparser
import time

NewsFeed = feedparser.parse(
    "https://medium.com/feed/@blakesanie")

articles = sorted(NewsFeed.entries,
                  key=lambda x: x['published_parsed'], reverse=True)[:5]

html = ""

for article in articles:
    print(article)
    html += f"<li><a href='{article['link']} target='_blank'>{article['title']} - {time.strftime('%m/%d/%Y', article['published_parsed'])}</a></li>"

html = '<ul>' + html + '</ul>'

readme = open("./README.md")
content = readme.read()
readme.close()

startMarker = '<!--Start Medium-->'
endMarker = '<!--End Medium-->'

content = content[:content.index(
    startMarker) + len(startMarker)] + html + content[content.index(endMarker):]

print('new content is', content)

readme = open("./README.md", 'w')
readme.write(content)
readme.close()
