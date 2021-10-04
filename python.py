from beem import Hive
from beem.account import Account
from beem.blockchain import Blockchain
from beem.block import Block
from beem.market import Market

hive = Hive()
hive.wallet.unlock("<KEY>")
account = Account("lmac", blockchain_instance=hive)


#size of prize pool in HIVE
pool = 200

#round of LMAC
round = 93

#list of winners in ranked order
panel = ['<ACCOUNT1>', '<ACCOUNT2>', ... ,'<ACCOUNT15>' ]

#prize ranks
rank = ["first", "second", "third", "fourth", "fifth", "Top10", "Top15"]

for i in panel:
    #transactions rank 1-5
    if n <= 4:
        account.transfer(panel[n], "{:0.2f}".format(prize[n]), "HIVE", "Congratulations, your entry won the %s place in the LMAC Round %s!" % (rank[n], round));
        n +=1;
    #transactions Top 10
    elif n <= 9:
        account.transfer(panel[n], "{:0.2f}".format(prize[5]), "HIVE", "Congratulations, your entry made it in the %s in the LMAC Round %s!" % (rank[5], round));
        n +=1;
    #transactions Top 15
    else:
        account.transfer(panel[n], "{:0.2f}".format(prize[6]), "HIVE", "Congratulations, your entry made it in the %s in the LMAC Round %s!" % (rank[6], round));
        n +=1;
