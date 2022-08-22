import pandas as pd

Dic1 = {'Janet': [1, 2, 3, 4]}
Dic2 = {'Riza:': [1, 2, 3, 4]}

listOutput = []

listOutput.append(Dic1)
listOutput.append(Dic2)

print('Appeneded list: ', listOutput)

test = pd.concat([pd.DataFrame(x) for x in listOutput], axis=1)
print(test)