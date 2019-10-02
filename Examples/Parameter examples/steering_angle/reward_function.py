def reward_function(params):
    STEERING_THRESHOLD = 20.0
    # Read input variable
    steering = abs(params['steering_angle']) # We don't care whether it is left or right steering
    # Initialize the reward with typical value
    reward = 1.0
    # Penalize if car steer too much to prevent zigzag
    if steering > STEERING_THRESHOLD:
        reward *= 0.8
    return reward