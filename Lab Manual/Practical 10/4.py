import pandas as pd
data = {'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)
r = df.apply(lambda x: x ** 2)
r.insert(0, '0', range(len(r)))
r.set_index('0', inplace=True)
print(r)
