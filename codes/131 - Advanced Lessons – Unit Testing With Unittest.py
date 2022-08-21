'''
====================================
-- 131 - Advanced Lessons – Unit Testing With Unittest 
-- link : https://www.youtube.com/watch?v=7qDuqwRYEhI&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------------------------------
# -- Advanced_Lessons =&gt; Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------

import unittest

assert 3 * 8 == 24, "Should Be 24"

def test_case_one():

  assert 5 * 10 == 50, "Should Be 50"

def test_case_two():

  assert 5 * 50 == 250, "Should Be 250"

if __name__ == "__main__":

  test_case_one()
  test_case_two()

  print("All Tests Passed")

class MyTestCase(unittest.TestCase):

  def test_one(self):

    self.assertTrue(100 &gt; 99, "Should Be True")

  def test_two(self):

    self.assertEqual(40 + 60, 100, "Should Be 100")

  def test_three(self):

    self.assertGreater(100, 101, "Should Be True")

if __name__ == "__main__":

  unittest.main()