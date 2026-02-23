import pandas as pd


def test_json_to_dataframe(data: dict):
    df = pd.DataFrame.from_dict(data["player_stats"], orient="index")
    return df