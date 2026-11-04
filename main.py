from game import is_valid_direction

choice = ""
move = 0
move_limit = 3
while choice != "quit":
    choice = input("direction (north/south/quit): ").lower().strip()
    if is_valid_direction(choice):
        move = move + 1
        print(f"Move so far: {move}")
        moves_left = move_limit - move
        print(f"Moves_left: {moves_left}")
        if move == move_limit:
            print("Out of move")
            break
    elif choice == "quit":
        break
    else:
        print("invalid option")

print("goodbye")

