import torch

g = torch.Generator()
seed = g.seed()
g.manual_seed(seed)
print(seed, g)
