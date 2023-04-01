class Year:
  def __init__(self, fullYear, months = []):
    self.fullYear = fullYear
    self.months = months
    self.isLeapYear = None
    self.maxSwe = 0
    self.maxMonthNumber = 0
    self.dataUnits = "in"

  def determineLeapYearStatus(self):
    #leap year rules: must be divisible by 4 unless divisible by 100 but not by 400
    if self.fullYear != None:
      self.isLeapYear = self.fullYear % 4 == 0 and not self.fullYear % 100 == 0 or self.fullYear % 400 == 0
    
  def determineMaxSwe(self):
    for month in self.months:
      monthMax = month.max
      if self.dataUnits != month.dataUnits:
        if self.dataUnits == "in":
          monthMax = self.convertToInches(monthMax)
        else:
          monthMax = self.convertToCentimeters(monthMax)
      if self.maxSwe < monthMax:
        self.maxSwe = monthMax
        self.maxMonthNumber = month.month

  def convertToInches(cm):
    inchesInACm = 1/2.54
    return cm * inchesInACm
  
  def convertToCentimeters(inches):
    cmInAnInch = 2.54
    return inches * cmInAnInch
    