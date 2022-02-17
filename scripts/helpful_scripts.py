from brownie import network, accounts, config, MockAggregator
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "Ganache-Local"]


DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_price_feed_address():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        return MockAggregator[-1].address


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockAggregator) <= 0:
        MockAggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
