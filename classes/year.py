class Year:
  def __init__(self, fullYear, months = []):
    self.fullYear = fullYear
    self.months = months
    self.isLeapYear = None

  def determineLeapYearStatus(self):
    #leap year rules: must be divisible by 4 unless divisible by 100 but not by 400
    if self.fullYear != None:
      self.isLeapYear = self.fullYear % 4 == 0 and not self.fullYear % 100 == 0 or self.fullYear % 400 == 0