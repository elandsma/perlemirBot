import cbpro
import json
import apiconfig as cfg
import botclass
from automatedDeposit import automatedDeposit

print('The taxation of trade routes to outlaying star systems is in dispute.')

#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']
sandbox = cfg.api['SANDBOX']

#make a new bot object ()
myBot = botclass.bot(apiKey, apiSecret, apiPassphrase, sandbox)
#perhaps grab these params from the config file directly - using local variables is superfluous?

#myBot.purchase(5, 'BTC')
#.purchase doesn't do anything, was just test method.

print(myBot)
#toString test.

myBot.marketBuy(10, 'BTC-USD')
#For testing: this will give an error in sandbox mode because I can't seem to get funds deposited from fake bank account.
#That error will be appended to the marketBuys.json file.
#if no error, the transaction details get appended.
#$10 minimum!


#now testing automateDeposit bot, which is child of botclass bot (inherits all of its methods etc)
depositBot = automatedDeposit(10, 10)
#consideration: the automatedDeposit bot will get the apikey from config file in order to call the parent bot constructor
#the parent bot constructor needs these as params
#perhaps make this consistent between the two?

#testing that the childbot can do something.
depositBot.getApikey()

