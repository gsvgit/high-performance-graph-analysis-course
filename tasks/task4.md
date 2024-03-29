# Задача 4. Реализация поиска кратчайших путей

* **Мягкий дедлайн**: 02.04.2023, 23:59
* **Жёсткий дедлайн**: 05.04.2023, 23:59
* Полный балл: 15

## Задача

Везде считаем, что вершины графа занумерованы подряд с нуля.
Обратите внимание на то, что про граф заранее не известно, есть ли в нём циклы отрицательного веса.

- [ ] Используя pygraphblas реализовать функцию поиска кратчайших путей в ориентированном графе из заданной вершины (Bellman–Ford).
  - [ ] Функция принимает представление графа, удобное для неё (загрузка, конвертация реализованы отдельно) и номер стартовой вершины.
  - [ ] Функция возвращает массив, где для каждой вершины указано расстояние до неё от указанной стартовой вершины. Если вершина не достижима, то значение соответствующей ячейки равно float('inf').
- [ ] Используя pygraphblas реализовать функцию поиска кратчайших путей в ориентированном графе из нескольких заданных вершин.
  - [ ] Функция принимает представление графа, удобное для неё (загрузка, конвертация реализованы отдельно) и массив номеров стартовых вершин.
  - [ ] Функция возвращает массив пар: вершина, и массив, где для каждой вершины указано расстояние до неё из указанной. Если вершина не достижима, то значение соответствующей ячейки равно float('inf').
- [ ] Используя pygraphblas реализовать функцию поиска кратчайших путей в ориентированном графе для всех пар вершин (Floyd–Warshall).
  - [ ] Функция принимает представление графа, удобное для неё (загрузка, конвертация реализованы отдельно).
  - [ ] Функция возвращает массив пар: вершина, и массив, где для каждой вершины указано расстояние до неё из указанной. Если вершина не достижима, то значение соответствующей ячейки равно float('inf').
- [ ] Добавить необходимые тесты.
