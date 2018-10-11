from metrics import *
from tokenizers import *

# evaluation

nist, bleu, entropy, avg_len = nlp_metrics(
	path_refs=['demo/ref0.txt', 'demo/ref1.txt'], 
	path_hyp='demo/hyp.txt')

print(nist)
print(bleu)
print(entropy)
print(avg_len)

bleu = cal_bleu(
	path_refs=['demo/ref0.txt', 'demo/ref1.txt'], 
	path_hyp='demo/hyp.txt')
print(bleu)

# tokenization 

s = " I don't know:). how about this?https://github.com/golsun/deep-RL-time-series"
print(clean_str(s))