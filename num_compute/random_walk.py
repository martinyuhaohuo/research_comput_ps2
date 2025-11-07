import random

# this function records one dimensional random walk with n steps
def od_randwalk(step_num, random_seed = 356789):
    random.seed(random_seed)
    loc = 0
    record = [(0,0)]
    for t in range(1,step_num+1,1):
        mov = random.randint(-1,1)
        loc += mov
        record.append((t,loc))
    return record