from tkinter import *
import random, time

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.teams = []
        self.league_size = len(self.teams)
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Teams\n").grid(row=0, column=0)
        Label(self,
              text = str(self.league_size)).grid(row=0, column=0, sticky=S)

        Label(self,
              text="Enter your teams here: ").grid(row=0, column=1, columnspan=2)

        self.team_name = Entry(self)
        self.team_name.grid(row=1, column=1, columnspan=3)

        Button(self,
               text="Clear",
               command = self.clear_button).grid(row=2, column=0)

        Button(self,
               text="Add Team",
               command=self.add_team).grid(row=2, column=1)

        Button(self,
               text="Generate Draft Order",
               command=self.draft_order).grid(row=2, column=2)

        self.order = Text(self, height=10, width=30, wrap=WORD)
        self.order.grid(row=3, column=0, columnspan=3)


    def add_team(self):
        team = self.team_name.get()
        if team:
            self.teams.append(team)
            self.league_size += 1
            self.team_name.delete(0, END)
            Label(self,
                  text = str(self.league_size)).grid(row=0, column=0, sticky=S)

    def draft_order(self):
        while self.league_size != 0:
            random_team = random.choice(self.teams)
            draft_spot = len(self.teams)
            draft_pick = "Pick " + str(draft_spot) + " " + random_team + "\n"
            self.order.insert(0.0, draft_pick)
            self.teams.remove(random_team)
            self.league_size -= 1


    def clear_button(self):
        self.teams.clear()
        self.order.delete(0.0, END)
        Label(self,
              text = len(self.teams)).grid(row=0, column=0, sticky=S)
        self.league_size = 0


root = Tk()
root.title("Draft Order")
app = Application(root)
root.mainloop()
