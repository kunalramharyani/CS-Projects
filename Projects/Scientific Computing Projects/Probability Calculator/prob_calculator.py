import copy
import random

class Hat:
  
  # Constructor to create any number of balls with a colour using **kwargs
  def __init__(self, **kwargs):
    self.contents = []
    # Traversing through each item in the dictionary
    for colour, number in kwargs.items():
      # Adding the colours to the contents list
      for i in range(number):
        self.contents.append(colour)

  # Draw method to remove balls from contents      
  def draw(self, number_of_balls):
    if number_of_balls >= len(self.contents):
      return self.contents
    balls_drawn = []
    for i in range(number_of_balls):
      balls = random.randrange(len(self.contents))
      balls_drawn.append(self.contents[balls])
      del self.contents[balls]
      
    return balls_drawn

# Experiment function to calculate approximate probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  num_success = 0
  
  for i in range(num_experiments):
    # Creating copy of hat object
    hat_copy = copy.deepcopy(hat)
    experiment_result = hat_copy.draw(num_balls_drawn)
    experiment_result_object = {}
    for ball in experiment_result:
      if ball in experiment_result_object:
        experiment_result_object[ball] += 1
      else:
        experiment_result_object[ball] = 1
    
    success = 1
    for colour, num in expected_balls.items():
      # Checking if desired colour found in experiment_result_object
      if colour in experiment_result_object and experiment_result_object[colour] >= num:
        success *= 1
      else:
        success = 0
        break
    num_success += success
    approx_prob = num_success / num_experiments
  return approx_prob