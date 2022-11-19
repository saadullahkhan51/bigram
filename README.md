Implementing a character level bigram language model
## Requirements
* Pytorch
* Matplotlib
* pickle5

> Use `python3` if you have python3...

## Training
use train.py to train the model on a list of names.
```
$python train.py
```
You can pass a file as the second cli argument. Default names file is `names.txt` present in the repo
The frequency tensor (`freqs`), along with some other stuff, gets pickled and stored in the `vars` folder.

## Generating
`main.py` generates names using `freqs`. The first argument specifies number of names to generate. The second is optional and can be used to call an "untrained" model. This is just for comparison.
```
$python main.py 5
```
The trained model is called by default but can be specified as well. Usage for untrained model:
```
$python main.py 5 untrained
```

## Visualizer
Use visualizer to get a nice image that shows all the bigrams and their frequencies.
```
$python visualizer.py
```
