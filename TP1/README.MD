# TP1 - Expressão regular para apanhar Strings Binárias que não contenham a substring "011"

## Autor
- **Nome:** José Miguel Gomes Braga
- **ID:** A109066
- **Foto:**
![A minha foto de perfil](foto.jpg)

## Resumo
O objetivo deste trabalho prático foi desenvolver uma Expressão Regular capaz de identificar e aceitar strings binárias que não contenham a substring "011".

Para resolver este problema, a expressão concebida foi `^1*(0+1)*0*$`. 
A lógica aplicada consiste em permitir qualquer quantidade inicial de uns (`1*`). Em seguida, garante-se que qualquer zero seja seguido de, no máximo, um único um (`(0+1)*`), o que invalida a possibilidade da sequência proibida "011". Por fim, a string pode terminar com qualquer número de zeros (`0*`).

## Resultados
- [Ficheiro da Resolução](resolucao.txt)