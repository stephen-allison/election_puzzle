import itertools
# A Solver for this puzzle
# http://www.theguardian.com/science/alexs-adventures-in-numberland/2015/may/04/einsteins-election-riddle-are-you-in-the-two-per-cent-that-can-solve-it
# basically the same as the 'zebra' problem in udacity cs212

def leftof(a, b): #puzzle only solvable if this means 'immediately to left'
    return b - a == 1


def nextto(a, b):
    return abs(a-b) == 1

# basically a jumbo generator expression
# there are pow(5!,5) possible arrangements, so have to apply the constraints
# as soon as possible to get a reasonable run time
def election_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next(((nicola, ed, nick, david, nigel),
                (tartan, gingham, paisley, polkadot, striped),
                (guineapig, badger, pitbull, squirrel, fish),
                (foot, plane, bike, car, train),
                (flatwhite, espresso, chai, decaf, mocha))
                for (tartan, gingham, paisley, polkadot, striped) in orderings
                if leftof(paisley, gingham)
                for (nicola, ed, david, nick, nigel) in orderings
                if nicola is tartan
                if nick is first
                if nextto(nick, polkadot)
                for (guineapig, squirrel, badger, pitbull, fish) in orderings
                if ed is guineapig
                for (car, bike, train, foot, plane) in orderings
                if car is squirrel
                if striped is bike
                if nextto(train, pitbull)
                if nextto(badger, bike)
                if nigel is foot
                for (flatwhite, espresso, chai, decaf, mocha) in orderings
                if david is mocha
                if paisley is flatwhite
                if middle is espresso
                if plane is chai
                if nextto(train, decaf))

if __name__ == "__main__":
    results = election_puzzle()
    names = ('nicola', 'ed', 'nick', 'david', 'nigel')
    houses = ('tartan', 'gingham', 'paisley', 'polkadot', 'striped')
    pets = ('guineapig', 'badger', 'pitbull', 'squirrel', 'fish')
    travel = ('foot', 'plane', 'bike', 'car', 'train')
    drink = ('flatwhite', 'espresso', 'chai', 'decaf', 'mocha')
    attribute_results = [houses, pets, travel, drink]
    results_dict = {}
    name_results = results[0]
    for name_code in name_results:
        attributes = []
        for i, category in enumerate(attribute_results):
            attribute_index = results[i+1].index(name_code)
            attributes.append(category[attribute_index])
        name_index = name_results.index(name_code)
        name = names[name_index]
        results_dict[name] = attributes

    print results_dict
    for k,v in results_dict.items():
        if 'fish' in v:
            print '%s owns the fish' % k
