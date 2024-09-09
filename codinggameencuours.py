import sys
import math

# Send your busters out into the fog to trap ghosts and bring them home!

busters_per_player = int(input())  # the amount of busters you control
ghost_count = int(input())  # the amount of ghosts on the map
my_team_id = int(input())  # if this is 0, your base is on the top left of the map, if it is one, on the bottom right

# game loop


while True:
    entities = int(input())  # the number of busters and ghosts visible to you
    ghosts = []
    busters = []

    for i in range(entities):
        # entity_id: buster id or ghost id
        # y: position of this buster / ghost
        # entity_type: the team id if it is a buster, -1 if it is a ghost.
        # state: For busters: 0=idle, 1=carrying a ghost.
        # value: For busters: Ghost id being carried. For ghosts: number of busters attempting to trap this ghost.
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]
        if entity_type == -1:
            ghosts.append((entity_id, x, y, state, value))
        if entity_type == my_team_id:
            busters.append((entity_id, x, y, state, value))

    for i in range(busters_per_player):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # MOVE x y | BUST id | RELEASE
        print(ghosts)
        print("l y a", busters)
        print("MOVE 8000 4500")