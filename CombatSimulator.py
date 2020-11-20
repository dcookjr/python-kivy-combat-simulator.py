'''
Douglas Cook
Nov 16, 2020
Basic Game combat simulator
'''

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.modules import keybinding
from kivy.core.window import Window
from kivy.uix.button import Button

class Game:
    def __init__(self):
        self.playing = True
        self.won = False
        self.playerDescription = "Welcome to the Game!"
        self.enemyDescription = "Use one of the attacks below!"
        self.location = 0
        self.target = ""
        self.damage = 0

class Ability:
    def __init__(self, name, modifier, type):
        self.name = name
        self.modifier = modifier
        self.type = type
        

class Character:
    def __init__(self):
        self.name = "Hero"
        self.HP = 100
        self.MaxHP = 100
        self.strength = 25
        self.defense = 10
        self.intelligence = 10
        self.ability0 = Ability("Attack", 1, 0)
        self.ability1 = Ability("Heavy Attack", 1.5, 0)
        self.ability2 = Ability("Fireball", 1.5, 1)
        self.ability3 = Ability("Heal", 1, 2)
class Enemy:
    def __init__(self):
        self.name = "Skelly"
        self.HP = 50
        self.MaxHP = 50
        self.modifier = 1
        self.strength = 20
        self.defense = 8
        self.intelligence = 2

player = Character()
enemy = Enemy()
currentGame = Game()

