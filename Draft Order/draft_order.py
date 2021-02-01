# This is a program that creates a random order for your fantasy sports league.

import random, time

teams = []

league_size = int(input("Enter your league size: "))
draft_spots = league_size

while not league_size == 0:
    team_name = input("Enter team name: ")
    teams.append(team_name)
    league_size -= 1
print("\n")
draft_order = input("Press Enter for your Draft Order")
print("\n")
print("======================")
while not draft_spots == 0:
    random_team = random.choice(teams)
    if len(teams) == 0:
        break
    else:
        print(draft_spots,random_team)
        print("======================")
        draft_spots -= 1
        teams.remove(random_team)
        time.sleep(1)

print("\n")
exit = input("Here is your draft order! Press enter to exit.")
