import time

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['text'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
        print()

    def start_quiz(self):
        print("Welcome to the Amazing Quiz Game!")
        time.sleep(1)

        for question in self.questions:
            self.display_question(question)
            start_time = time.time()

            user_answer = input("Your answer: ")

            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time > 15:
                print("Time's up! You took too long to answer.")
            elif user_answer.lower() == question['answer'].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}.\n")

            
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

# Sample questions
questions = [
    {
        'text': 'What is the capital of France?',
        'options': ['Berlin', 'Paris', 'London', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'text': 'Which programming language is this quiz written in?',
        'options': ['Java', 'Python', 'C++', 'JavaScript'],
        'answer': 'Python'
    },

    {
        'text': 'Who is the best Footballer in the world?',
        'options': ['Messi', 'Pele', 'Cristiano Ronaldo', 'Neymar'],
        'answer': 'Messi'
    },
  
]

if __name__ == "__main__":
    quiz = Quiz(questions)
    quiz.start_quiz()
