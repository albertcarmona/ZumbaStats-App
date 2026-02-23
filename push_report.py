from git import Repo
from generate_report import generate_report


test_data = {
    "number_of_players": 2,
    "player_stats": {
        "canon": {
            "play_time": 100,
            "kills": 100,
            "deaths": 100
        },
        "canon_2": {
            "play_time": 150,
            "kills": 120,
            "deaths": 80
        }
    }
}


def test_push_report():
    
    generate_report(test_data, "test_report")

    repo = Repo(".")
    repo.index.add(["data/zumba4/test_report.json"])
    repo.index.commit("Uploaded est report")
    repo.remotes.origin.push()


if __name__ == "__main__":
    test_push_report()
