import pandas as pd

def get_config():
    res = {}
    res['PATH'] = './data/N510.csv'
    return res

def main():
    config = get_config()
    path = config['PATH']

    data = pd.read_csv(path, sep='\t')

    res = {
        'R1':{},
        'R2':{},
        'R3':{},
        'R4':{}
    }
    for i in range(data.shape[0]):
        row = data.iloc[i]
        # print(i)
        if not row['RB'] in res[row['RA']]:
            res[row['RA']][row['RB']] = row['response']
        else:
            res[row['RA']][row['RB']] += row['response']

    print(res)

if __name__ == "__main__":
    main()