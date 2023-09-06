class Scoreboard:
    def __init__(self, team):
        self.team = team
        self.score = 0
        
    def __repr__(self):
        return f'<Scoreboard {self.team}, {self.score}>'
    
    def __eq__(self, other):
        return self.team == other.team and self.score == other.score
    
    def __hash__(self):
        return hash((self.team, self.score))
    
    def get_team(self):
        return self.team
    
    def get_score(self):
        return self.score
    
    def update_score(self, value):
        self.score += value

class Question:
    def __init__(self, theme, question, value):
        self.theme = theme
        self.question = question
        self.value = value
        self.image = None
    
    def __repr__(self):
        return f'<Question {self.question}, {self.value}>'
    
    def __eq__(self, other):
        return self.question == other.question and self.image == other.image
    
    def __lt__(self, other):
        return self.image < other.image
    
    def __hash__(self):
        return hash((self.question, self.image))
    
    def get_theme(self):
        return self.theme
        
    def get_question(self):
        return self.question
    
    def get_image(self):
        return self.image

class Answer:
    def __init__(self, answer):
        self.answer = answer
        self.correct = False
    
    def __repr__(self):
        return f'<Answer {self.answer}, {self.correct}>'
    
    def __eq__(self, other):
        return self.answer == other.answer and self.correct == other.correct
    
    def __hash__(self):
        return hash((self.answer, self.correct))
    
    def get_answer(self):
        return self.answer
    
    def is_correct(self):
        self.correct = True

    def is_wrong(self):
        self.correct = False
        

