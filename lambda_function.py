import pandas as pd


def lambda_handler(event, context):
    alphabet = {'column1': [1, 2, 3], 'column2': [
        4, 5, 6], 'column3': [7, 8, 9]}
    df = pd.DataFrame(data=alphabet)
    print(df)
    print('Done!')
