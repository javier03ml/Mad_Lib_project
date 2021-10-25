# This is a MadLib Games.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Second verb: ")
monster= input("Monster: ")

madlib = "I love Halloween! It's very {adj}. Witches {verb1} across the skies and Vampires {verb2} through the night.Even the neighbor is a {monster}!".format(adj = adj, verb1 = verb1, verb2 = verb2, monster = monster)

print(madlib)