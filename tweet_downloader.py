###############################################################################
#
# tweet_downloader.py
#
# Natalie Parde
# natalie.parde@unt.edu
#
# Reads in a list of tweet IDs and downloads each tweet.  Stores the tweet
# text, along with some other potentially useful metadata, in a CSV file.
#
###############################################################################

import csv
import argparse
from twython import Twython, TwythonError

class TweetDownloader:

   # Reads in the document containing the tweet IDs and stores the IDs
   # in a list.
   def read_ids(self, id_file_name):
      self.ids = []
      id_file = open(id_file_name)
      for line in id_file:
         self.ids.append(line.strip())  # Strip newline from end of ID.
      id_file.close()

   # Downloads each tweet ID in the list of IDs, and writes it (along with some
   # metadata) to a file.
   def download_tweets(self, app_key, app_secret, oauth_token, oauth_token_secret):
      try:
         twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

         tweet_file = open("tweet_dataset.csv", "w")
         writer = csv.writer(tweet_file, quotechar='|')  # Cells containing commas will be surrounded by | characters.
         writer.writerow(["ID", "Tweet", "User", "Creation Date"])
         for tweet_id in self.ids:
            try:
               tweet = twitter.show_status(id=tweet_id)
               tweet_text = " ".join(tweet['text'].split())  # All whitespace contained in the tweet is normalized.
               writer.writerow([tweet[id_str], tweet_text, tweet['user']['screen_name'], tweet['created_at']])
            except TwythonError as e2:
               print e2
         tweet_file.close()
      except TwythonError as e:
         print e

   # Get command-line parameters and run the program.
   def Main(self):
      parser = argparse.ArgumentParser(description="Downloads the tweets associated with an input list of tweet IDs.")
      parser.add_argument("--app_key", type=str, help="Your Twitter consumer key.")
      parser.add_argument("--app_secret", type=str, help="Your Twitter consumer secret.")
      parser.add_argument("--oauth_key", type=str, help="Your Twitter access token.")
      parser.add_argument("--oauth_secret", type=str, help="Your Twitter access token secret.")
      parser.add_argument("--id_file", type=str, help="The name of the file containing the tweet IDs.  IDs should be listed one per line, with no header line.")
      args = parser.parse_args()

      # Check for errors.
      if args.app_key == None:
         parser.error("Please specify your Twitter consumer key as follows: --app_key <consumer key>")
      if args.app_secret == None:
         parser.error("Please specify your Twitter consumer secret as follows: --app_secret <consumer secret>")
      if args.oauth_key == None:
         parser.error("Please specify your Twitter access token as follows: --oauth_key <access token>")
      if args.oauth_secret == None:
         parser.error("Please specify your Twitter access token secret as follows: --oauth_secret <access token secret>")
      if args.id_file == None:
         parser.error("Please specify your tweet ID file as follows: --id_file <name of tweet ID file>")

      # Run the program.
      self.read_ids(args.id_file)
      self.download_tweets(args.app_key, args.app_secret, args.oauth_key, args.oauth_secret)

if __name__ == "__main__":
   tweet_downloader = TweetDownloader()
   tweet_downloader.Main()
