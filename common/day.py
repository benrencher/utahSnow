class Day:
  """Holds a day's date and its snow water equivalent in inches by default"""
  def __init__(self, date, swe, unit = None):
    self.date = date
    self.swe = swe # swe -> "Snow water equivalent"
    self.unit = "in" if unit == None else unit # inches by default

  def convertToCentimeters(self):
    inToCmConversion = 2.54 # 2.54 cm in an inch
    if self.unit == "in":
      self.swe = self.swe * inToCmConversion
      self.unit = "cm"

  def convertToInches(self):
    cmToInConversion = 1/2.54 # 1 inch per 2.54 centimeters
    if self.unit == "cm":
      self.swe = self.swe * cmToInConversion
      self.unit = "in"