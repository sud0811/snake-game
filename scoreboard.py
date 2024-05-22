from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score= int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y= 270)
        self.write ( arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 24, 'normal'))
        self.hideturtle()
        
    def reset(self): 
        if self.score > self.high_score:
            self.high_score= self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            
        self.score = 0
        self.clear()
        self.write ( arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 24, 'normal'))
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write ( arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 24, 'normal'))