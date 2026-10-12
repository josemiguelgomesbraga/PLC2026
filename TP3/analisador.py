import re

def analisador_lexico(codigo):
    # Definir regras para cada token
    regras = [
        ('COMENTARIO', r'#.*'),
        ('VARIAVEL', r'\?[a-zA-Z0-9_]+'),
        ('LINGUA', r'@[a-zA-Z]{2}'),
        ('STRING', r'"[^"]*"'),
        ('RESERVADA', r'\bLIMIT\b'),
        ('NUMERO', r'\b\d+\b'),
        ('CONCEITO', r'[a-zA-Z0-9_:]+'), 
        ('DELIMITADOR', r'[{}.]'),
        ('ESPACO', r'\s+'),
        ('ERRO', r'.')
    ]
    
    # Juntar todas com (|)
    regex_completa = '|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in regras)
    
    tokens = []
    for correspondencia in re.finditer(regex_completa, codigo):
        tipo = correspondencia.lastgroup
        valor = correspondencia.group()
        
        # Ignoramos espacos e comentarios consoante as regras
        if tipo == 'ESPACO' or tipo == 'COMENTARIO':
            continue 
        elif tipo == 'ERRO':
            print(f"Erro lexico: Carater inesperado '{valor}'")
        else:
            tokens.append((tipo, valor))
            
    return tokens

# Teste de exemplo igual ao da aula
if __name__ == '__main__':
    codigo_teste = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000"""

    for token in analisador_lexico(codigo_teste):
        print(token)