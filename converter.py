from os import path
import gdxpds
import pandas as pd
import os


class converter:
    def __init__(self, path):
        self.path = path

    def convert_file(self, path):
        dataframes = gdxpds.to_dataframes(path)
        for symbol_name, df in dataframes.items():
            print("Doing work with {}.".format(symbol_name))
            path = path.strip('.gdx') + '.xls'
            pd.DataFrame(df).to_excel(path)

    def convert(self):
        if os.path.isfile(self.path):

            if path.endswith('.gdx'):
                self.convert_file(self.path)
            else:
                return "Not supported file format"
        else:
            for subdir, dirs, files in os.walk(self.path):
                for file in files:
                    self.convert_file(self.path + '/' + file)


