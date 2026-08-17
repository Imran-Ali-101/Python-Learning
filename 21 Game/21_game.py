# 21 Game
import random

print("==== 21 Game ====")
print("Rule: You can choose up to 3 consecutive numbers.")
is_hard = input("Want to play hard? y/n: ")
print()

def get_computer_choice(current_last):
    remaining = 21 - current_last
    needed = (4 - (current_last % 4)) % 4
    max_take = needed if is_hard in ["y", "Y"] else random.randint(1, min(3, remaining))
    return max_take



computer_last = 0
while True:
    # User turn
    raw = input("## User input: ").split()[:3]
    if not raw:
        print("Please enter valid number")
        continue

    used = [int(x) for x in raw]

    if used[0] != computer_last+1:
        print(f"You must start with {computer_last + 1}")
        continue

    isConsecutive = all(used[i] == used[i-1] + 1 for i in range(1, len(used)))
    if not isConsecutive:
        print(f"Input should be consecutive {used}")
        continue

    user_last = used[-1]
    if user_last >= 21:
        print("You reached 21! Computer won the game.")
        break

    computer_take = get_computer_choice(user_last)
    computer_output = list(range(user_last + 1, computer_take + user_last + 1))
    computer_last = computer_output[-1]

    print(f">> Computer Output: {computer_output}")

    if computer_last >= 21:
        print("Computer reached 21! User won the match.")
        break