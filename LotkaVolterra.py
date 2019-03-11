prey_growthrate = float(input("What is the preys rate of growth: "))
predation = float(input("What is the rate at which predators kill: "))
predator_deathrate = float(input("What is the predators death rate: "))
predator_growthrate = float(input("what is the predators rate of growth: "))

'''
prey_growthrate = .1 [it is the rate at which prey birth exceeds natural death]
predation = .01 [the rate at which the predator hunts the prey]
predator_deathrate = .01[the rate which natural predator deaths exceeds births, due to prey population falling]
predator_growthrate = .0002 [the rate which predator birth increases due to prey population rising]
'''

prey_population = float(input("What is the prey population: "))
predator_population = float(input("What is the predator population: "))

population_cycles = int(input("How Many Periods Would You Like To Pass: "))

for i in range(population_cycles):
    dprey = (prey_growthrate*prey_population) - (predation*prey_population*predator_population)
    dpred = (predator_growthrate*prey_population*predator_population) - (predator_deathrate*predator_population)

    prey_population = prey_population + dprey
    predator_population = predator_population + dpred

    print("Your Prey Population after", i, "is", prey_population)
    print("Your Predator Population after", i, "is", predator_population)