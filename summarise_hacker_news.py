import feedparser
import google.generativeai as gemini
import os

# !!! Set your API key for Google Generative AI
os.environ["GOOGLE_API_KEY"] = "TOKEN_HERE"

gemini.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Function to fetch top (default 10) articles from Hacker News RSS feed
def fetch_top_articles(feed_url, top_n=10):
    feed = feedparser.parse(feed_url)
    articles = feed.entries[:top_n]
    return articles

# Function to summarise multiple articles using Google Generative AI
def summarise_articles(articles):
    prompt = "Summarise the key points of the following articles and include the links in the response. Format the summary to be included in an email. Don't include any greetings:\n\n"
    for article in articles:
        prompt += f"Title: {article.title}\nLink: {article.link}\n\n"
    
    response = gemini.generate_text(prompt=prompt)
    summary = response.result
    return summary

if __name__ == "__main__":
    rss_feed_url = "https://news.ycombinator.com/rss"

    articles = fetch_top_articles(rss_feed_url)

    summary = summarise_articles(articles)
    print(f"Summary:\n{summary}")
