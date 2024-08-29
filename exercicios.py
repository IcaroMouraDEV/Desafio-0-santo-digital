def exercicio_1(n: int):
  return [i * '*' for i in range(1, n + 1)];


def exercicio_2(arr: list,  allow_duplicates=True, sorted_pairs=True,  unique_pairs=False):
  if len(arr) < 2:
    return []; # tem que ter no minimo 2 elementos

  if not allow_duplicates:
    arr = [*set(arr)]; # eliminando duplicatas
  
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


def exercicio_3(conj: list):
  subs = [[]];

  for item in conj:
    novo_subs = [];

    for sub in subs:
      novo_subs.append(sub + [item])
    
    subs.extend(novo_subs)

  return subs;


print(exercicio_3([5, 3, 5, 9, 7, 11]));
