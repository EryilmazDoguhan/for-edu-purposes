import requests
from web3 import Account
from eth_account import Account as LocalAccount
import time
from discord_webhook import DiscordWebhook
import os 

privky = "https://discord.com/api/webhooks/1079346763510591518/6nsgyIX4rSnmQW7kJtHmkDOp2YQOPfg91BqyckfgmaZS6EFGDHHSoFTLuovhgcWg4To3"
api_key = "AIW5HS4W4RXSMUTQ71KJETTDJUX558UQ9D"
f = open("data.txt", "w")
webhook = DiscordWebhook(url=privky, content='bot is working')
webhook.execute()

while True:
    private_key = LocalAccount.create().key.hex()[2:]
    address = Account.from_key(private_key).address
    #privky = "https://discord.com/api/webhooks/1079346763510591518/6nsgyIX4rSnmQW7kJtHmkDOp2YQOPfg91BqyckfgmaZS6EFGDHHSoFTLuovhgcWg4To3"
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    balance = int(response.json()["result"]) / 10**18

    if balance > 0:
        message = f"Private key: {private_key}\nAddress: {address}\nBalance: {balance} ETH"
        webhook = DiscordWebhook(url=privky, content=message)
        webhook.execute()
        print(message)
        f.write("\n")
        f.write(message)
        f.close()



        data = {"content": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(privky, json=data, headers=headers)

        break
    else:
        print(f"Private key: {private_key}")
        print(f"Balance: {balance} ETH")