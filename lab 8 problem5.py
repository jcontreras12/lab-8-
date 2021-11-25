# Jose Contreras
# 11/22/21
# Write a function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs.
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

print(" There are three task you can do")
print("Task 1. Climb a mountain")
print("Task.2 cook a Meal")
print("Task 3. Write a book")
option = input(" Enter one of the following options 1-3")

if option == '1':
    task = ['rope', 'coat', ' first aid kit']
    not_allowed_state = 'slow'

if option == '2':
    task = ['pan', 'groceries']
    not_allowed_state = 'small'

if option == '3':
    task = ['pen', 'paper']
    not_allowed_state = 'confusion'

player1.check_equipment(task, not_allowed_state)
