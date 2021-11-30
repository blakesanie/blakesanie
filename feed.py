import feedparser

NewsFeed = feedparser.parse(
    "https://medium.com/feed/@blakesanie")

articles = sorted(NewsFeed.entries, key=lambda x: x['published_parsed'])[:5]

html = ""

for article in articles:
    html += f"<li><a href='{article['link']} target='_blank'>{article['title']}</a></li>"

html = '<ul>' + html + '</ul>'

readme = open("readme.md")
content = readme.read()
readme.close()

startMarker = '<!--Start Medium-->'
endMarker = '<!--End Medium-->'

content = content[:content.index(
    startMarker) + len(startMarker)] + html + content[content.index(endMarker):]

readme = open("readme.md", 'w')
readme.write(content)
readme.close()
