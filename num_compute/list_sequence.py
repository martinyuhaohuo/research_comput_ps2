
# this function returns a list of prime numbers less or equal to n
def find_prime(n):
    prime_list = [2]
    for i in range(3,n+1,1):
        is_prime = True
        for prime in prime_list:
            if i%prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list

# this function returns first n terms in the Recaman’s sequence
def find_recaman(n):
    term_list = [0]
    for i in range(1,n,1):
        a = term_list[-1]
        if (a-i>0) and (a-i not in term_list):
            term_list.append(a-i)
        else:
            term_list.append(a+i)
    return term_list

# this function returns the list of elements that present both in the first n terms of prime number lists and Recaman’s sequence
def find_reprime(n):
    # find first n prime numbers
    prime_list = [2]
    i = 3
    while len(prime_list) < n:
        is_prime = True
        for prime in prime_list:
            if i%prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
        i += 1
    # find first n terms of Recamen sequence
    recaman_list = find_recaman(n)
    # find intersection of two sets
    overlap = set(recaman_list).intersection(set(prime_list))
    return overlap

# this function returns all pairs of factors of a given psoitive interger in list of tuples
def find_factor(n):
    factor_list = [(i,n//i) for i in range(1,n+1,1) if  n%i == 0]
    return factor_list