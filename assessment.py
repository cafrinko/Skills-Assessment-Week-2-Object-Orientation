"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
       Encapsulation - instead of separating the function from the data in separate
       files, modules, etc, you can define and organically create the data with a
       class.
       Abstration - attributes and methods that multiple instances of the class have
       in common can be stated in a class that doesn't need to be called.
       Polymorphism - can make multiple instances of a class with
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


""" Part 2: Classes and Init Methods"""

""" 1. Student """

   class Student(object):

       def __init__(self, first_name, last_name, address):
           self.first_name = first_name
           self.last_name = last_name
           self_address = address

"""2. Question"""

    class Question(object):

        def __init__(self, question, correct_answer):
           self.question = question
           self.correct_answer = correct_answer

"""3.  Exam"""

    class Exam(object):

        def __init__(self, name):
           self.name = name
           self.questions = []


""" Part 3: Methods:"""

"""1.""" 

    class Exam(Question):

        def __init__(self, name, question, correct_answer):
           self.name = name
           super(Exam, self).__init__(question, correct_answer)
           self.questions = []

        def add_question(self):
            return self.question
            self.questions.extend(self.question, self.correct_answer)

"""2."""

    class Question(object):

    def __init__(self, question, correct_answer):
       self.question = question
       self.correct_answer = correct_answer

    def question_ask_and_evaluate(self):
        answer_prompt = raw_input("> ")
        print "%s %s" %(self.question, answer_prompt)
        if self.correct_answer == answer_prompt:
            return True
        else:
            return False

"""3."""

    class Exam(Question):

        def __init__(self, name, question, correct_answer):
           self.name = name
           super(Exam, self).__init__(question, correct_answer)
           self.questions = []

        def add_question(self, question, correct_answer):
            self.question = Question(raw_input("Add your new exam question here > "), raw_input("Add the answer to your question here > "))
            self.questions.extend(self.question, self.correct_answer)    

        def administer(self):
            score = 0
            for self.question in self.questions:
                super(Exam, self).question_ask_and_evaluate()
                if True:
                    score += 1
            return score

""" Part 4"""

"""1."""

    def take_test(exam, student)

        exam.administer()
        setattr(student, score, exam.administer())

"""2."""

    def example():

        exam_name = raw_input("What would you like to call this exam? > ")
        print exam_name
        first_question = raw_input("Please enter the first question. > ")
        print first_question
        first_answer = raw_input("Please enter the answer to the first question. > ")
        exam = Exam(exam_name, first_question, first_answer)

        add_addl_question = raw_input("Would you like to add another question and answer pair? Enter Y or N >")
        while addl_question_prompt == "Y":
            next_question = raw_input("Please enter a question. > ")
            print next_question
            next_answer = raw_input("Please enter the answer > ")
            exam.add_question(next_question, next_answer)
            continue

        student_first_name = raw_input("What is your first name? > ")
        student_last_name = raw_input("What is your last name? > ")
        student_address = raw_input("What is your address? > ")
        student = Student(student_first_name, student_last_name, student_address)
        print "%s %s \n %s" %(student_first_name, student_last_name, student_address)
        print "Hello %s, and welcome to your exam. Let's begin" %(student_first_name)

        exam.administer()
        
"""3."""

