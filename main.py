import torch
import sys
import pickle5 as pickle

# Load
with open('vars/freqs.dat', 'rb') as f:
    freqs = pickle.load(f)
with open('vars/itos.dat', 'rb') as f:
    itos = pickle.load(f)
with open('vars/stoi.dat', 'rb') as f:
    stoi = pickle.load(f)

# model trained using bigram
def trained(n, g):
    for i in range(n):
        preds = []
        i = 0
        while True:
            p = freqs[i].float()
            p /= p.sum()
            i = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
            preds.append(itos[i])
            if i == 0:
                break
        print(''.join(preds))


# untrained model. All characters equally likely
def untrained(n, g):
    for i in range(n):
        untrainedPreds = []
        i = 0
        while True:
            p = torch.ones(27) / 27.0
            i = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
            untrainedPreds.append(itos[i])
            if i == 0:
                break
        print(''.join(untrainedPreds))

if __name__ == "__main__":

    g = torch.Generator()
    seed = g.seed()
    g.manual_seed(seed)
    args = sys.argv
    if len(args) == 3 and str(args[2]) == 'untrained':
        untrained(int(args[1]), g)
    else:
        trained(int(args[1]), g)

# $python main.py 5 untrained 
# sys.argv[1] => number of names to generate
# sys.argv[2] => specifies model (trained by default)