# tweet-downloader

This repository contains a simple script (tweet_downloader.py) that can be used to download the tweets included in Parde and Nielsen's (2017) Twitter dataset for sarcasm detection (it can also be used to download any other tweets for which you have IDs).

The script depends on the Twython Twitter library.  More information, and the source code for this library, can be found here: https://github.com/ryanmcgrath/twython

To install Twython, type:
pip install twython

or:
easy_install twython

(If you'd rather build it from source, see the link above.)

To run tweet_downloader.py, you'll need to generate several keys using Twitter.  To do this:
1) Log into your Twitter account, and go to apps.twitter.com.
2) Click "Create a New App" and fill out the application details.
3) Enter the page for your app and click on the tab titled "Keys and Access Tokens."
4) Generate the following or, if they're already generated, take note of their values:
   - Consumer Key
   - Consumer Secret
   - Access Token
   - Access Token Secret

Once you have these values, you should be able to run tweet_downloader.py.  The script accepts the keys and tokens as command arguments.  You can view a description of each argument by typing:
python tweet_downloader.py -h 

To run tweet_downloader.py, type:
python tweet_downloader --app_key <your consumer key> --app_secret <your consumer secret> --oauth_key <your access token> --oauth_secret <your access token secret> --id_file <the name of the file containing your tweet IDs>

The program will print an error message if it is unable to connect to Twitter, or unable to download a tweet.  It will write all downloaded tweets to a CSV file titled "tweet_dataset.csv."  Columns in the CSV file include the tweet ID, the tweet text, the user who created the tweet, and the tweet's creation date.

If you use the tweets in this dataset for your own research, please cite the following paper:

Natalie Parde and Rodney D. Nielsen. #SarcasmDetection is soooo general! Towards a Domain-Independent Approach for Detecting Sarcasm. In the Proceedings of the 30th International FLAIRS Conference. Marco Island, Florida, May 22-24, 2017.
