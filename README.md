# Engine de Recomendação

## Instalação
Essa engine de recomendação utiliza implementações presentes no projeto [python-recsys](https://github.com/ocelma/python-recsys). Instruções de instalação também estão presentes no link.

## Dataset
O dataset utilizado nesse projeto representa dados de avaliação de usuários sobre filmes que contém informações como: título, gêneros e data de avaliação.

O dataset pode ser baixado diretamente pelo [repositório da MovieLens](https://grouplens.org/datasets/movielens/1m/).

Após o download basta setar o caminho do arquivo `ratings.dat` na variável `RATINGS`.

## Funções
Todas as implementações fornecem algoritmos baseados na fatorização de matriz.

O python-recsys faz uso do [SVD (Singular Value Decomposition)](https://en.wikipedia.org/wiki/Singular_value_decomposition) para a a fatorização de matriz.

### Similaridade
Existem duas funções de similaridade. A primeira (entre itens) calcula um valor de similaridade entre dois itens.

Já a segunda (a partir de um item) encontra itens potencialmente similares ao informado.

Os valores da similaridade variam entre 0 e 1 (quanto maior, mais similar).
#### Entre itens
```python
svd = load_data()
engine = Engine(svd)
TOY_STORY = 1 # Toy Story
A_BUGS_LIFE = 2355 # A bug's life
print engine.get_similarity(TOY_STORY, A_BUGS_LIFE)
# 0.677069366773
```

#### A partir de um item
```python
TOY_STORY = 1 # Toy Story
print engine.get_similar(TOY_STORY)
# [(1, 0.99999999999999978), (3114, 0.87060391051017305), (2355, 0.67706936677314977), (588, 0.58073514967544992), (595, 0.46031829709744226), (1907, 0.44589398718134982), (364, 0.42908159895577563), (2081, 0.42566581277822413), (3396, 0.42474056361934953), (2761, 0.40439361857576017)]
```
Ou seja, o item 3114 (Toy Story 2) é o mais similar ao item 1 (Toy Story).

### Predição
Essa função tenta adivinhar uma avaliação que o usuário daria a um filme baseada nos dados referentes à avaliação de um determinado usuário:
```python
print engine.predict_rating(1, 10) # qual nota o usuário 1 daria ao filme 10?
# 4.11823417929
```
As notas variam de 0 a 5.

### Recomendação
Existem duas funções de recomendação. Uma recomenda filmes a partir de um usuário e a outra faz o caminho inverso, recomendando usuários que possam gostar de um filme.

#### A partir de um usuário
```python
print engine.recommend_from_user(89) # recomende filmes para o usuário 89
# [(1193, 4.3079570356055426), (318, 4.2822619682381857), (2905, 4.2797600479045848), (1198, 4.2563654970507399), (50, 4.2207264111002827), (2019, 4.211843330561412), (904, 4.1990555544080577), (527, 4.1938272001459929), (745, 4.1772025691190917), (1212, 4.1610853531292582)]
```
Ou seja, o usuário 89 é propício a gostar do filme 1193 (One Flew Over the Cuckoo's Nest).

#### A partir de um filme
```python
KARATE_KID = 2420
print engine.recommend_from_item(KARATE_KID) # quais usuários podem gostar do filme 2420 (The Karate Kid)
# [(4801, 4.8926771286079349), (2339, 4.8625503664375973), (3902, 4.8622025911549054), (283, 4.8016103413311599), (3032, 4.785088757413309), (3324, 4.7343748811568105), (5862, 4.7320035863040424), (4634, 4.7033854873168846), (412, 4.6940386350020233), (446, 4.6939587815173871)]
```
