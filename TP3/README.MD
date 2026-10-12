# TP3 - Analisador Léxico

## Autor
- **Nome:** José Miguel Gomes Braga
- **ID:** A109066
- **Foto:**
![A minha foto de perfil](foto.jpg)

## Resumo
O objetivo deste trabalho prático foi desenvolver um analisador léxico para uma linguagem de query específica.

Para resolver este problema, utilizei a biblioteca `re` do Python. Defini uma lista de tuplos, onde cada tuplo contém o nome do token e a expressão regular correspondente. Em seguida, utilizei a funcionalidade de grupos nomeados (`(?P<nome>...)`) combinada com a junção de todas as regras num `OR` lógico (`|`) para criar uma única expressão regular abrangente. O iterador `re.finditer` percorre o código fonte gerando tokens, ignorando automaticamente espaços em branco e comentários iniciados por `#`, de acordo com os requisitos estabelecidos.

## Resultados
- [Código do Analisador Léxico](analisador.py)