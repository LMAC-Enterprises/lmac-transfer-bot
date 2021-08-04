from beem import Hive
from beem.account import Account
from beem.blockchain import Blockchain
from beem.block import Block
from beem.market import Market

hive = Hive()
hive.wallet.unlock("<KEY>")
account = Account("lmac", blockchain_instance=hive)

account.transfer("<ACCOUNT1>", "<AMOUNT>", "HIVE", "<MEMO>"),
# account.transfer("<ACCOUNT2>", "<AMOUNT>", "HIVE", "<MEMO>"),
# account.transfer("<ACCOUNT3>", "<AMOUNT>", "HIVE", "<MEMO>"),
# (...)