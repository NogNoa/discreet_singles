import pathlib

tumbler = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {"tumblr": {}, "other": {}}
for file in tumbler.iterdir():
    tag, _, rest = file.name.partition("_")
    if tag == "tumblr":
        name, _, rest = rest.partition("_")
        hash, _, rest = rest.partition("_")
        size = int(rest.partition(".")[0])
        try:
            fili["tumblr"][name] += {hash: size}
        except KeyError:
            fili["tumblr"][name] = {hash: size}
    elif rest:
        name, _, rest = rest.partition("_")
        size = int(rest.partition(".")[0])
        if tag in fili.keys():
            if name in fili[tag].keys():
                fili[tag][name].append(size)
            else:
                fili[tag] += {name: [size]}
        else:
            fili[tag] = {name: [size]}
    else:
        fili["other"] += tag
