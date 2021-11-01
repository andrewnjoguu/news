# virtual environment first

#let us import flask 
from flask import Flask, render_template

from newsapi import NewsApiClient





app = Flask(__name__)

#route function as we render html
@app.route('/')
def home():

    newsapi = NewsApiClient(api_key="cf3fc3965f40483f84312fb87de9435b")

  #for the top headlines of news we will code:
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')
    #the main articles ,
    all_articles = newsapi.get_everything(sources='bbc-news')

  # source is meant by where news comes into app by api

 #fetch all articles
    t_articles = top_headlines['articles']
    #fetch all articles
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #let us fetch contents using for loop
    for i in range(len(t_articles)):
        main_aricle = t_articles[i]

    #add articles of each list 
        news.append(main_aricle['title'])
        desc.append(main_aricle['description'])
        img.append(main_aricle['urlToImage'])
        p_date.append(main_aricle['publishedAt'])
        url.append(main_aricle['url'])

    news_all = []
    desc_all =[]
    img_all =[]
    p_date_all = []
    url_all = []
    #loop for all articles
    for i in range(len(a_articles)):
        a_articles = a_articles[i]

    

        #zip made to find contents directly
        contents = zip(news,desc,img,p_date,url)


    return render_template('home.html', contents=contents)
 


if __name__ =='__main__':
    app.run(debug=True)