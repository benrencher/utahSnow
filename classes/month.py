class Month:
  """Holds month information and can make changes to day children"""
  def __init__(self):
    self.month = None # starts at 1 for January
    self.days = [] # days are stored sequentially beginning at 1
    self.max = None
    self.min = None
    self.average = None
    self.dataUnits = "in" # inches by default

  def displayMonthName(self, isAbbreviated):
    if self.month == None | self.month > 12 | self.month < 1:
      raise ValueError(f"Impossible month value: {self.month}")
    match self.month:
      case 1:

        return "Jan" if isAbbreviated else "January"
      case 2:
        return "Feb" if isAbbreviated else "February"
      case 3:
        return "Mar" if isAbbreviated else "March"
      case 4:
        return "Apr" if isAbbreviated else "April"
      case 5:
        return "May"
      case 6:
        return "Jun" if isAbbreviated else "June"
      case 7:
        return "Jul" if isAbbreviated else "July"
      case 8:
        return "Aug" if isAbbreviated else "August"
      case 9:
        return "Sep" if isAbbreviated else "September"
      case 10:
        return "Oct" if isAbbreviated else "October"
      case 11:
        return "Nov" if isAbbreviated else "November"
      case 12:
        return "Dec" if isAbbreviated else "December"
      
  def determineMax(self):
    max = 0
    for day in self.days:
      if day.unit != self.dataUnits & self.dataUnits == "in":
        day.convertToInches()
      else:
        day.convertToCentimeters()
      
      if day.swe > max:
        max = day.swe
    self.max = max

  def determineMix(self):
    pass

  def determineAverage(self):
    pass

  def convertToInches(self):
    pass

  def convertToCentimeters(self):
    pass