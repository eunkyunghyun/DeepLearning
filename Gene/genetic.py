# Set password

import random
import string

# A function that generates a peculiar password.

def generate_word(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, k=length))

# A function that generates initial population.

def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        length = i % (max_len - min_len + 1) + min_len
        population.append(generate_word(length))
    return population

# A function that evaluates the object's fitness.

def fitness(original_word, test_word):
    score = 0

    # If the length's different, the genetic evaluation score is assessed as 0.
    if len(original_word) != len(test_word):
        return score

    # If the length's the same as it, it'll add to 0.5 points.
    len_score = 0.5
    score += len_score

    # Add one point if the string's the same for each digit.
    for i in range(len(original_word)):
        if original_word[i] == test_word[i]:
            score += 1

    # It's converted to 100 points and returned.
    return (score / (len(original_word) + len_score)) * 100

# A function that evaluates goodness of fit for each of objects and adds scores to the list.

def compute_performance(original_word, population):
    performance_list = []
    predict_len = 0

    for word in population:
        score = fitness(original_word, word)

        # if the score is not 0, the length of the original password is found.
        if score != 0:
            predict_len = len(word)

        performance_list.append([word, score])

    population_sorted = sorted(performance_list, key=lambda x: x[1], reverse=True)

    return population_sorted, predict_len

# A function that creates a survival group with a good score among each of individuals.

def select_survivors(population_sorted, best_sample_size, lucky_sample_size, password_len):
    next_generation = []

    # Insert good factor to the list.
    for i in range(best_sample_size):
        if population_sorted[i][1] > 0:
            next_generation.append(population_sorted[i][0])

    # Insert survivors from the list.
    lucky_survivors = random.sample(population_sorted, k=lucky_sample_size)
    for survivor in lucky_survivors:
        next_generation.append(survivor[0])

    # Add a random password if the length of the next_generation is smaller than the best_sample_size and lucky_sample_size combined.
    while len(next_generation) < best_sample_size + lucky_sample_size:
        next_generation.append(generate_word(password_len))

    random.shuffle(next_generation)

    return next_generation

# A function that creates new objects by crossing two objects.

def create_child(mom, dad):
    # Receive two objects and create children by mixing one character of mom and dad with 50% probability based on the small object.
    child = ''
    min_len = min(len(mom), len(dad))

    for i in range(min_len):
        point = random.randint(1, 2)
        if point == 1:
            child += mom[i]
        else:
            child += dad[i]

    return child


# A function that selects two of the survivors as children and returns a list.
# If the initial population was 100 and the survivor was 40, the number_child should be set to 5 to make the next group 100.

def mating(survivors, number_child):
    next_population = []

    for i in range(int(len(survivors)/2)):
        for j in range(number_child):
            next_population.append(create_child(survivors[i], survivors[len(survivors) - i - 1]))

    return next_population

# A function that creates mutant objects.

def mutate_word(word):
    index = random.randint(0, len(word)-1)
    change_char = random.choice(string.ascii_letters + string.digits)
    if index == 0:
        word = change_char + word[1:]
    else:
        word = word[:index] + change_char + word[index+1:]
    return word

# A function that generates mutant individuals with a certain probability in the population.

def mutate_population(population, mutate_percent):
    for i in range(len(population)):
        if random.randint(0, 100) < mutate_percent:
            population[i] = mutate_word(population[i])
    return population
