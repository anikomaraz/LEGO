import csv
import gzip
import pip

# pip.main(['install', 'numpy', 'pandas', 'matplotlib', 'seaborn'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# List of gzipped file paths
gz_files = ["colors.csv.gz", "elements.csv.gz", "inventories.csv.gz", "inventory_minifigs.csv.gz",
           "inventory_parts.csv.gz", "inventory_sets.csv.gz", "part_categories.csv.gz", "part_relationships.csv.gz",
            "sets.csv.gz", "minifigs.csv.gz", "themes.csv.gz", "parts.csv.gz"]

for file_path in gz_files:
    data = []

    # Open the gzipped file
    with gzip.open(file_path, "rt") as file:
        reader = csv.reader(file) # CSV header
        columns = next(reader) # for header row
        for row in reader:
           data.append(row)

    # Create a pandas DataFrame
    df_name = file_path.split(".")[0]  # Extract filename without extension
    globals()[df_name] = pd.DataFrame(data, columns = columns)

# so now we have the following list of datasets:
lego_datasets = ["colors", "elements", "inventories", "inventory_minifigs", "inventory_parts", "inventory_sets", "part_categories", "part_relationships",
                 "sets", "minifigs", "themes", "parts"]



# plot set numbers over time
sets_num_agg = sets[['year', 'set_num']].groupby(['year']).agg('count')
# plot.tick_params(axis='x', labelrotation = 45)
plt.plot(sets_num_agg['year'].values, sets_num_agg['set_num'].values)
# plt.show()



# sets_num_agg = sets[['year', 'set_num']].groupby(['year']).agg('count')
# sns.set_theme(style = 'whitegrid')
# plot = sns.scatterplot(x = 'year',
#                     y = 'set_num',
#                     data = sets_num_agg)
# plot.tick_params(axis='x', labelrotation = 45)
# plot.set_title("Set numbers increase over time", fontsize = 30)
# plt.show()

