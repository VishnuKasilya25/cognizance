import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
for i in ser:
    v = i
    k = v.capitalize()
    print(k , end = " ")