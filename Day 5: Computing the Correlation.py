from collections import Counter
import math

math_scores, phys_scores, chem_scores = Counter(), Counter(), Counter()
math_phys_pairs, chem_math_pairs, phys_chem_pairs = Counter(), Counter(), Counter()
N = int(input())

def calculate_coeff(s1_scores, s2_scores, s1_s2_pairs, n):
    s1_s2_sum = n * sum([k[0] * k[1] * v for k, v in s1_s2_pairs.items()])
    s1_sum = sum([int(k) * v for k, v in s1_scores.items()])
    s2_sum = sum([int(k) * v for k, v in s2_scores.items()])

    numer = s1_s2_sum - s1_sum * s2_sum
    
    s1_denom = math.sqrt(n * sum([int(k)**2 * v for k, v in s1_scores.items()]) - s1_sum**2)
    s2_denom = math.sqrt(n * sum([int(k)**2 * v for k, v in s2_scores.items()]) - s2_sum**2)
    denom = s1_denom * s2_denom
    
    return float(numer) / float(denom)

for i in range(N):
    scores = list(map(int, input().split()))

    math_scores[str(scores[0])] += 1
    phys_scores[str(scores[1])] += 1
    chem_scores[str(scores[2])] += 1
    
    math_phys_pairs[(scores[0], scores[1])] += 1
    chem_math_pairs[(scores[2], scores[0])] += 1
    phys_chem_pairs[(scores[1], scores[2])] += 1

r_math_phys, r_chem_math, r_phys_chem = 0, 0, 0

r_math_phys = calculate_coeff(math_scores, phys_scores, math_phys_pairs, N)
r_phys_chem = calculate_coeff(phys_scores, chem_scores, phys_chem_pairs, N)
r_chem_math = calculate_coeff(chem_scores, math_scores, chem_math_pairs, N)

ans = [r_math_phys, r_phys_chem, r_chem_math]

for r in ans:
    print(round(r, 2))
    
