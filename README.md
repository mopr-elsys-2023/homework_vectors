# Създаване на интерфейс за връзка с изкуствен интелект за работа с естествен език

Като новонает програмист, вие сте пред следното предизвикателство – да изградите интерфейс, който да интегрира изкуствения интелект в обработката и анализа на естествен език. Господин Георгиев, ваш ментор и един от водещите разработчици в тази област, ви е предоставил забележителен ресурс: обучен модел, който асоциира думи с техните векторни представяния. Тази структура от данни ви дава възможност да извършвате сложни семантични анализи и да разпознавате взаимоотношенията между различни понятия в езика.

Трябва да намерите решения на следните проблеми: 

## 0. Инструкции

Аргументът `model` навсякъде е `dictionary`:
1. ключ - дума от тип `str`
2. стойност - вектор от тип `list`

Множеството от всички стойности на `model` формира линейно пространство.
Приемете, че векторите на думите съотвестват на точки, а отношениеята между две думи - на свързан вектор. 
Също така, свойствата засегнати в урока за геометрични вектори са в сила.

## 1. Измерване на семантична близост

Напишете функция `calculate_similarity`, която оценява до колко две думи - `base_word` и `target_word` са семантично подобни една на друга. 
За метрика на подобие, считайте до колко векторите, съответсващи на думите в модела, имат еднакъв ъгъл ( ъгълът между подобни думи е малък ). 

Използвайки `calculate_similarity`, напишете функция `find_most_similar_to_given`, която намира най-подобната на `given_word` измежду `target_words`.

Използвайки `calculate_similarity`, напишете функции `doesnt_match`, която намира дума от `given_words`, която е най-малко подобна на всички останали.

```python
# Изход: число в интервал [-1; 1]
def calculate_similarity(model, base_word, target_word):
    pass

# Пример
# Вход: model, 'bridge', ['car', 'man', 'arch']
# Изход: 'arch'
def find_most_similar_to_given(model, given_word, target_words):
    pass

# Пример
# Вход: model, ['lunch', 'breakfast', 'dinner', 'homework']
# Изход: 'homework'
def doesnt_match(model, given_words):
    pass
```

## 2. Намиране на семантични отношения: 

Напишете функция, която намира как се отнасят две думи една спрямо друга в линейното пространство на модела и използва тази връзка, за да намери дума с подобно отношение спрямо трета дума.

```python
# Пример
# Вход: model, 'man', 'king', 'woman'
# Изход: 'queen'
#
# Пояснение: Връзката между 'man' и 'king' е същата като между 'woman' и 'queen'
def find_common_meaning(model, base_word, related_word, target_word):
    pass
```

