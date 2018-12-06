import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

# P2P_PREFIX is taken from chainparams.cpp in the official Platinum coin repo
P2P_PREFIX = 'fbc1b8dc'.decode('hex')
P2P_PORT = 13580
ADDRESS_VERSION = 23
RPC_PORT = 13581
RPC_CHECK = True
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
  'address' in (yield bitcoind.rpc_help()))) 
SUBSIDY_FUNC = lambda height: 200*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 60
SYMBOL = 'AGNT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.platinumcoin'), 'bitcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
