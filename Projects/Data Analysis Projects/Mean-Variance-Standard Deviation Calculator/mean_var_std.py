import numpy as np
def calculate(list):
  # Checking the number of elements in the list
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  
  # Reshaping the list to a 3 x 3 matrix format
  matrix = np.reshape(list, (3, 3))
  
  calculations = {}
  
  # Calculating mean
  calculations["mean"] = [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(matrix)]
  # Calculating variance
  calculations["variance"] = [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(matrix)]
  # Calculating standard deviation
  calculations["standard deviation"] = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(matrix)]
  # Calculating max number
  calculations["max"] = [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(matrix)]
  # Calculating min number
  calculations["min"] = [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(matrix)]
  # Calculating sum
  calculations["sum"] = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(matrix)]
  
  return  calculations