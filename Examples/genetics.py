import random

# Initial chromosomes
chromosomes = ["00000000", "11111111", "10101010", "01010101"]

# Fitness function
def fitness(chrom):
    """Fitness = -decimal^2 + 5"""
    decimal = int(chrom, 2)
    return -decimal**2 + 5

# Selection: pick the top 2 fittest
def select_fittest(population):
    fitness_list = [fitness(ch) for ch in population]
    # Sort chromosomes by fitness descending
    sorted_pop = sorted(zip(fitness_list, population), reverse=True)
    fittest = sorted_pop[:2]  # top 2
    return [f[1] for f in fittest]

# Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation: flip a random bit
def mutate(chrom, mutation_rate=0.1):
    chrom_list = list(chrom)
    for i in range(len(chrom_list)):
        if random.random() < mutation_rate:
            chrom_list[i] = '1' if chrom_list[i]=='0' else '0'
    return ''.join(chrom_list)

# Run one generation
def run_generation(population):
    fittest_parents = select_fittest(population)
    print("Fittest parents:", fittest_parents)
    
    child1, child2 = crossover(fittest_parents[0], fittest_parents[1])
    print("Children before mutation:", child1, child2)
    
    child1 = mutate(child1)
    child2 = mutate(child2)
    print("Children after mutation:", child1, child2)
    
    # New generation: replace the least fit with new children
    population.sort(key=lambda ch: fitness(ch))
    population[0] = child1
    population[1] = child2
    return population

# Example: run 5 generations
population = chromosomes.copy()
for gen in range(5):
    print(f"\nGeneration {gen+1}")
    population = run_generation(population)
    print("New population:", population)
