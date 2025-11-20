"""Week 5 DRY exercise"""


def start_scene():
 print("You are in a dark forest. You see two paths.")
 choice1 = input("Do you go 'left' or 'right'? ")
 if choice1 == 'left':
     left_path_scene()
 elif choice1 == 'right':
     right_path_scene()
 else:
  print("Invalid choice. You are lost.")
     
def left_path_scene():
 print("You walk down the left path and find a river.")
 choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
 if choice2 == 'swim':
  print("You are tired from swimming and rest. You win!")
 elif choice2 == 'follow':
  print("You follow the river bank and find a hidden cave. You win!")
 else:
  print("Invalid choice. You are lost.")

def right_path_scene():
 print("You walk down the right path and encounter a sleeping bear.")
 choice2 = input("Do you 'tiptoe' past or 'run' away? ")
 if choice2 == 'tiptoe':
    print("You successfully sneak past the bear. You win!")
 elif choice2 == 'run':
  print("You trip while running and the bear wakes up. You lose.")
 else:
  print("Invalid choice. You are lost.")
  
  
start_scene()
