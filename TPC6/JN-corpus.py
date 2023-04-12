#!/usr/bin/env python3

# o import cria a pasta /tmp/.newspaper_scraper
import newspaper
import os
import datetime
import re

path = os.getcwd()
print(path)

url = "https://expresso.pt/"

jn = newspaper.build(url)

print(jn.size())

corpus = {}
erros = []
for article in jn.articles:
    #print(article.url,article.title)
    ar = newspaper.Article(article.url)
    ar.download()
    try:
        ar.parse()

        if type(ar.publish_date) == datetime.datetime:
            ar.publish_date = ar.publish_date.strftime("%Y_%m_%d")
        elif ar.publish_date is None:
            ar.publish_date = "Unknown" 
        elif re.search(r"\d{4}-\d{2}-\d{2}", ar.publish_date):
            match = re.match(r"(\d{4}-\d{2}-\d{2})", ar.publish_date)
            ar.publish_date = match.group(1).replace("-","_")

        if not os.path.exists(f"{path}/corpus/{ar.publish_date}"):
            os.makedirs(f"{path}/corpus/{ar.publish_date}")

        ar.title = ar.title.replace("/","_")
        with open(f"{path}/corpus/{ar.publish_date}/{ar.title}.txt", "w") as f:
            text = f"""<title>{ar.title}</title>
            <url>{ar.url}</url>
            <authors>{ar.authors}</authors>
            {ar.text}
            """
            if ar.publish_date in corpus.keys():
                corpus[ar.publish_date] += "\n" + ar.text
            else:
                corpus[ar.publish_date] = ar.text
            f.write(text)
    except Exception as e:
        print(e," : ", article.url, article.title)
        erros.append((article.url, article.title))
        continue
    
for date in corpus.keys():
    if os.path.exists(f"{path}/corpus/{date}/.corpus.txt"):    
        with open(f"{path}/corpus/{date}/.corpus.txt", "a") as f:
            f.write(corpus[date])
    else:
        with open(f"{path}/corpus/{date}/.corpus.txt", "w") as f:
            f.write(corpus[date])

with open(f"{path}/corpus/.erros.txt", "w") as f:
    for url,titulo in erros:
        f.write(f"{url} - {titulo}\n")
    
# por isto de maneira a q crie com algum consenso ficheiros com coisas novas
# fazer com q o corpus vá crescendo
# pasta com o corpus do dia para jornais diarios
