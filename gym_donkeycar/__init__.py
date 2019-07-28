# -*- coding: utf-8 -*-

"""Top-level package for OpenAI Gym for Donkey Car (https://www.donkeycar.com/)."""

__author__ = """Leigh Johnson"""
__email__ = 'leigh@data-literate.com'
__version__ = '1.0.0'

from gym.envs.registration import register

register(
    id='donkey-generated-roads-v0',
    entry_point='gym_donkeycar.envs:GeneratedRoadsEnv',
)

register(
    id='donkey-warehouse-v0',
    entry_point='gym_donkeycar.envs:WarehouseEnv',
)

register(
    id='donkey-avc-sparkfun-v0',
    entry_point='gym_donkeycar.envs:AvcSparkfunEnv',
)

register(
    id='donkey-generated-track-v0',
    entry_point='gym_donkeycar.envs:GeneratedTrackEnv',
)
