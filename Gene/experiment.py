from genetic import *

password = 'ascii'  # a password consisting of letters and numbers

MIN_LEN = 2
MAX_LEN = 10
POPULATION = 100
BEST_SAMPLE = 20
LUCKY_SAMPLE = 20
NUMBER_CHILD = 5
MUTATE_PERCENT = 10

COUNT = 1

# create initial population
pop = generate_population(POPULATION, MIN_LEN, MAX_LEN)

while True:
    print('\n=====Generation #{0}====='.format(COUNT))
    print('\n[Sample Group Performance Measurement]')
    pop_sorted, predict_len = compute_performance(password, pop)
    print(' best performance specimen: ', pop_sorted[0])
    print(' predicted password length: ', predict_len)

    if int(pop_sorted[0][1] == 100):
        print('\n=====Learning End=====')
        print('\n[ANSWER] password:', pop_sorted[0][0])
        break

    print('\n[Survival Group Formation]')
    survivors = select_survivors(pop_sorted, BEST_SAMPLE, LUCKY_SAMPLE, predict_len)
    print(' part of the survival group created: ', survivors[:3])
    print(' survival group length generated: ', len(survivors))

    print('\n[Survival Group Mating]')
    children = mating(survivors, NUMBER_CHILD)
    print(' part of the child group created: ', children[:3])
    print(' child group length generated: ', len(children))

    print('\n[Mutate]')
    new_generation = mutate_population(children, MUTATE_PERCENT)
    print(' population after mutation: ', len(new_generation))

    pop = new_generation

    COUNT += 1
