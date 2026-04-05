import random
import time

class PythonQuest:
    def __init__(self):
        self.player_level = 1
        self.score = 0
        self.max_health = 100
        self.health = 100
        self.experience = 0
        self.exp_to_next_level = 50
        
    def print_slow(self, text, delay=0.03):
        """Typewriter effect for immersion"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def clear_screen(self):
        print("\033[H\033[J", end="")
    
    def show_status(self):
        print(f"\n{'='*50}")
        print(f"🐍 PYTHON QUEST 🐍 | Level: {self.player_level} | Score: {self.score}")
        print(f"Health: {self.health}/{self.max_health} | XP: {self.experience}/{self.exp_to_next_level}")
        print(f"{'='*50}\n")
    
    def level_up(self):
        self.player_level += 1
        self.experience = 0
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
        self.max_health += 20
        self.health = self.max_health
        self.print_slow(f"🎉 LEVEL UP! You are now Level {self.player_level}! 🎉")
        time.sleep(1)
    
    def challenge_print(self, text):
        print(f"\n💻 CHALLENGE 💻")
        print("-" * 40)
        self.print_slow(text)
        print("-" * 40)
    
    def get_user_code(self):
        print("\n📝 Enter your Python code below:")
        print("Type 'HELP' for hints, 'SKIP' to skip (costs 20 HP), or your code:")
        code = input(">>> ").strip()
        return code
    
    def run_challenge(self, challenge_num):
        if challenge_num == 1:
            self.challenge_print("""
LESSON 1: PRINT STATEMENTS & VARIABLES

Write code that:
1. Prints "Hello, Python Quest!"
2. Creates a variable 'player_name' with your name
3. Prints "Welcome, [player_name]!"

Example output:
Hello, Python Quest!
Welcome, Alice!
            """)
            
            code = self.get_user_code()
            
            if code.lower() == 'help':
                print("\n💡 HINT: Use print() and create a variable like: player_name = 'YourName'")
                return self.run_challenge(1)
            
            if code.lower() == 'skip':
                self.health -= 20
                return False
            
            try:
                exec(code)
                print("\n✅ SUCCESS! Your code ran perfectly!")
                self.score += 25
                self.experience += 25
                return True
            except:
                print("\n❌ Code had errors. Try again!")
                self.health -= 10
                return False
                
        elif challenge_num == 2:
            self.challenge_print("""
LESSON 2: MATH & DATA TYPES

Create variables:
- health = 100
- attack = 25
- potion = 50

Then print: "Total power: [health + attack + potion]"
            """)
            
            code = self.get_user_code()
            
            if code.lower() == 'help':
                print("\n💡 HINT: Use + for addition. health + attack + potion")
                return self.run_challenge(2)
            
            if code.lower() == 'skip':
                self.health -= 20
                return False
            
            try:
                exec(code)
                if 'health' in locals() and 'attack' in locals() and 'potion' in locals():
                    power = health + attack + potion
                    print(f"\n✅ SUCCESS! Total power: {power}")
                    self.score += 30
                    self.experience += 30
                    return True
                else:
                    raise Exception()
            except:
                print("\n❌ Missing variables or error!")
                self.health -= 10
                return False
                
        elif challenge_num == 3:
            self.challenge_print("""
LESSON 3: CONDITIONALS (if/else)

Write code that:
1. Sets enemy_health = 75
2. If enemy_health > 50, print "Enemy is strong!"
3. Else print "Enemy is weak!"
            """)
            
            code = self.get_user_code()
            
            if code.lower() == 'help':
                print("\n💡 HINT: if enemy_health > 50:\n    print('Enemy is strong!')\nelse:\n    print('Enemy is weak!')")
                return self.run_challenge(3)
            
            if code.lower() == 'skip':
                self.health -= 20
                return False
            
            try:
                exec(code)
                print("\n✅ Perfect! You defeated the logic monster!")
                self.score += 35
                self.experience += 35
                return True
            except:
                print("\n❌ Syntax error! Logic monster laughs!")
                self.health -= 10
                return False
                
        elif challenge_num == 4:
            self.challenge_print("""
LESSON 4: LISTS & LOOPS

Create a list: spells = ['fireball', 'heal', 'shield']
Loop through it and print each spell numbered:
1. fireball
2. heal
3. shield
            """)
            
            code = self.get_user_code()
            
            if code.lower() == 'help':
                print("\n💡 HINT: for i, spell in enumerate(spells, 1):\n    print(f'{i}. {spell}')")
                return self.run_challenge(4)
            
            if code.lower() == 'skip':
                self.health -= 20
                return False
            
            try:
                exec(code)
                print("\n✅ Epic! You mastered loops!")
                self.score += 40
                self.experience += 40
                return True
            except:
                print("\n❌ Loop failed! Try enumerate()")
                self.health -= 10
                return False

    def play(self):
        self.clear_screen()
        self.print_slow("🌟 Welcome to PYTHON QUEST! 🌟")
        self.print_slow("Learn Python by defeating coding monsters!")
        input("\nPress Enter to begin your adventure...")
        
        challenges = [1, 2, 3, 4]
        random.shuffle(challenges)
        
        while self.health > 0 and self.player_level < 5:
            self.clear_screen()
            self.show_status()
            
            if not challenges:
                self.print_slow("🏆 You completed all challenges! You're a Python Master! 🏆")
                break
                
            challenge = challenges.pop(0)
            success = self.run_challenge(challenge)
            
            if success:
                self.print_slow("✨ Challenge complete! Gained XP!")
                if self.experience >= self.exp_to_next_level:
                    self.level_up()
            else:
                self.print_slow("💀 Challenge failed. Health lost!")
            
            if self.health <= 0:
                self.print_slow("💀 Game Over! Your Python journey ends here...")
                break
                
            input("\nPress Enter for next challenge...")
        
        self.show_final_score()
    
    def show_final_score(self):
        self.clear_screen()
        print(f"\n{'🎉 FINAL RESULTS 🎉'}")
        print(f"Level Reached: {self.player_level}")
        print(f"Total Score: {self.score}")
        print(f"Python Mastery: {'⭐⭐⭐⭐⭐' if self.player_level >= 5 else '⭐⭐⭐' if self.player_level >= 3 else '⭐⭐'}")
        
        if self.player_level >= 5:
            print("\n🏆 PYTHON MASTER ACHIEVED! 🏆")
        else:
            print("\n🔄 Try again to become a Python Master!")
        
        print("\nSkills Learned: Variables, Print, Math, If/Else, Lists, Loops")
        input("\nPress Enter to exit...")

# Start the game!
if __name__ == "__main__":
    game = PythonQuest()
    game.play()
