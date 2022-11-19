import matplotlib.pyplot as plt
import pickle5 as pickle

# Load
with open('vars/freqs.dat', 'rb') as f:
    freqs = pickle.load(f)
with open('vars/itos.dat', 'rb') as f:
    itos = pickle.load(f)
with open('vars/stoi.dat', 'rb') as f:
    stoi = pickle.load(f)


plt.figure(figsize=(16,16))
plt.imshow(freqs, cmap='Blues', aspect='auto')
for i in range(27):
    for j in range(27):
        chstr = itos[i] + itos[j]
        plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
        plt.text(j, i, freqs[i, j].item(), ha='center', va='top', color='gray')
        
plt.axis('off')
plt.show(block=True)
