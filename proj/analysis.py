import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('626_annot.csv')

x = [-1, -.75, -.5, -.25, 0, .1, .2, .3, .4, .5]
gpt = defaultdict(list)
bert = defaultdict(list)

for typ in ["Gender", "Race", "Religion"]:
    g = df[df.type == typ]
    l = len(g)
    for frac in x:
        gpt[typ].append((((g.p_unrelated_gpt - g.p_anti1_gpt) > frac * g.p_anti1_gpt).sum()) / l)
        bert[typ].append((((g.p_unrelated_bert - g.p_anti1_bert) > frac * g.p_anti1_bert).sum()) / l)

k = sns.lineplot(data=gpt)
k.set_xticks(range(len(x)))
k.set_xticklabels(x)
k.set_ylabel('% of higher scoring unrelated sents')
k.set_xlabel('Tolerance')
k.figure.savefig('3.gpt.png')

##

gpt, bert = list(), list()
for typ in ['Gender', 'Race', 'Religion']:
    g = df[df.type == typ]
    l = len(g)
    gpt.append((abs(g.p_stereotype_gpt - g.p_anti1_gpt) < (g.p_anti1_gpt * .1)).sum()/l)
    bert.append((abs(g.p_stereotype_bert - g.p_anti1_bert) < (g.p_anti1_bert * .1)).sum()/l)
c = pd.DataFrame.from_dict({'gpt': gpt, 'bert': bert})
plt.figure(figsize=(10, 6))
sns.barplot(x="", hue="kind", y="data", data=c)
plt.show()
