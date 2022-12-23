import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.combinatorics import Permutation

from src.math_library.monoid_elements_generator import MonoidElementsGenerator
import src.math_library.positive_bt_permutations as positive_bt_permutations

"""
With this function we create the dataset.
The function create_dataset takes two inputs: a numpy array (containing all the vectors representing the positive elements that we will put 
dataset) and a string (containing the path of the csv to be created).
"""
def create_dataset(monoid_elements: np.ndarray, csv_path: str) -> None:
    _, width = monoid_elements.shape
    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([
            'leaves',
            *['x' + str(i) for i in range(width)],
            'bottom_permutation',
            'top_permutation',
            'permutation',
            'orbits'
        ])
        for i in range(len(monoid_elements)):
            monoid_element = np.array(monoid_elements[i][:])
            # monoid_element = np.insert(monoid_element, 0, 1, axis=0)
            number_of_leaves = positive_bt_permutations.number_of_leaves(
                monoid_element)
            bottom_permutation = Permutation(
                positive_bt_permutations.bottom_permutation(number_of_leaves))
            top_permutation = Permutation(
                positive_bt_permutations.top_permutation(number_of_leaves, monoid_element))
            whole_permutation = positive_bt_permutations.whole_permutation(
                number_of_leaves, monoid_element)
            writer.writerow(
                [number_of_leaves] +
                [monoid_element[i] for i in range(width)] +
                [bottom_permutation, top_permutation,
                    whole_permutation, len(whole_permutation)]
            )

"""
This function takes the whole data set "data_final.csv" (available at https://zenodo.org/record/7424881) 
and produces a dataset of smaller height and width.
csv_path is the location of the file "data_final.csv" in the computer.
"""
def reduce_data_set(width: int, height: int, csv_path: str) -> pd.DataFrame:
  df = pd.read_csv(csv_path)
  df = df[df.apply(lambda row: all(column <= height for column in row[2:width+2]), axis=1)]
  df = df[df.apply(lambda row: all(column == 0 for column in row[width+2:9]), axis=1)]
  return df
            
    
"""
This function plots the data contained in the csv file (stored in "csv_path"). 
It also determines the largest and smallest class of permutations in the file.
"""
def plot_data(csv_path: str) -> None:
  df = pd.read_csv(csv_path)
  df = df.groupby('orbits')['orbits'].count()
  print("The largest class is:", df.idxmax())
  print("The smallest class is:", df.idxmin())
  df.plot()
  plt.xlabel('number of orbits')
  plt.ylabel('number of permutations')
  plt.legend()


            
if __name__ == '__main__':
    HEIGHT = 2
    WIDTH = 2
    
    csv_path = 'data_w' + str(WIDTH) + 'h' + str(HEIGHT) + '.csv'

    monoid_elements = MonoidElementsGenerator(
        HEIGHT, WIDTH).generate_monoid_elements()

    create_dataset(monoid_elements, csv_path)
