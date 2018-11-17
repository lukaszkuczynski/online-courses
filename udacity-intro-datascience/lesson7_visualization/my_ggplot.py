from ggplot import aes, ggplot, geom_point, geom_line
import pandas as pd

def draw():
    df = pd.read_csv("turnstile_data_master_with_weather.csv")
    df['fogg'] = df['fog'].astype(int)
    gg = ggplot(aes(x="EXITSn_hourly",y="ENTRIESn_hourly", color='fogg'), data=df) + geom_line()
    print(gg)

if __name__ == '__main__':
    draw()

