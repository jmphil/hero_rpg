#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. fight zombie
# 3. do nothing - in which case the goblin will attack him anyway
# 4. use health pot +10 health / hero only
# 5. use armor up pot / def +2
# 6. use evade plus pot  / 2 evade = 10% dodge / 4 evade = 20% dogdge ...
# 7. flee
# 8. 
class Character:
    
    def alive(self):#step4
        if self.health > 0 :
            return True
        else:
            return False
        
    def atk(self, enemy):#part3
        enemy.health -= self.power 
        
    # def defend(self):
    #     pass

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        # self.armor = armor
        
    def atk(self, enemy):#part2 
        enemy.health -= self.power
         
    def alive(self):#step4
        if self.health > 0 :
            return True
        else:
            return False

    def print_status(self):#step5
        print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
       
    def print_status(self):#step5
        print(f"The goblin has {self.health} health and {self.power} power.")
        
class Zombie(Character):
    def __init__(self, health):
        self.health = health
        
    def print_status(self):    
        print(f"The zomie has {self.health} health")
        
class Medic(Character):
    def __init__(self, health, power):
        self.health = power
        self.power = power
        
class Shadow(Character):
    def __init__(self, health, power):
        pass

def main():#part1
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    zombie = Zombie(float('inf'), 0)



        
    while goblin.alive() > 0 and hero.alive() > 0:
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zombie")
        # print("3. defend")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
                hero.atk(goblin)
                print("You do {} damage to the goblin.".format(hero.power))
            # if not goblin.alive()
            #     print("The goblin is dead.")
        elif raw_input == "2":
                hero.atk(zombie)
                print("You do {} damage to the zombie.".format(hero.power)
                      
        elif raw_input == "3":
            pass
            
        elif raw_input == "4":
            print("You have fled the battle.")
            break
            
        else:
            print("Invalid input {}".format(raw_input))
            
            
        if goblin.alive():
            # Goblin attacks hero
            # goblin.atk(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if not hero.alive():
                print("You are dead.")

main()
   
            

