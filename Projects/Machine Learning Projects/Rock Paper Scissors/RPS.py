
def player(prev_play, opponent_history=[]):
  
  # Dictionary to save steps 
  prev_steps = {}
  # Plays added to opponent's previous moves
  if prev_play != '' :
    opponent_history.append(prev_play)

  # Returning Rock if there is not enough moves in opponent history
  if len(opponent_history) <= 4: 
    return "R"

  # Opponent history list must contain last 4 moves known
  if len(opponent_history) > 4:
    opponent_history.pop(0)

  # Incrementing last step
  steps = "".join(opponent_history)
  prev_steps[steps] = prev_steps.get(steps, 0) + 1

  # Prediction of next move based on previous steps taken
  steps     = "".join(opponent_history[-3:])

  prediction = max([steps+"R", steps+"P", steps+"S"],
                  key=lambda key : prev_steps.get(key,0))[-1]

  # Response to moves
  if prediction == "R": return "P"
  elif prediction == "P": return "S"
  elif prediction == "S" : return "R" 
  else : return "Error : Invalid move"