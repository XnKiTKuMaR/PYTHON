# What Should I Do Tonight?

import random

# Our list of bars
bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

# Our list of friends
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Alexander Hamilton",
          "Samuel L. Jackson"
          "Swastik"]

people2 = ["Mattan",
          "Chris",
          "hsd",
          "Samuel L. Jackson",
          "Swastik"]         

random_bar = random.choice(bars)
random_person = random.choice(people)
random_p = random.choice(people2)

print(f"How about you go to {random_bar} with {random_person} and {random_p}?")
