class HeroMelee():
    def __init__(self, health, attack, agility, race, experience):
        """ Class to Create our Hero """
        self.health = health
        self.attack = attack
        self.agility = agility
        self.race = race
        self.experience = experience

    def show_hero(self):
        """ Print All parameters our Hero """
        parameters  = ("State: \n\tExperience: " + str(self.experience) +  "\n\tHealth: " + str(self.health) +
                       "\n\tBase attack: " + str(self.attack) + "\n\tBase agility:" + str(self.agility) +
                       "\n\tRace: " + self.race)
        print(parameters)

    def lvl_up(self):
        """ LevelUp with  add base attribute """
        self.health += 10
        self.attack += 2
        self.agility += 3
        print("Congratulations! You are have new level!")

    def kill_monster(self):
        """ Add Exp from the easy monster """
        self.experience += 30

    def kill_boss(self):
        self.experience += 300








