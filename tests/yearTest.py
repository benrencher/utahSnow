from classes.year import Year

def testLeapYear():
  totalCases = 4
  correct = 0
  incorrect = []
  # 2000 -> True (testing divisible by 400, 4, and 100)
  testYear = Year(2000)
  testYear.determineLeapYearStatus()
  if testYear.isLeapYear:
    correct += 1
  else:
    incorrect.append(testYear.fullYear)

  # 1900 -> False (testing divisible by 4 and 100 but not 400)
  testYear.fullYear = 1900
  testYear.determineLeapYearStatus()
  if not testYear.isLeapYear:
    correct += 1
  else:
    incorrect.append(testYear.fullYear)

  # 2024 -> True (testing divisible by 4)
  testYear.fullYear = 2024
  testYear.determineLeapYearStatus()
  if testYear.isLeapYear:
    correct += 1
  else:
    incorrect.append(testYear.fullYear)

  # 2023 -> False (testing indivisible by 4)
  testYear.fullYear = 2023
  testYear.determineLeapYearStatus()
  if not testYear.isLeapYear:
    correct += 1
  else:
    incorrect.append(testYear.fullYear)

  correctPercent = (correct / totalCases) * 100
  print(f"correct: {correctPercent}% | incorrect: {100 - correctPercent}% | incorrect cases: {incorrect}")

testLeapYear()