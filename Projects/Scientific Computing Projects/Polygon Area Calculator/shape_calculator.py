class Rectangle:

  # Constructor to create width and height attributes
  def __init__(self, width,height):
    self.width = width
    self.height = height

  # Setting width 
  def set_width(self, width):
    self.width = width

  # Setting height
  def set_height(self, height):
    self.height = height

  # Calculating area
  def get_area(self):
    area = self.width * self.height
    return area

  # Calculating perimeter
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  # Calculating diagonal length
  def get_diagonal(self):
    diagonal_length = ((self.width ** 2) + (self.height ** 2)) ** 0.5
    return diagonal_length

  # Creating a picture
  def get_picture(self):
    size_error = "Too big for picture."
    if self.width > 50:
      return size_error
    if self.height > 50:
      return size_error
    picture = []
    for i in range(self.height):
      line = "*" * self.width
      picture.append(line)
    return "\n".join(picture) + "\n"

  # The number of times a shape could fit into another shape
  def get_amount_inside(self, shape):
    amount_inside = int(self.width / shape.width) * int(self.height / shape.height)
    return amount_inside
  
  # Returning rectangle details as output 
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

# Class Square inherits all the properties of class Rectangle
class Square(Rectangle):
  
  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    super().__init__(side, side)
  
  # Returning square details as output
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
