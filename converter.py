import gdxpds
import pandas as pd


gdx_file = 'Opgave_E5.gdx'
dataframes = gdxpds.to_dataframes(gdx_file)
for symbol_name, df in dataframes.items():
    print("Doing work with {}.".format(symbol_name))
    pd.DataFrame(df).to_excel('test.xls')

