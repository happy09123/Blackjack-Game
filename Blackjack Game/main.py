import random
from replit import clear 
# ^^^^^^^^^^^^^^^^^^^^^^
# You can just remove ^^ if you aren't using replit.

def deal_cards(person, n=1):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(n):
        person.append(cards[random.randint(0, len(cards) - 1)])

def calculate_score(people):
    if (11 in people[0]["cards"] and sum(people[0]["cards"]) > 21):
      people[0]["cards"][people[0]["cards"].index(11)] = 1
    elif (11 in people[1]["cards"] and sum(people[1]["cards"]) > 21):
      people[1]["cards"][people[1]["cards"].index(11)] = 1
    elif (sum(people[0]["cards"]) == 21 or sum(people[1]["cards"]) == 21):
      print(f"Your final hand: {people[0]['cards']}, final score: {people[0]['score']}\nComputer's final hand: {people[1]['cards']}, final score: {people[1]['score']}")
      if (sum(people[0]["cards"]) == 21):
          people[0]["score"] = 0
          print("Win, you have a Blackjack")
      elif (sum(people[1]["cards"]) == 21):
          people[1]["score"] = 0
          print("Lose, the dealer has a Blackjack")
      return True
    people[0]["score"] = sum(people[0]["cards"])
    people[1]["score"] = sum(people[1]["cards"])

def compare(person1, person2):
    finish = False
    text = [f"Your final hand: {person1['cards']}, final score: {person1['score']}\nComputer's final hand: {person2['cards']}, final score: {person2['score']}"]
    if (person1["score"] == person2["score"]):
      if (person2["score"] > 17):
        text.append("Draw")
        finish = True
    elif (person1["score"] > 21 or person2["score"] > 21):
      if (person1["score"] > 21):
        text.append("You went over. You lose")
      else:
        text.append("The dealer went over. You win")
      finish = True
    elif (person1["score"] > person2["score"] or person1["score"] < person2["score"]):
      if (person2["score"] > 17):
        if (person1["score"] > person2["score"]):
          text.append("You win.")
        else:
          text.append("You lose.")
        finish = True
    if (finish):
      print("\n".join(text))
    return finish

def restartCards(person1, person2):
    deal_cards(person1["cards"], 2)
    deal_cards(person2["cards"], 2)
    return calculate_score([person1, person2])

players = [
  {
    "cards": [],
    "score": "",
  },
  {
    "cards": [],
    "score": "",
  }
]

finished = [False, True]
while not finished[0]:
  [players[0], players[1]] = [{"cards": [], "score": ""}, {"cards": [], "score": ""}]
  if (restartCards(players[0], players[1])):
    finished[1] = True
  while not finished[1]:
    print(f"Your cards: {players[0]['cards']}, current score: {players[0]['score']}")
    print(f"Computer's first card: {players[1]['cards'][0]}")
    question = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if ('y' in question):
      deal_cards(players[0]["cards"])
      calculate_score(players)
    elif ('n' in question):
      if (players[1]["score"] < 17):
        deal_cards(players[1]["cards"])
        calculate_score(players)
    print(players[0], players[1])
    if (compare(players[0], players[1])):
      break
  
  choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if ("y" in choice1):
    finished[0] = False
    finished[1] = False
    clear() # Also remove this if you removed the import.
  else:
    finished[0] = True
    finished[1] = True
