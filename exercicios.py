from itertools import combinations


def exercicio_1(n: int):
  return [i * '*' for i in range(1, n + 1)];


def exercicio_2(arr: list,  allow_duplicates=True, sorted_pairs=True,  unique_pairs=False):
  if len(arr) < 2:
    return [];

  if not allow_duplicates:
    arr = list(set(arr));
  
  if sorted_pairs:
    arr.sort();

  menor_dif = float('inf');
  new_arr = [*arr];
  new_arr.sort();

  for i in range(len(new_arr) - 1):
    dif = abs(new_arr[i + 1] - new_arr[i]);
    if dif < menor_dif:
      menor_dif = dif;

  pairs = [];
  for i in range(len(arr) - 1):
    for j in range(i+1, (len(arr))):
      if abs(arr[j] - arr[i]) == menor_dif:
        pair = (arr[i], arr[j]);
        if unique_pairs:
          pair = tuple(sorted(pair));
          if pair not in pairs:
            pairs.append(pair);
        else:
          pairs.append(pair);

  return pairs;


def exercicio_3(sets: list, max_size=None, min_size=0, distinct_only=False, sort_subsets=False):
  subs = [];

  if distinct_only:
    sets = list(set(sets));

  for size in range(min_size, (max_size or len(sets)) + 1):
    new_subs = [];
    for sub in combinations(sets, size):
      new_subs.append(list(sub))
    
    subs.extend(new_subs)
  
  if sort_subsets:
    subs = [sorted(sub) for sub in subs];
    subs.sort(key=lambda x: (len(x), x))

  return subs;
