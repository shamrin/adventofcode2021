inp = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

# inp = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

from itertools import permutations

inp = open('day8.txt').read()
lines = [[s.strip().split(' ') for s in line.split('|')] for line in inp.split('\n')]

# part 1
n = 0
for patterns, output in lines:
    for o in output:
        if len(o) == 2: #1
            n += 1
        if len(o) == 4: #4
            n += 1
        if len(o) == 3: #7
            n += 1
        if len(o) == 7: #8
            n += 1
print(n)

# part 2
digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}
def ordered(s): return ''.join(sorted(s))
lines = [([ordered(p) for p in patterns], [ordered(o) for o in output]) for patterns, output in lines]
results = []
for patterns, outputs in lines:
    for combination in permutations('abcdefg'):
        xy = dict(zip(combination, 'abcdefg'))
        if all(ordered(xy[p] for p in pattern) in digits for pattern in patterns):
            results.append(int(''.join(str(digits[ordered(xy[o] for o in output)]) for output in outputs)))

# part 1 second solution
print(sum(str(r).count(d) for r in results for d in '1478'))
# part 2 solution
print(sum(results))