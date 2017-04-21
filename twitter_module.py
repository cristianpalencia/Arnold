"""
Quickie Media - Twitter (Arnold 2.0)
"""

from __future__ import print_function
import twitter
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz

# generate user OAuth tokens for here

api = twitter.Api(consumer_key="8QYsyQt5angTTjQQcYJvYj5po",
                  consumer_secret="QPRwTUN9tNWMWISq91IUMHDGpErG257whhJJFnbunh85MSkOYC",
                  access_token_key="15213778-ac5w2shqIn34BRFTSBHeYdbn8GtSXogkcNsvlMtXv",
                  access_token_secret="vipRgHNCqtCU6NrAJ1pqpf0pfusVHoUQoRXA9EucGFNKY")


def convert_time(datestring):
    timestamp = mktime_tz(parsedate_tz(datestring))
    s = str(datetime.fromtimestamp(timestamp))
    return s


def print_timeline(status):
    # modifies header length based on screen_name length
    dash = ""
    for i in range(0, len(status.user.screen_name)):
        dash = dash + "-"

    # print(status)
    print("\n--------------------------------------------------" + str(dash))
    print(status.user.screen_name, "| ", end="")
    print(convert_time(status.created_at), "| ", end="")
    print("Likes:", status.favorite_count, "| ", end="")
    print("Retweets:", status.retweet_count, "| ")
    print("--------------------------------------------------" + str(dash))
    print(status.text)
    print("--------------------------------------------------" + str(dash))


def get_timeline():
    data = api.GetHomeTimeline(count=3)
    for status in data:
        print_timeline(status)


if __name__ == "__main__":
    get_timeline()
