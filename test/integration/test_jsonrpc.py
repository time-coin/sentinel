import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from timed import TIMEDaemon
from time_config import TIMEConfig


def test_timed():
    config_text = TIMEConfig.slurp_config_file(config.time_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000f9af577358ea5cbd79b0a4e32a0fab8b921543ec03dfaf653ffc06a9784'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'000002731816bccf90ab744347dc894cf484e3826b19f967b8d5f028c204a4f0'

    creds = TIMEConfig.get_rpc_creds(config_text, network)
    timed = TIMEDaemon(**creds)
    assert timed.rpc_command is not None

    assert hasattr(timed, 'rpc_connection')

    # TIME testnet block 0 hash == 000002731816bccf90ab744347dc894cf484e3826b19f967b8d5f028c204a4f0
    # test commands without arguments
    info = timed.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert timed.rpc_command('getblockhash', 0) == genesis_hash
