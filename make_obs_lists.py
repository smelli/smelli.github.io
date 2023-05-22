from itertools import chain
import smelli
import flavio

gl = smelli.GlobalLikelihood()

for ll_name, ll in chain(gl.likelihoods.items(), gl.fast_likelihoods.items()):
    print(ll_name)
    print()
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
        text = f"{o.name}"
        if args:
            text += " @ "
            args_info = zip(o.arguments, args)
            text += ", ".join(f"{name} = {value}" for name, value in args_info)
        print(text)
    print("-"*20)
