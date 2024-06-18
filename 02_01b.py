# Deque: Storing a user's most recent food orders
from collections import deque
def main():
    #add code here
    foods = deque(maxlen=5)
    foods.append("STA001")
    print(foods)
    ordered_foods = ["DES003", "STA002", "ENT001"]
    foods.extend(ordered_foods)
    foods.append("DES002")
    foods.appendleft("DES005")
    print(foods)
    return

if __name__ == "__main__":
    main()