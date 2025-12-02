import os
import sys
import time


while True:
    def p(text, delay = 0.05):
        for char in text:
            print(char, end='', flush = True)
            time.sleep(delay)
        print()

    def clear():
        if os.name == 'nt':  
            os.system('cls')
        else:  
            os.system('clear')

    def obtain():

        print("====================================")
        print("  ANÁLISE ESTATÍSTICA DE TEXTO   ")
        print("====================================")
        
        p("\n Por favor, insira o bloco de texto para análise:\n\n>>> ")
        try:
            texto = sys.stdin.readline()
        except:
            sys.exit() 

        texto_limpo = texto.lower()

        caracteres_indesejados = [',', '.', '!', '?', ';', ':', '(', ')', '"', "'", '\n']
        for char in caracteres_indesejados:
            texto_limpo = texto_limpo.replace(char, ' ')
            
        return texto_limpo

    def analitic(texto_limpo):
        estatisticas = {}

        palavras = [p for p in texto_limpo.split() if p]

        estatisticas['total_palavras'] = len(palavras)
        
        palavra_mais_longa = ""
        if palavras:
            for palavra in palavras:
                if len(palavra) > len(palavra_mais_longa):
                    palavra_mais_longa = palavra
        estatisticas['palavra_mais_longa'] = palavra_mais_longa


        todos_caracteres_sem_espaco = ''.join(palavras)
        estatisticas['total_caracteres'] = len(todos_caracteres_sem_espaco)

    
        frequencia_letras = {}
        for letra in todos_caracteres_sem_espaco:
            if 'a' <= letra <= 'z':
                frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
                
        estatisticas['frequencia_letras'] = frequencia_letras
        
        return estatisticas

    def results(estatisticas):

        p('Aqui vai sua analise completa! ')
        print()

        print("\n" + "="*40)
        print(" ANÁLISE COMPLETA")
        print("="*40)
        
        print(f"| Total de Palavras:   {estatisticas['total_palavras']}")
        print(f"| Total de Caracteres: {estatisticas['total_caracteres']}")
        print(f"| Palavra Mais Longa:  '{estatisticas['palavra_mais_longa']}'")
        print("-" * 40)
        
        print("| Frequência de Letras:")
        
        letras_ordenadas = sorted(estatisticas['frequencia_letras'].items())
        
        total_letras = estatisticas['total_caracteres']
        
        colunas = []
        for letra, contagem in letras_ordenadas:
            percentual = (contagem / total_letras) * 100 if total_letras > 0 else 0
            colunas.append(f"'{letra}': {contagem} ({percentual:.2f}%)")
        
        for i in range(0, len(colunas), 2):
            coluna1 = colunas[i]
            coluna2 = colunas[i+1] if i + 1 < len(colunas) else ""
            print(f"|   {coluna1:<20} {coluna2}")
            
        print("="*40)


    def main():
        clear()
        texto = obtain()
        
        if texto.strip():
            resultados = analitic(texto)
            
            clear()
            results(resultados)
        else:
            p("\n Nenhum texto foi inserido. Encerrando a análise.")
            print("====================================")
            print()

    clear()

    if __name__ == "__main__":
        main()

    
    p('Deseja continuar? (y/n) ')
    try:
        alternative = str(sys.stdin.readline().strip())
    except:
        sys.exit()
    if alternative == 'y':
        continue
    else:
        break