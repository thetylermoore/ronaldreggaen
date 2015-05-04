from twitter import *
import random

#fill in the required information for the entries marked "put_yours_here

access_token = "put_yours_here"
access_token_secret = "put_yours_here"
consumer_key = "put_yours_here"
consumer_secret = "put_yours_here"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

reagan = [' is not absense of conflict, it is the ability to handle conflict by means of ',
          " can't help everyone, but everyone can help "]

marley = ['Jah',
          'Herb',
          'Zion',
          'Love']

t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
    reagan[random.randint(0, len(reagan) -1)]
      + (marley[random.randint(0, len(marley) -1)]) + '. ' + '#reggae ' + '#conservative'))

