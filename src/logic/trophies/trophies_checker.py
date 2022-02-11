import json

from logic.trophies.trophies import trophies
from utils.translation.i18n import i18n


def check_trophies_bk(score_history):
    filename = 'assets/resources/trophies.json'
    with open(filename, "r") as file:
        saved_trophies = json.load(file)
    not_obtained_trophies_names = set(
        [t["name"] for t in saved_trophies if not t["obtained"]])
    for name, trophy in trophies.items():
        trophy.check(score_history)
    with open(filename, "w") as file:
        file.write(json.dumps([vars(t) for t in trophies.values()], indent=4))
    obtained_trophies_names = set(
        [t.name for t in trophies.values() if t.obtained])
    new_trophies_names = obtained_trophies_names.intersection(
        not_obtained_trophies_names)
    return {n: t for n, t in trophies.items() if n in new_trophies_names}


def check_trophies(score_history):
    checked_trophies = dict()
    for name, trophy in trophies.items():
        additional_params = vars(trophy)
        checked_trophies[name] = {
            "name": i18n._(trophy.name, **additional_params),
            "description": i18n._(trophy.description, **additional_params),
            "image": trophy.image,
            "obtained": trophy.check(score_history)
        }
    return checked_trophies


def compute_trophies_diff(old_trophies, new_trophies):
    trophies_diff = dict()
    for name, new_trophy in new_trophies.items():
        new_obtained = new_trophy["obtained"]
        if new_obtained and new_obtained != old_trophies[name]["obtained"]:
            trophies_diff[name] = new_trophy
    return trophies_diff
