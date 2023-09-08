from os import makedirs
from itertools import chain
import smelli
import flavio

base_dir = "obs"
smelli_ver = smelli.__version__
folder = f"{base_dir}/{smelli_ver}"
makedirs(folder, exist_ok=True)

observables_header = """---
layout: default
title: Observables - {0}
---

# List of all observables included in {0}

{{: class="table"}}
| Symbol | Name | Arguments | SM Prediction |
|--------|------|-----------|---------------|
"""

gl = smelli.GlobalLikelihood()
for ll_name, ll in chain(gl.likelihoods.items(), gl.fast_likelihoods.items()):
    print(f"Writing {ll_name}")
    with open(f"{folder}/{ll_name}.md", "w") as f:
        f.write(observables_header.format(ll_name))
        for obs_info in ll.observables:
            # Either a string with the name of the obs, or a tuple whose first 
            # element is the name, and others are the arguments passed.
            # For python3.10+, we can use match case since I just think they're neat
            match obs_info:
                case (name, *args):
                    pass
                case name:
                    args = None
            o = flavio.Observable[name]
            text = f"| {o.tex} | `{o.name}` | "
            if args:
                args_info = zip(o.arguments, args)
                text += ", ".join(f"{name} = {value}" for name, value in args_info)
            text += " |"
            if args:
                text += f"{flavio.sm_prediction(name, *args)} | \n"
            else:
                text += f"{flavio.sm_prediction(name)} | \n"
            f.write(text)



index_header = """---
layout: default
title: Likelihoods in smelli v{0}
---

# List of likelihoods in smelli v{0}

"""

print(f"Writing index for smelli v{smelli_ver}")
with open(f"{folder}/index.md", "w") as f:
    f.write(index_header.format(smelli_ver))
    for ll_name in chain(gl.likelihoods.keys(), gl.fast_likelihoods.keys()):
        f.write("[{0}]({0})\n\n".format(ll_name))
