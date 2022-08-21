'''
====================================
-- 084 - Decorators – Function with Parameters 
-- link : https://www.youtube.com/watch?v=ZVCPwfyAcBE&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------
# -- Decorators =&gt; Function With Parameters --
# --------------------------------------------

def myDecorator(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    if num1 &lt; 0 or num2 &lt; 0:

      print("Beware One Of The Numbers Is Less Than Zero")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

def myDecoratorTwo(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    print("Coming From Decorator Two")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator
@myDecoratorTwo

def calculate(n1, n2):

  print(n1 + n2)

calculate(-5, 90)