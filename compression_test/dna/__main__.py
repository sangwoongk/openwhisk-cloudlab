from time import time
import random
import squiggle

sequence = None
result = None

def generate_dna_sequence(length):
    random.seed(42)
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(bases) for _ in range(length))


def visualize(dna_len):
    global sequence, result
    if sequence is None:
        sequence = generate_dna_sequence(dna_len)
    result = squiggle.transform(sequence)
    return result


def main(params):
    global result
    dna_size = params['size']

    start = time()

    result = visualize(dna_size)
    latency = time() - start
    ret_val = {}
    ret_val["delay"] = latency

    return ret_val

if __name__ == '__main__':
    params = {'size': 1500000}
    main(params)