key = str(input())

url = "https://en.wikipedia.org/wiki/{}".format(key)
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")
contents = ""
link = ""
words = dict()

for content in bsObject.find_all('p'):
    contents += content.text.strip()

for word in contents:
  if word == ' ':
    try:
      words[link] += 1
    except:
      words[link] = 1
    link = ""
  else:
    if word not in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', "'", '"', ',', '.', '?']:
      link += word

print("WORD FREQUENCY: {}".format(str(words)))
print("SUMMARIZATION: {}".format(list(summarizer(contents, max_length=5000, min_length=30, do_sample=False)[0].values())[0]))
