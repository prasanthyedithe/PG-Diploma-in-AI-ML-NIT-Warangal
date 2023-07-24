import streamlit as st
# import SessionState
import streamlit.components.v1 as components
import pandas as pd
import tweepy
import time
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import plotly.express as px
import plotly.graph_objects as go
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re
import matplotlib.pyplot as plt
from matplotlib.cm import Reds, Greens, Purples, Greys
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import mdpAuth as auth
st.session_state['bearer_token'] = auth.BEARER_TOKEN
st.session_state['api_key']=auth.API_KEY
st.session_state['api_secret']=auth.API_SECRET
st.session_state['access_token']=auth.ACCESS_TOKEN
st.session_state['access_secret']=auth.ACCESS_TOKEN_SECRET

################################################################################################### Functions
stop = stopwords.words('english')
# Setup access to API
def connect_to_twitter_OAuth(api_key,api_secret,access_token,access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

def rejoin_words(row):
    my_list = row['tidy_tweet']
    joined_words = ( " ".join(my_list))
    return joined_words


def lemmatize_text(text):
    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]


def hashtag_extract(x):
    hashtags = []
    ht = re.findall(r"#(\w+)", x)
    hashtags.extend(ht)
    if hashtags==[]:
        return ''
    return hashtags

def word_cloud(wd_list,color):
    fig=plt.figure(figsize=(7,8))
    ax=fig.add_axes([0,0,1,1])
    stopwords = set(STOPWORDS)
    all_words = ' '.join([text for text in wd_list])
    wordcloud = WordCloud(max_font_size=None,stopwords=stopwords, background_color='#fcf4ee', collocations=False,colormap =color,
                  width=750, height=750).generate(all_words)
    ax.imshow(wordcloud)
    
    
    ax.set_axis_off()
    st.pyplot(fig)


# Side Bar comfiguration
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    )

pages=['Get Data','EDA','Analysis']
st.sidebar.title('Crypto Currency Sentiment Analysis')
out=st.sidebar.radio('Page:',pages)

if out=='Get Data':
    try:
       
        api = connect_to_twitter_OAuth(st.session_state['api_key'],st.session_state['api_secret'],
                                        st.session_state['access_token'],st.session_state['access_secret'])
    except:
        st.info('The provided API data was incorrect')
    crypto_list_def=['@ethereum','@litecoin','@Tether_to','@dogecoin','@Polkadot','@btc']
    crypto_list=st.text_input('Input crypto user handles(Separated by space)',value=' '.join(crypto_list_def))
    crypto_list=crypto_list.split(' ')
    if st.button('Fetch'):
        # Array to hold tweet data
        tweet_list = []
        # Iterate through all the crypto_list
        with st.spinner('Getting Tweets'):
            for crypto in crypto_list:
                # Bring out the 200 tweets
                crypto_tweets = api.user_timeline(screen_name=crypto, count=10)
                time.sleep(1)
                # Loop through the 10 tweets
                for tweet in crypto_tweets:
                    tweet_id = tweet.id # unique integer identifier for tweet
                    text = tweet.text # utf-8 text of tweet
                    favorite_count = tweet.favorite_count
                    retweet_count = tweet.retweet_count
                    created_at = tweet.created_at # utc time tweet created
                    source = tweet.source # utility used to post tweet
                    reply_to_status = tweet.in_reply_to_status_id # if reply int of orginal tweet id
                    reply_to_user = tweet.in_reply_to_screen_name # if reply original tweetes screenname
                    retweets = tweet.retweet_count # number of times this tweet retweeted
                    favorites = tweet.favorite_count # number of time this tweet liked
                    # append attributes to list
                    tweet_list.append({'crypto':crypto,
                                    'tweet_id':tweet_id, 
                                    'text':text, 
                                    'favorite_count':favorite_count,
                                    'retweet_count':retweet_count,
                                    'created_at':created_at, 
                                    'source':source, 
                                    'reply_to_status':reply_to_status, 
                                    'reply_to_user':reply_to_user,
                                    'retweets':retweets,
                                    'favorites':favorites})
            tweet_data=pd.DataFrame(tweet_list)
            tweet_data.to_csv('Tweets.csv',index=None)
        st.success('Data Successfully retrieved')


elif out=='EDA':
    data=pd.read_csv('Tweets.csv')
    source=data.source.value_counts()
    trace=go.Pie(labels=source.index,values=source,showlegend=False,hole=0.33,text=[str(round(i*100,3))+'%' for i in source/sum(source)],hovertext='Source',
                hoverinfo='label+text',textinfo='text+label'
                )
    layout=go.Layout(title="Which Device People are using?")
    fig=go.Figure(data=[trace],layout=layout)
    st.plotly_chart(fig)
    source=data.groupby('crypto').agg(sum)[['retweet_count','favorite_count']]
    fig=go.Figure()
    fig.add_bar(x=source.index,y=source.retweet_count,name='Retweet Count')
    fig.add_bar(x=source.index,y=source.favorite_count,name='Favorite Count')
    st.plotly_chart(fig)

elif out=='Analysis':
    with st.spinner('Cleaning the data...'):
        data=pd.read_csv('Tweets.csv')
        data['tidy_tweet'] = data['text'].replace(to_replace ='(@[\w]+)', value ='', regex = True) 
        data['tidy_tweet'] = data['tidy_tweet'].replace(to_replace =('RT'), value ='',regex = True) 
        data['tidy_tweet'] = data['tidy_tweet'].str.replace('((www\.[\s]+)|(https?://[^\s]+))','\0',regex=True)
        data['tidy_tweet'] = data['tidy_tweet'].str.replace("[^a-zA-Z]+", " ")
        data["tidy_tweet"] = data["tidy_tweet"].str.lower()
        data["tidy_tweet"] = data["tidy_tweet"].str.split()
        data['tidy_tweet']=data['tidy_tweet'].apply(lambda x: [item for item in x if item not in stop]) 
        data['tidy_tweet'] = data.apply(rejoin_words, axis=1)
        data['tidy_tweet'] = data['tidy_tweet'].apply(lemmatize_text)
        data['tidy_tweet'] = data.apply(rejoin_words, axis=1)
        analyzer = SentimentIntensityAnalyzer()
        out={'neg':[],'neu':[],'pos':[],'compound':[]}
        for i in range(data.shape[0]):
            vader_out=analyzer.polarity_scores(data.tidy_tweet[i])
            for key in vader_out.keys():
                out[key].append(vader_out[key])
        for key in out.keys():
            data[key]=out[key]
        source=data.groupby('crypto').agg('mean')
    fig=go.Figure()
    for crypto in data.crypto.unique():
        fig.add_bar(x=['Negative','Neutral','Positive','Compound'],y=list(source[source.index==crypto][out.keys()].values[0]),name=crypto)
    fig.update_layout(title='Average Sentiment Across type of cryptocurrencies')
    st.plotly_chart(fig)

#    for key in out.keys():
#        pos_tags = data['text'][data[key]>0.2].apply(hashtag_extract)
#        sentiment_tags=[]
#        for tag in pos_tags:
#            if tag!='':
#               sentiment_tags.extend(tag)
#        color={'neg':Reds,'pos':Greens,'neu':Greys,'compound':Purples}
#        word_cloud(sentiment_tags,color[key])