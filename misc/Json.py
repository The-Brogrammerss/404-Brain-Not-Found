import json
def to_json(gnome):

    with open('best.json', 'w') as jsonfile:
        s = json.dumps(gnome, default=lambda gnome: gnome.__dict__,
                          sort_keys=True, indent=4)
        jsonfile.write(s)
        jsonfile.close()


def load_config(str):
    # with open('config.json', 'r') as obj:
    #     obj = json.load(obj)
    #     print(obj)
    obj = open("config.json")
    return obj
