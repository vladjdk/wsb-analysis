# WallStreetBets Analysis

With recent news, it became evident that Reddit's r/WallStreetBets is a sentimental market powerhouse. They hold massive influence, to the point where the mainstream media is quoting their memes. Their recent plays with GME caused a huge interest from the media, even causing people outside of trading in general to become interested in what's going on. The events didn't all unfold overnight, though. The surge in price was a result of months of planning and discussion on the forums. It is no doubt that WSB has at least some influence in major market movements. Trends take a while to appear, so catching them before they make a loud noise is crucial. This project aims to do just that. Catch the future trending stock before it surges, by catching the noise it makes in the subreddit.

## Plans

Here are the elements that are necessary for the analysis.

- [ ] WSB Subreddit post scraper
- [ ] Data cleaner and preprocessor
- [ ] Token extractor for tickers that each post talks about
- [ ] Sentiment analyzer for posts (how positive is this post's sentiment surrounding the mentioned stock?)
- [ ] Data and trend visualizer for occurrence of ticker mentions
- [ ] Determine metrics needed for impactful analysis
- [ ] Predictor for future trends based off of past events

## Getting Started

To get started, install the dependencies in `requirements.txt`. You will need a [CoinMarketCap](https://pro.coinmarketcap.com/) API key and a [registered Reddit app](https://www.reddit.com/prefs/apps/). Finally, create a file called `config.yaml` with the following structure:
```YAML
# CoinMarketCap
coinmarketcap:
  api_key: your-api-key

# Reddit
reddit:
  user: your-username
  password: your-password
  client_id: reddit-client-id
  client_secret: reddit-client-secret
  user_agent: reddit-user-agent
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