class GameGrid(GridLayout):
    def __init__(self, **kwargs):
        super(GameGrid,self).__init__(**kwargs)
        self.cols = 1
        self.StatusGrid = GridLayout()
        self.StatusGrid.cols = 2

        self.ProtagStatusGrid = GridLayout()
        self.ProtagStatusGrid.cols = 1


        self.ProtagNameLabel = Label(text=player.name)
        self.ProtagHPLabel = Label(text = str(player.HP) + "/" + str(player.MaxHP))

        self.ProtagStatusGrid.add_widget(self.ProtagNameLabel)
        self.ProtagStatusGrid.add_widget(self.ProtagHPLabel)

        self.StatusGrid.add_widget(self.ProtagStatusGrid)

        self.EnemyStatusGrid = GridLayout()
        self.EnemyStatusGrid.cols = 1


        self.EnemyNameLabel = Label(text=enemy.name)
        self.EnemyHPLabel = Label(text = str(enemy.HP) + "/" + str(enemy.MaxHP))

        self.EnemyStatusGrid.add_widget(self.EnemyNameLabel)
        self.EnemyStatusGrid.add_widget(self.EnemyHPLabel)

        self.StatusGrid.add_widget(self.EnemyStatusGrid)

        self.add_widget(self.StatusGrid)

        self.descriptionGrid = GridLayout()
        self.descriptionGrid.cols = 1

        self.playerDescriptionLabel = Label(text = currentGame.playerDescription)
        self.descriptionGrid.add_widget(self.playerDescriptionLabel)

        self.enemyDescriptionLabel = Label(text = currentGame.enemyDescription)
        self.descriptionGrid.add_widget(self.enemyDescriptionLabel)

        self.add_widget(self.descriptionGrid)

        self.buttonGrid = GridLayout()
        self.buttonGrid.cols = 2

        
        self.ability0Button = Button(text = "Attack")
        self.ability0Button.bind(on_press=self.ability0Press)
        self.ability1Button = Button(text = "Heavy Attack")
        self.ability1Button.bind(on_press=self.ability1Press)
        self.ability2Button = Button(text = "Fireball")
        self.ability2Button.bind(on_press=self.ability2Press)
        self.ability3Button = Button(text = "Heal")
        self.ability3Button.bind(on_press=self.ability3Press)

        self.buttonGrid.add_widget(self.ability0Button)
        self.buttonGrid.add_widget(self.ability1Button)
        self.buttonGrid.add_widget(self.ability2Button)
        self.buttonGrid.add_widget(self.ability3Button)



        self.add_widget(self.buttonGrid)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    def updateButtons(self):
        if (currentGame.location == 0):
            self.ability0Button.background_color = (.1, .3, 1, 1)
            self.ability1Button.background_color = (1, 1, 1, 1)
            self.ability2Button.background_color = (1, 1, 1, 1)
            self.ability3Button.background_color = (1, 1, 1, 1)
        elif (currentGame.location == 1):
            self.ability0Button.background_color = (1, 1, 1, 1)
            self.ability1Button.background_color = (.1, .3, 1, 1)
            self.ability2Button.background_color = (1, 1, 1, 1)
            self.ability3Button.background_color = (1, 1, 1, 1)
        elif (currentGame.location == 2):
            self.ability0Button.background_color = (1, 1, 1, 1)
            self.ability1Button.background_color = (1, 1, 1, 1)
            self.ability2Button.background_color = (.1, .3, 1, 1)
            self.ability3Button.background_color = (1, 1, 1, 1)
        elif (currentGame.location == 3):
            self.ability0Button.background_color = (1, 1, 1, 1)
            self.ability1Button.background_color = (1, 1, 1, 1)
            self.ability2Button.background_color = (1, 1, 1, 1)
            self.ability3Button.background_color = (.1, .3, 1, 1)

        print(currentGame.location)

    def ability0Press(self, instance):
        if currentGame.playing:
            if(player.ability0.type == 0):
                currentGame.target = enemy.name
                currentGame.damage = int((player.ability0.modifier * player.strength) * enemy.defense / 100)
                enemy.HP -= currentGame.damage

            if(player.ability0.type == 1):
                currentGame.target = enemy.name
                currentGame.damage = int((player.ability0.modifier * player.intelligence) * enemy.defense / 100)
                enemy.HP -= currentGame.damage

            elif(player.ability0.type == 2):
                currentGame.target = enemy.name
                currentGame.damage = int(player.ability30.modifier * player.intelligence)
                player.HP += currentGame.damage
            currentGame.location = 0
            currentGame.playerDescription = "You used " + player.ability0.name + " on " + currentGame.target + " for " + str(currentGame.damage)
            self.playerDescriptionLabel.text = currentGame.playerDescription
            self.EnemyHPLabel.text= str(enemy.HP) + "/" + str(enemy.MaxHP)
            self.enemyTurn()
            self.enemyDescriptionLabel.text = str(enemy.name) + " attacks you for " + str(currentGame.damage)
            self.ProtagHPLabel.text = str(player.HP) + "/" + str(player.MaxHP)
            self.updateButtons()
            self.checkState()

    def ability1Press(self, instance):
        if currentGame.playing:
            if(player.ability1.type == 0):
                currentGame.damage = (player.ability1.modifier * player.strength) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            if(player.ability1.type == 1):
                currentGame.damage = (player.ability1.modifier * player.intelligence) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            elif(player.ability1.type == 2):
                currentGame.damage = player.ability1.modifier * player.intelligence
                player.HP += currentGame.damage
                currentGame.target = player.name
            currentGame.location = 0
            self.enemyTurn()
            currentGame.playerDescription = "You used " + player.ability1.name + " on " + currentGame.target + " for " + str(currentGame.damage)
            self.playerDescriptionLabel.text = currentGame.playerDescription
            self.EnemyHPLabel.text= str(enemy.HP) + "/" + str(enemy.MaxHP)
            self.enemyTurn()
            self.enemyDescriptionLabel.text = str(enemy.name) + " attacks you for " + str(currentGame.damage)
            self.ProtagHPLabel.text = str(player.HP) + "/" + str(player.MaxHP)
            self.updateButtons()
            self.checkState()

    def ability2Press(self, instance):
        if currentGame.playing:
            if(player.ability2.type == 0):
                currentGame.damage = (player.ability2.modifier * player.strength) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            if(player.ability2.type == 1):
                currentGame.damage = (player.ability2.modifier * player.intelligence) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            elif(player.ability2.type == 2):
                currentGame.damage= player.ability2.modifier * player.intelligence
                enemy.HP += currentGame.damage
                currentGame.target = player.name
            currentGame.location = 0
            self.enemyTurn()
            currentGame.playerDescription = "You used " + player.ability2.name + " on " + currentGame.target + " for " + str(currentGame.damage)
            self.playerDescriptionLabel.text = currentGame.playerDescription
            self.EnemyHPLabel.text= str(enemy.HP) + "/" + str(enemy.MaxHP)
            self.enemyTurn()
            self.enemyDescriptionLabel.text = str(enemy.name) + " attacks you for " + str(currentGame.damage)
            self.ProtagHPLabel.text = str(player.HP) + "/" + str(player.MaxHP)
            self.updateButtons()
            self.checkState()

    def ability3Press(self, instance):
        if currentGame.playing:
            if(player.ability3.type == 0):
                currentGame.damage = (player.ability3.modifier * player.strength) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            if(player.ability3.type == 1):
                currentGame.damage = (player.ability3.modifier * player.intelligence) * enemy.defense / 100
                enemy.HP -= currentGame.damage
                currentGame.target = enemy.name

            elif(player.ability3.type == 2):
                currentGame.damage = player.ability3.modifier * player.intelligence
                player.HP += currentGame.damage
                currentGame.target = player.name
            currentGame.location = 0
            self.enemyTurn()
            currentGame.playerDescription = "You used " + player.ability3.name + " on " + currentGame.target + " for " + str(currentGame.damage)
            self.playerDescriptionLabel.text = currentGame.playerDescription
            self.EnemyHPLabel.text= str(enemy.HP) + "/" + str(enemy.MaxHP)
            self.enemyTurn()
            self.enemyDescriptionLabel.text = str(enemy.name) + " attacks you for " + str(currentGame.damage)
            self.ProtagHPLabel.text = str(player.HP) + "/" + str(player.MaxHP)
            self.updateButtons()
            self.checkState()

    def enemyTurn(self):
        currentGame.target = player.name
        currentGame.damage = int(enemy.modifier * enemy.strength * player.defense / 100)
        player.HP -= currentGame.damage

    def wPress(self):
        if currentGame.location > 1:
            currentGame.location -= 2
        self.updateButtons()
    
    def sPress(self):
        if currentGame.location < 2:
            currentGame.location += 2
        self.updateButtons()

    def aPress(self):
        if(currentGame.location == 1 or currentGame.location == 3):
            currentGame.location -= 1
        self.updateButtons()

    def dPress(self):
        if(currentGame.location == 0 or currentGame.location == 2):
            currentGame.location += 1
        self.updateButtons()
    
    def enterPress(self):
        print("Enter")
        if(currentGame.location == 0):
            self.ability0Press(self.ability0Button)
        elif(currentGame.location == 1):
            self.ability1Press(self.ability1Button)
        elif(currentGame.location == 2):
            self.ability2Press(self.ability2Button)
        elif(currentGame.location == 3):
            self.ability3Press(self.ability3Button)
        self.updateButtons()
        
    def checkState(self):
        if player.HP <= 0 or enemy.HP <= 0:
            currentGame.playing = False
            if player.HP <= 0:
                currentGame.won = False
                self.playerDescriptionLabel.text = "Sorry"
                self.enemyDescriptionLabel.text = "Seems you lost..."
            else:
                currentGame.won = True
                self.playerDescriptionLabel.text = "Congratulations!"
                self.enemyDescriptionLabel.text = "You have defeated your enemy!"
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if (keycode[1] == 'w'):
            self.wPress()
        elif (keycode[1] == 's'):
            self.sPress()
        elif (keycode[1] == 'a'):
            self.aPress()
        elif (keycode[1] == 'd'):
            self.dPress()
        elif (keycode[1] == "enter"):
            self.enterPress()

class CombatSimulator(App):
    def build(self):
        return GameGrid()


if __name__ == "__main__":
    CombatSimulator().run()