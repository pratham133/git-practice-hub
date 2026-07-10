def count_vowels(s):
    return sum(1 for c in s if c in 'aeiou')  # bug: misses uppercase vowels — Tier 2 fix-it issue
