"""Week 5 Task 2"""

player_score = 0
def add_points(current_score):
 new_score = current_score + 10
 print(f"[Inside Function] Score is now: {new_score}")
 return new_score #send the new score back

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
player_score = add_points(player_score)
print(f"[Outside] Player score is: {player_score}")