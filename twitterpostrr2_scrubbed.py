from twitter import *
import random

#fill in the required information for entries marked "put_yours_here"

access_token = "put_yours_here"
access_token_secret = "put_yours_here"
consumer_key = "put_yours_here"
consumer_secret = "put_yours_here"

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

reagan1_1 = " is not absense of "
reagan1_2 = ", it is the ability to handle "
reagan1_3 = " by means of "

reagan2_1 = " can't help everone, but everyone can help "

reagan3_1 = "'s first duty is to protect the "
reagan3_2 = ", not run their "

reagan4_1 = " are never defeated unless we give up on "

reagan5_1 = "When you make them see the "
reagan5_2 = ", make them feel the "

module = random.randint(0, 4)

if module == 0:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
    #reagan1[random.randint(0, len(reagan1) -1)]
    reagan1_1 +
    (marley[random.randint(0, len(marley) -1)]) +
    reagan1_2 +
    (marley[random.randint(0, len(marley) -1)]) +
    reagan1_3 +
    (marley[random.randint(0, len(marley) -1)]) + '.'))

elif module == 1:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
    reagan2_1 +
    (marley[random.randint(0, len(marley) -1)]) + '.'))

elif module == 2:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
    reagan3_1 +
    (marley[random.randint(0, len(marley) -1)]) +
    reagan3_2 +
    (marley[random.randint(0, len(marley) -1)]) + '.'))

elif module == 3:
    t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
    reagan4_1 +
    (marley[random.randint(0, len(marley) -1)]) + '.'))

elif module == 4:
    t.statuses.update(status=((reagan5_1 +
    (marley[random.randint(0, len(marley) -1)]) +
    reagan5_2 +
    (marley[random.randint(0, len(marley) -1)]) + '.' + '#reggae ' + '#conservative'))

#t.statuses.update(status=((marley[random.randint(0, len(marley) -1)]) +
#    reagan[random.randint(0, len(reagan) -1)]
#      + (marley[random.randint(0, len(marley) -1)]) + '. ' + '#reggae ' + '#conservative'))
