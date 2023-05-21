from itertools import chain
import smelli
import flavio

gl = smelli.GlobalLikelihood()

for ll_name, ll in chain(gl.likelihoods.items(), gl.fast_likelihoods.items()):
    print(ll_name)
    print()
    for obs in ll.observables:
        match obs:
            case (name, *b):
                print(name, "with args", b)
            case name:
                print(name)
    print("-"*20)

