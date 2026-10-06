import re

def converter_markdown_para_html(texto):
    # Converter Imagens primeiro para que os links nao interfiram
    texto = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', texto)
    
    # Converter Links
    texto = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', texto)
    
    # Converter Bold
    texto = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', texto)
    
    # Converter Italico
    texto = re.sub(r'(?<!\*)\*(?!\*)(.*?)\*', r'<i>\1</i>', texto)
    
    # Converter Cabecalhos (do maior para o menor nivel)
    texto = re.sub(r'^###\s+(.*)', r'<h3>\1</h3>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^##\s+(.*)', r'<h2>\1</h2>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^#\s+(.*)', r'<h1>\1</h1>', texto, flags=re.MULTILINE)
    
    # Converter itens da Lista Numerada
    texto = re.sub(r'^\d+\.\s+(.*)', r'<li>\1</li>', texto, flags=re.MULTILINE)
    
    # Juntar os <li> consecutivos dentro de blocos <ol>
    texto = re.sub(r'(<li>.*</li>(?:\n<li>.*</li>)*)', r'<ol>\n\g<1>\n</ol>', texto)
    
    return texto

# Teste de exemplo igual ao da aula
if __name__ == '__main__':
    texto_teste = """
# Exemplo
Este é um **exemplo** ...
Este é um *exemplo* ...
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
    """
    
    html_gerado = converter_markdown_para_html(texto_teste)
    print(html_gerado)