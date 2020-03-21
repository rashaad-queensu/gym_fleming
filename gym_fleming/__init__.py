from gym.envs.registration import register

register(
    id='taxi_fleming-5x10',
    entry_point='gym_fleming.envs:FlemingTaxiEnv_5x10',
)

register(
    id='taxi_fleming-10x10',
    entry_point='gym_fleming.envs:FlemingTaxiEnv_10x10',
)

register(
    id='taxi_fleming-20x20',
    entry_point='gym_fleming.envs:FlemingTaxiEnv_20x20',
)
