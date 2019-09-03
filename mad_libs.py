adj_list = []

adj_1 = input(str("Type an adjective: "))
adj_2 = input(str("Type another adjective: "))
adj_3 = input(str("Another Adjective!"))

adj_list.append(adj_1)
adj_list.append(adj_2)
adj_list.append(adj_3)

noun_list = []

noun_1 = input(str("Type a noun: "))
noun_2 = input(str("Type another noun: "))
noun_3 = input(str("Another noun: "))
noun_4 = input(str("A fourth noun!"))
noun_5 = input(str("Noun!"))

noun_list.append(noun_1)
noun_list.append(noun_2)
noun_list.append(noun_3)
noun_list.append(noun_4)
noun_list.append(noun_5)

verb_list = []

verb = input(str("Type a verb: "))
verb_2 = input(str("And a Final Verb!"))

verb_list.append(verb)
verb_list.append(verb_2)






Result = "There was once a " + noun_list[0] + " and their pet " + adj_list[0] + " " + noun_list[1] + ". They woke up one morning to find out a " + adj_list[1] + " " + noun_list[2] + " had " + verb_list[0] + " all over their " + noun_list[3] + ". In response, they took out their trusty " + adj_list[2] + " " + noun_list[4] + " 3000 to " + verb_list[1] + " it up!"

print(Result)