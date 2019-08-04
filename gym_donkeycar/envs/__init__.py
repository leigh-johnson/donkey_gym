from gym.envs.registration import register

register(
    id='donkey-generated-roads-v0',
    entry_point='gym_donkeycar.envs.donkey_env:GeneratedRoadsEnv',
)

register(
    id='donkey-warehouse-v0',
    entry_point='gym_donkeycar.envs.donkey_env:WarehouseEnv',
)

register(
    id='donkey-avc-sparkfun-v0',
    entry_point='gym_donkeycar.envs.donkey_env:AvcSparkfunEnv',
)

register(
    id='donkey-generated-track-v0',
    entry_point='gym_donkeycar.envs.donkey_env:GeneratedTrackEnv',
)
