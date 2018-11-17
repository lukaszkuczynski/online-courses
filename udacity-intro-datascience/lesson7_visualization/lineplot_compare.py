from pandas import *
from ggplot import *

def lineplot_compare():
    df = pandas.read_csv('hr_by_team_year_sf_la.csv')
    print(ggplot(df, aes(x='yearID',y='HR', color='teamID')) + geom_line())


if __name__ == '__main__':
    lineplot_compare()