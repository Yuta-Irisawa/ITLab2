import argparse
import datetime
import os
import pandas as pd

def main(input_file, window_size):
    df = pd.read_csv(input_file, header=None, names=['datetime', 'x', 'y', 'z'])

    df['datetime'] = pd.to_datetime(df['datetime'], format="%Y/%m/%d-%H:%M:%S:%f")
    startDatetime = df['datetime'].head(1).values[0]
    df['deltaDatetime'] = df['datetime'] - startDatetime
    df = df.loc[df.deltaDatetime <= window_size, :]
    df = df.loc[:, :'z']
    os.makedirs("output", exist_ok=True)
    df.to_csv(path_or_buf=f"./output/{input_file.split('/')[-1]}", index=False, header=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="input file's path.")
    parser.add_argument("--window-size", required=True, help="How many seconds should be cut out from the beginning?")
    args = parser.parse_args()

    input_file = args.input_file
    window_size = int(args.window_size)

    window_size = datetime.timedelta(seconds=window_size)
    main(input_file, window_size)