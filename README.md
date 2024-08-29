# Hackathon Santo Digital

## Desafio 0

### Exercicio I

Utilizando a capacidade do **python** de multiplicar **strings**, fiz um **loop** que multiplica **n** por *, retornando o **array** com as strings de asterisco.

### Exercicio II

1. Verifico se o **array** tinha mais que dois elementos.

2. Verifico o parametro `allow_duplicates`, sendo verdadeiro, utilizo o `set` para garantir que não tenha elementos duplicados e  coloco esses elementos em um **array** utilizando o `list`.

3. Verifico o parametro `sorted_pairs`, sendo verdadeiro, ordeno o **array** utilizando a função `sort()` do **python**.

4. Busco a menor diferença entre os elementos.

5. Busco os elementos que atendiam a condição de menor diferença.

6. Verifico o parametro `unique_pairs`, sendo verdadeiro, removi a possibilidade de elementos duplicados.

### Exercicio III

1. Verifico o parametro `distinct_only`, sendo verdadeiro, utilizo o `set` para garantir que não tenha elementos duplicados e coloco esses elementos em um **array** utilizando o `list`.

2. Verifico o parametro `min_size` e `max_size`, sendo verdadeiro, limito o tamanho mínimo e máximo do subconjunto. Caso contrário utilizo os valores padrões `min_size = 0` e `max_size=None`

3. Utilizo a ferramenta `combinations` para gerar os subconjuntos limitando o tamanho.

4. Verifico o parametro `sort_subsets`, sendo verdadeiro, ordeno o **array** utilizando a função `sort()` do **python**, para garantir que os elementos sejam ordenados de forma crescente, utilizo a função `lambda` para comparar o tamanho do elemento, e os valores do elemento.