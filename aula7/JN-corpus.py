#!/usr/bin/env python3

import newspaper
import os


path = os.getcwd()
print(path)

if not os.path.exists("/tmp/.newspaper_scraper"):
    origem = os.path.join(path,"newspaper")
    os.symlink(origem,"/tmp/.newspaper_scraper")



url = "https://expresso.pt/"

jn = newspaper.build(url)

print(jn.size())



for article in jn.articles:
    #print(article.url,article.title)
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    print(f"""<title>{ar.title}</title>
    <url>{ar.url}</url>
    <authors>{ar.authors}</authors>
    <date>{ar.publish_date}</date>
    {ar.text}
    """)


# por isto de maneira a q crie com algum consenso ficheiros com coisas novas
# fazer com q o corpus vá crescendo
# pasta com o corpus do dia para jornais diarios
