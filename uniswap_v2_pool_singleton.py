import json

from web3 import Web3

# TODO: should these be flags?
_INFURA_URL = 'https://mainnet.infura.io/v3/2650232fdb0943f4951668c686fb5524'
_POOL_ADDRESS = '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
_PATH_TO_ABI = './data/UniswapV2_USDC_ABI.json'

_web3_singleton = None


def CreatePoolSingelton():
    global _web3_singleton
    if _web3_singleton is None:
        _web3_singleton = _PoolSingleton()
    return _web3_singleton


class _PoolSingleton:
    def __init__(self):
        # TODO: in some codebases, you don't want __init__ to ever fail. If that is the case I should move logic to the
        #  create function.
        self._web3 = Web3(Web3.HTTPProvider(_INFURA_URL))
        if not self._web3.is_connected():
            raise RuntimeError("Web3 HTTPProvider is not available at ", _INFURA_URL)
        with open(_PATH_TO_ABI) as abi_file:
            abi = json.load(abi_file)
            self._contract = self._web3.eth.contract(address=_POOL_ADDRESS, abi=abi)

    @property
    def contract(self):
        return self._contract

    @property
    def eth_token_index(self):
        return 1

    @property
    def usdc_token_index(self):
        return 0

    @property
    def latest_block_number(self):
        return self._web3.eth.block_number
