import pandas as pd

Dic1 = {'Janet': [1, 2, 3, 4]}
Dic2 = {'Riza:': [1, 2, 3, 4]}
Dic3 = {'Matt': [1, 2, 3, 4]}

listOutput = []

listOutput.append(Dic1)
listOutput.append(Dic2)
listOutput.append(Dic3)

print('Appeneded list: ', listOutput)

# test = pd.concat([pd.DataFrame(x) for x in listOutput], axis=1)
s1 = pd.DataFrame(Dic1)
s2 = pd.DataFrame(Dic2)
s3 = pd.DataFrame(Dic3)
test = pd.concat([s1, s2, s3], axis=1)
print(test)