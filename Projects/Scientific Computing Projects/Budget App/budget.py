class Category:

  #Constructor method 
  def __init__(self, category):
    self.category = category
    self.ledger = []
  
  # Deposit method to append the amount and optional description to the ledger 
  def deposit(self, amount, description = ""):
    self.ledger.append({
      "amount": amount,
      "description": description
    })

  # Withdraw method to append the amount as a negative number to the ledger
  def withdraw(self, amount, description = ""):
    if not self.check_funds(amount):
      return False
    else:
      self.ledger.append({
        "amount": -1 * amount,
        "description": description
      })
      return True
  
  # Updating and getting the balance amount
  def get_balance(self):
    balance = 0
    for operation in self.ledger:
      balance += operation["amount"]
    return balance

  # Amount transfer
  def transfer(self, amount, category_object):
    if not self.check_funds(amount):
      return False
    else:
      self.ledger.append({
        "amount": -1 * amount,
        "description": "Transfer to " + category_object.category
      })
      category_object.deposit(amount, "Transfer from " + self.category)
      return True

  # Checking funds  
  def check_funds(self, amount):
    return amount <= self.get_balance()
  
  # Pretty output
  def __str__(self):
    output_list = []
    first_line = "*" * int((30 - len(self.category)) / 2) + self.category.title() 
    first_line = first_line + "*" * int((30 - len(first_line)))
    output_list.append(first_line)
    for operation in self.ledger:
      line = operation["description"][:23] + (" " * (23 - len(operation["description"]))) + "{:7.2f}".format(operation["amount"])
      output_list.append(line)
    last_line = "Total: " + "{:.2f}".format(self.get_balance())
    output_list.append(last_line)
    return "\n".join(output_list)

# Creating the spend chart
def create_spend_chart(categories):
  from itertools import zip_longest
  total_spend = 0
  spend = []
  
  for category in categories:
    category_spend = 0
    for operation in category.ledger:
      if operation["amount"] < 0:
        total_spend += -1 * operation["amount"]
        category_spend += -1 * operation["amount"]
    spend.append(category_spend)  
  
    
  percent_spend = [ (int((x / total_spend) * 10)) * 10 for x in spend]
  symbols = [["o" if i >= x else " " for i in percent_spend] for x in range(100, -10, -10)]
  category_names = [category.category for category in categories]
  category_names_chars = [[char for char in word] for word in category_names]
  zipped_names = list(zip_longest(*category_names_chars, fillvalue = " "))
  
  output = ["Percentage spent by category"]
  i = 0
  for j in range(100, -10, -10):
      line = " " * (3 - len(str(j))) + str(j) + "| " + "  ".join(symbols[i]) + "  "
      output.append(line)
      i += 1

  output.append(" " * 4 + "-" * (len(categories) * 3 + 1))
  for lin in zipped_names:
      output.append(" " * 5 + "  ".join(lin) + "  ")
  
  return "\n".join(output)