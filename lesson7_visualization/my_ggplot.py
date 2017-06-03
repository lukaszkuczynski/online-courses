from ggplot import aes, ggplot, geom_point, geom_line
import pandas as pd

def draw():
    df = pd.read_csv("turnstile_data_master_with_weather.csv")
    gg = ggplot(df, aes("TIMEn","ENTRIESn_hourly")) + geom_point()
    print(gg)

if __name__ == '__main__':
    draw()

