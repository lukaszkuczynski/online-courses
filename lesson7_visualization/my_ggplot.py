from ggplot import aes, ggplot, geom_point, geom_line
import pandas as pd

def draw():
    df = pd.read_csv("turnstile_data_master_with_weather.csv")
    gg = ggplot(aes(x="EXITSn_hourly",y="ENTRIESn_hourly"), data=df) + geom_line()
    print(gg)

if __name__ == '__main__':
    draw()

