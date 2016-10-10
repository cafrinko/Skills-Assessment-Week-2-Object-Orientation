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
            print "%s" %(self.question)
            answer_prompt = raw_input("> ")
            if self.correct_answer == answer_prompt:
                return True
            else:
                return False

"""3."""

    class Exam(Question):

        def __init__(self, name, question = None, correct_answer = None):
           self.name = name
           super(Exam, self).__init__(question, correct_answer)
           self.questions = []

        def add_question(self, question, correct_answer):
            q_and_a_pair = Question(question, correct_answer)
            self.questions.extend(self.q_and_a_pair)

        def administer(self):
            # print "\n".join(self.questions)
            score = 0
            for self.question in self.questions:
                super(Exam, self).question_ask_and_evaluate()
                if True:
                    score += 1
            return score

""" Part 4"""

"""1."""

    def take_test(exam, student):

        exam.administer()
        setattr(student, score, exam.administer())

"""2."""

    def example(exam, student):

        exam = Exam("Anxiety Level")

        question1 = "Are you ready for this?"
        correct_answer1 = "No"
        exam.add_question(question1, correct_answer1)

        question2 = "What is your stress level on a scale of 1 to 10?"
        correct_answer2 = "7"
        exam.add_question(question2, correct_answer2)

        student_first_name = "Isabelle"
        student_last_name = "Allende"
        student_address = "2525 Lantern Way Humboldt, CA 94123"
        student = Student(student_first_name, student_last_name, student_address)

        exam.administer()
        
"""Part 5"""

    class Quiz(Exam, Question):

        def __init__(self, name, question = None, correct_answer = None):
            super(Quiz, self).__init__(name, question, correct_answer)
            self.questions = []

        def add_question(self, question, correct_answer):
            super(Quiz, self).add_question()

        def administer(self):
            score = 0
            for self.question in self.questions:
                super(Quiz, self).question_ask_and_evaluate()
                if True:
                    score += 1
            if score >= (len(self.questions) / 2):
                result = True
            else:
                result = False
            return result




