from itertools import product
import pandas as pd


def insert_dots(input_str):
    result = []
    posibility = []
    charecters = [char for char in input_str]
    for i in range(len(input_str)-1):
        posibility.append(0)
    possible_lists = list(product([0, 1], repeat=len(posibility)))
    for possible_list in possible_lists:
        modified_str = ''.join(f'{elem1}.' if elem2 == 1 else elem1 for elem1, elem2 in zip(charecters, possible_list))
        result.append(modified_str + input_str[-1] + '@gmail.com')
    return result


input_str = "sdf123"
result = insert_dots(input_str)
df = pd.DataFrame(result, columns=['Gmail'])
print(df)
df.to_csv('gmail.csv')
df.to_excel('gmail.xlsx')