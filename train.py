import torch
import pickle5 as pickle

# load names (from cli)
names = open('names.txt', 'r').read().splitlines()
names[:] = (n.lower() for n in names)

# string to int map (stoi)
chars = sorted(list(set(''.join(names))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0

# int to string map (itos) — for visualization
itos = {i:s for s,i in stoi.items()}

# creating a 27x27 tensor to store the counts (a–z chars + . token)
freqs = torch.zeros((27, 27), dtype=torch.int32)

# count frequencies
for n in names:
    ch = ['.'] + list(n) + ['.']
    for c1, c2 in zip(ch, ch[1:]):
        i = stoi[c1]
        j = stoi[c2]
        freqs[i, j] += 1

# store 'trained' tensor
with open('vars/freqs.dat', 'wb') as f:
    pickle.dump((freqs), f)

# store 'trained' tensor
with open('vars/itos.dat', 'wb') as f:
    pickle.dump((itos), f)

# store 'trained' tensor
with open('vars/stoi.dat', 'wb') as f:
    pickle.dump((stoi), f)