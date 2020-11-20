#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def atk(self, enemy):#part2 
        enemy.health -= self.power
         
    def alive(self):#step4
        if self.health > 0 :
            return True
        else:
            return False

    def print_status(self, health, power):#step5
        print(f"You have {hero.health} health and {hero.power} power.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
       
    def atk(self, enemy):#part3
        enemy.health -= self.power   

    def alive(self):#step4
        if self.health > 0 :
            return True
        else:
            return False

    def print_status(self, health, power):#step5
        
        print(f"The goblin has {self.health} health and {self.power} power.")

def main():#part1
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)



        
    while goblin.alive() > 0 and hero.alive() > 0:
        hero.print_status()
        goblin.print_status()
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.atk(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if not goblin.alive():
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.atk(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if not hero.alive():
                print("You are dead.")

main()
   
            

