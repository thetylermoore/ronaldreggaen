from twitter import *
import random

access_token = "redacted"
access_token_secret = "redacted"
consumer_key = "redacted"
consumer_secret = "redacted"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

marley = ['Jah',
          'Herb',
          'Zion',
          'Love',
          'Rastafari',
          'Riddim',
          'Judah',
          'Jamaica',
          'Babylon',
          'Promised Land',
          'Heaven',
          'Earth',
          'Tribes']

reagan0_1 = " is not absense of "
reagan0_2 = ", it is the ability to handle "
reagan0_3 = " by means of "

reagan1_1 = " can't help everone, but everyone can help "

reagan2_1 = "'s first duty is to protect the "
reagan2_2 = ", not run their "

reagan3_1 = " are never defeated unless we give up on "

reagan4_1 = "When you make them see the "
reagan4_2 = ", make them feel the "

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

results = t.trends.place(_id = 2442047)
#top 10 trending results from los angeles

for location in results:
    toptrend = location["trends"][0]['name']

#module = 0
#module = random.randint(0, 2)
module = random.randint(0, 4)

if module == 0:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
                              reagan0_1 +
                              (marley[random.randint(0, len(marley) -1)]) +
                              reagan0_2 +
                              (marley[random.randint(0, len(marley) -1)]) +
                              reagan0_3 +
                              (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative ' + toptrend))

elif module == 1:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
                              reagan1_1 +
                              (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative ' + toptrend))

elif module == 2:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
                              reagan2_1 +
                              (marley[random.randint(0, len(marley) -1)]) +
                              reagan2_2 +
                              (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative ' + toptrend))

elif module == 3:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
                              reagan3_1 +
                              (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative ' + toptrend))

elif module == 4:
    t.statuses.update(status=(
                              reagan4_1 +
                              (marley[random.randint(0, len(marley) -1)]) +
                              reagan4_2 +
                              (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative ' + toptrend))

#elif module == 4:
#    t.statuses.update(status=((reagan5_1 +
#    (marley[random.randint(0, len(marley) -1)]) +
#    reagan5_2 +
#    (marley[random.randint(0, len(marley) -1)]) + '.' + ' #reggae' + ' #conservative'))