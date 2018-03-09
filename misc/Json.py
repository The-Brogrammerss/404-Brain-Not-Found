import json
def to_json(gnome):

    with open('best.json', 'w') as jsonfile:
        s = json.dumps(gnome, default=lambda gnome: gnome.__dict__,
                          sort_keys=True, indent=4)
        jsonfile.write(s)
        jsonfile.close()


def from_jason():
    print (json.loads('coolpole.json'))
    # return json.loads('coolpole.json')