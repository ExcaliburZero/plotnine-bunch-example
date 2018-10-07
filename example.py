from plotnine import *

import pandas as pd

def main():
    file_name = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    data = pd.read_csv(file_name)

    plot = ggplot(data, aes("sepal_length", "sepal_width")) +\
        geom_point()

    ggsave(plot=plot, filename="example.png")

if __name__ == "__main__":
    main()
