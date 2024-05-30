ending=", doo-doo"*3
sharks=["Baby", "Mommy", "Daddy", "Granma", "Granpa"]
moves=["Let's go hunt", "Run away", "Safe at last", "It's the end"]

for shark in sharks:
  print("{}{} shark\n".format(("{} shark{}\n".format(shark, ending) * 3), shark))

for move in moves:
  print("{}{}\n".format(("{}{}\n".format(move, ending) * 3), move))
