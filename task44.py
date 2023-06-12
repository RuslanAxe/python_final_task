# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

from sklearn.preprocessing import MultiLabelBinarizer
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head(10)

new_df = pd.DataFrame(columns=['robot','human'])
new_df.loc[:, 'robot'] = data['whoAmI']
new_df.loc[:, 'human'] = data['whoAmI']

# penguins['bill_group'] = ['high' if value > 42 else 'middle' if 35 < value <= 42 else 'low' for value in penguins.bill_length_mm]
new_df['robot'] = ['1' if value == 'robot' else '0' for value in data.whoAmI]
new_df['human'] = ['1' if value == 'human' else '0' for value in data.whoAmI]
new_df