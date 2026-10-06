# TP2 - Conversor de MarkDown para HTML

## Autor
- **Nome:** José Miguel Gomes Braga
- **ID:** A109066
- **Foto:**
![A minha foto de perfil](foto.jpg)

## Resumo
O objetivo deste trabalho prático foi criar um conversor em Python que traduza elementos com sintaxe básica de MarkDown para código HTML equivalente.

Para a resolução, utilizei o módulo `re` do Python. Defini uma função que aplica substituições sucessivas (`re.sub`) ao texto de entrada. Tratei especificamente as imagens e os links primeiro, seguidos dos estilos de texto (bold e itálico). Para os cabeçalhos (`h1`, `h2`, `h3`) e itens de listas (`li`), ativei a flag `re.MULTILINE` para garantir que o padrão atua corretamente no início de cada linha. Finalmente, agrupei itens de lista consecutivos num bloco `<ol>`.

## Resultados
- [Código do Conversor (Python)](conversor.py)