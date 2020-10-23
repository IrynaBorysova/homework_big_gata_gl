import pandas as pd
from pandas import merge

df = pd.read_csv(r'test-task_dataset_summer_products.csv')
mean1 = df.groupby(['origin_country']).agg({'price': 'mean'})

def divide_two_cols(df_sub):
    if not float(df_sub['rating_count'].sum()):
        return 0
    else:
        return df_sub['rating_five_count'].sum() * 100 / float(df_sub['rating_count'].sum())


ratios = df.groupby('origin_country').apply(divide_two_cols)
print(merge(
    mean1, ratios.reset_index(name='five_percentage'),
    on="origin_country"))