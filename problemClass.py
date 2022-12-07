class Problem:
  def __init__(self, number, description, input,test_input = None ,test_answer = None):
    self.number = number
    self.description = description
    self.input = input
    self.test_answer = test_answer
    self.test_input = test_input


  def test_solution(self):
    if self.test_input == None or self.test_answer == None:
      print("No test inputs given for problem number:", self.number)
      return False 

    test_solution = self.solution(self.test_input)
    print(test_solution)
    if self.test_answer == test_solution:
      print("Test Passed.")
      return True
    else:
      print("Test Failed. Correct answer:", self.test_answer, "Answer given:", test_solution)
      return False
