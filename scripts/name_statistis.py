import pandas as pd

df = pd.read_csv("MeritList.csv")


def name_by_category(s):
    return df["Category"][
        df["Candidate's Full Name"]
        .str.lower()
        .str.contains(s)
        .map(lambda x: x if type(x) is bool else False)
    ].value_counts()


def name_counts(s):
    return df["Category"][
        df["Candidate's Full Name"]
        .str.lower()
        .str.contains(s)
        .map(lambda x: x if type(x) is bool else False)
    ].count()


def name_percentage(s):
    total_cnt = name_counts(s)
    return name_by_category(s).map(lambda x: round(x / total_cnt * 100, 2))


def name_normalised(s):
    return pd.DataFrame(name_by_category(s), name_percentage(s))


if __name__ == "__main__":
    name = input("Enter string: ")
    print("Count: ", name_percentage(name))
