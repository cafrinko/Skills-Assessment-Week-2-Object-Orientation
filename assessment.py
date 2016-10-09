"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Encapsulation - instead of separating the function from the data in separate
   files, modules, etc, you can define and organically create the data with a
   class.
       Abstration - attributes and methods that multiple instances of the class have
       in common can be stated in a class that doesn't need to be called.
       Flexibility of structure - can make multiple instances of a class with
       varying and interchangeable attributes and methods.
2. What is a class?
       A type of construct that groups methods and data in containers, allowing you
       to access them later
3. What is an instance attribute?
       A piece of data set on the object
4. What is a method?
       A function defined on a class
5. What is an instance in object orientation?
       An child and type of what the parent class was defining, or an individual
       occurrence of a class. It is also known as an object
6. How is a class attribute different than an instance attribute?
       Give an example of when you might use each.
       A class attribute is defined on the class, and an instance attribute is
       defined on the object. If you want all instances of an Animal class
       to all share a common base greeting like "hello", you can make that a
       class attribute. Since each animal's name varies, you can use an instance
       attribute, so all animals can have access to the attribute and the name
       value can be defined when the particular animal instance is called.

"""


"""
Part 2: Classes and Init Methods

1. Student

   class Student(object):

       def __init__(self, first_name, last_name, address):
           self.first_name = first_name
           self.last_name = last_name
           self_address = address

2.  Question

    class Question(object):

        def __init__(self, question, correct_answer):
           self.question = question
           self.correct_answer = correct_answer

3.  Exam

    class Exam(object):

        def __init__(self, name):
           self.name = name
           self.questions = []

"""

"""
Part 3: Methods:

1. 
    class Exam(Question):

        def __init__(self, name):
           self.name = name
           super(Exam, self).__init__(question, correct_answer)
           self.questions = []

        def add_question(self):
            print %s %(self.question)
            self.questions.extend(self.question)





