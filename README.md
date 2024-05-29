
# Hacker News Summariser

The 'Hacker News' provided by Y Combinator (https://news.ycombinator.com/news) offers a great insight into popular tech articles. However, scrolling through all the articles can be time-consuming. This script queries the top articles (by default 10) and uses Google's Gemini to summarise them into a quick, readable summary.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/marabb01/ycombinator-gemini-summary.git
   cd ycombinator-gemini-summary
   ```

2. **Install the Required Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Generate a Free Google Gemini API Key:**

   You can get a free API key by visiting the following link: [Google Gemini API Key](https://aistudio.google.com/app/apikey)

4. **Update the Configuration:**

   Replace `TOKEN_HERE` with your Google Gemini API key in the configuration file or script.

5. **Run the Script:**

   ```bash
   python summarise_hacker_news.py
   ```

## Configuration

By default, the script queries the top 10 articles. You can adjust this number by modifying the `fetch_top_articles(rss_feed_url)` to include a number `fetch_top_articles(rss_feed_url, 10)`

## Contributing

If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
