def reward_function(params):
   #Read input parameters
   all_wheels_on_track = params['all_wheels_on_track']
   distance_from_center = abs(params['distance_from_center'])
   track_width = params['track_width']

   #Give a very low reward by default
   reward = 1e-3

   # Give a high reward if no wheels go off the track and the vehicle is somewhere in between the track borders
   if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
      reward = 1.0
   # Always return a float value
   return reward