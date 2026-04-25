import os 
import random

"""
Sistema StudyCam - Gerenciamento de Notas

Funcionalidades:
- Capturar notas com validação OCR
- Listar notas por matéria
- Pesquisar por tags e conteúdo
"""
# Lista global de notas
notas = [
    {'nome': 'Teorema de Pitágoras', 'materia': 'Matemática', 'confianca_ocr': 92, 'revisado': False, 'tags': ['#Geometria', '#Prova'], 'conteudo': 'Em um triângulo retângulo, o quadrado da hipotenusa é igual à soma dos quadrados dos catetos.'}, 
    {'nome': 'Revolução Francesa', 'materia': 'História', 'confianca_ocr': 87, 'revisado': True, 'tags': ['#Resumo', '#Revolução'], 'conteudo': 'A Revolução Francesa foi um período de transformação social e política na França, iniciado em 1789.'},
    {'nome': 'Fotossíntese', 'materia': 'Biologia', 'confianca_ocr': 79, 'revisado': False, 'tags': ['#Processos', '#Celular'], 'conteudo': 'Processo biológico onde plantas convertem luz em energia química, utilizando água e dióxido de carbono.'}
]


def exibir_nome_do_programa():
    """
    Exibe o nome do sistema no terminal.
    """
    print("=" * 72)
    print("""
░██████╗████████╗██╗░░░██╗██████╗░██╗░░░██╗░█████╗░░█████╗░███╗░░░███╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗████╗░████║
╚█████╗░░░░██║░░░██║░░░██║██║░░██║░╚████╔╝░██║░░╚═╝███████║██╔████╔██║
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║░░╚██╔╝░░██║░░██╗██╔══██║██║╚██╔╝██║
██████╔╝░░░██║░░░╚██████╔╝██████╔╝░░░██║░░░╚█████╔╝██║░░██║██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝""")
    print("=" * 72)

def exibir_opcoes():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    print('1. Capturar Nota')
    print('2. Listar por Matéria')
    print('3. Pesquisar')
    print('4. Sair\n')


def finalizar_app(): 
    """
    Finaliza o sistema exibindo uma mensagem de encerramento.
    """
    exibir_subtitulo('Encerrando Sistema')
    print('Obrigado por usar StudyCam!')
    print('Suas notas foram salvas.\n')


def voltar_ao_menu_principal():
    """
    Aguarda interação do usuário e retorna ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """
    Exibe mensagem de erro quando o usuário escolhe uma opção inválida.
    """
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu')
    main()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado e limpa a tela.

    Funcionamento:
    - Executa comando do sistema para limpar tela
    - Exibe o texto como um subtítulo
    """
    limpar_terminal()
    print("=" * 40)
    print(texto)
    print("=" * 40)
    print()


def classificar_materia(conteudo):
    """
    Classifica a matéria baseado em palavras-chave do conteúdo.

    Funcionamento:
    - Procura por palavras-chave em cada disciplina
    - Retorna a matéria encontrada ou 'Geral'
    """
    conteudo_lower = conteudo.lower()
    
    # Palavras-chave por matéria
    if 'número' in conteudo_lower or 'equação' in conteudo_lower or 'teorema' in conteudo_lower or 'cálculo' in conteudo_lower:
        return 'Matemática'
    
    if 'ano' in conteudo_lower or 'século' in conteudo_lower or 'revolução' in conteudo_lower or 'guerra' in conteudo_lower:
        return 'História'
    
    if 'célula' in conteudo_lower or 'organismo' in conteudo_lower or 'gene' in conteudo_lower or 'fotossíntese' in conteudo_lower:
        return 'Biologia'
    
    if 'força' in conteudo_lower or 'energia' in conteudo_lower or 'velocidade' in conteudo_lower or 'movimento' in conteudo_lower:
        return 'Física'
    
    return 'Geral'


def validar_entrada_texto(mensagem_prompt, campo_nome='texto'):
    """
    Valida entrada de texto do usuário com repetição até obter dado válido.

    Funcionamento:
    - Usa while True para repetir até obter entrada válida
    - Verifica se a entrada não está vazia
    - Exibe mensagem de erro se inválida
    """
    while True:
        entrada = input(mensagem_prompt)
        
        if entrada == '':
            print(f'Erro: O {campo_nome} não pode estar vazio!\n')
            continue
        
        return entrada


def capturar_nova_nota():
    """
    Captura uma nova nota com validação de confiança OCR.

    Funcionamento:
    - Recebe título e conteúdo da nota
    - Gera confiança OCR (50-100%)
    - Se < 50%, rejeita e pede nova captura
    - Classifica a matéria automaticamente
    - Atribui tags baseado na matéria
    - Adiciona à lista de notas
    """
 
    exibir_subtitulo('Captura de Nova Nota')
    
    # Entrada do título
    titulo_nota = validar_entrada_texto('Digite o título da nota: ', 'título')
    
    # Entrada do conteúdo
    print('Digite o conteúdo da nota:')
    conteudo_nota = validar_entrada_texto('> ', 'conteúdo')
    
    # Gera confiança OCR
    confianca_ocr = random.randint(50, 100)
    
    print(f'\nProcessando OCR...')
    print(f'Confiança: {confianca_ocr}%')
    
    # Valida confiança
    if confianca_ocr < 50:
        print('Confiança muito baixa! Tente capturar novamente.')
        input('\nDigite uma tecla para voltar ao menu')
        main()
        return
    
    # Classifica matéria
    materia_detectada = classificar_materia(conteudo_nota)
    print(f'Matéria detectada: {materia_detectada}')
    
    # Define tags por matéria
    tags_por_materia = {
        'Matemática': ['#Cálculo', '#Fórmula'],
        'História': ['#Contexto', '#Período'],
        'Biologia': ['#Processos', '#Celular'],
        'Física': ['#Movimento', '#Energia'],
        'Geral': ['#Nota', '#Revisão']
    }
    
    tags_nota = tags_por_materia.get(materia_detectada, ['#Nota'])
    
    # Cria dicionário com dados da nota
    dados_da_nota = {
        'nome': titulo_nota,
        'materia': materia_detectada,
        'confianca_ocr': confianca_ocr,
        'revisado': False,
        'tags': tags_nota,
        'conteudo': conteudo_nota
    }

    # Adiciona à lista
    notas.append(dados_da_nota)

    print(f'\nNota "{titulo_nota}" capturada com sucesso!')
    print(f'Confiança: {confianca_ocr}% | Matéria: {materia_detectada}')
    
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def listar_notas_por_materia():
    """
    Lista todas as notas de uma matéria específica.

    Funcionamento:
    - Coleta matérias disponíveis
    - Valida escolha do usuário
    - Filtra notas da matéria selecionada
    - Exibe informações das notas
    """
    exibir_subtitulo('Listar Notas por Matéria')
    
    # Coleta matérias disponíveis
    materias_disponiveis = []
    for nota in notas:
        if nota['materia'] not in materias_disponiveis:
            materias_disponiveis.append(nota['materia'])
    
    if not materias_disponiveis:
        print('Nenhuma matéria cadastrada ainda.\n')
        voltar_ao_menu_principal()
        return
    
    # Exibe matérias
    print('Matérias disponíveis:')
    for indice, materia in enumerate(materias_disponiveis, 1):
        print(f'{indice}. {materia}')
    
    print()
    
    # Valida escolha
    escolha_valida = False
    while not escolha_valida:
        try:
            escolha = int(input('Escolha uma matéria pelo número: '))
            
            if 1 <= escolha <= len(materias_disponiveis):
                materia_selecionada = materias_disponiveis[escolha - 1]
                escolha_valida = True
            else:
                print(f'Digite um número entre 1 e {len(materias_disponiveis)}.\n')
        except ValueError:
            print('Digite um número válido.\n')
    
    # Filtra notas da matéria
    notas_da_materia = []
    for nota in notas:
        if nota['materia'] == materia_selecionada:
            notas_da_materia.append(nota)
    
    if not notas_da_materia:
        print(f'Nenhuma nota encontrada para {materia_selecionada}\n')
        voltar_ao_menu_principal()
        return
    
    # Exibe notas
    print(f'\nNotas de {materia_selecionada}:\n')
    
    for nota in notas_da_materia:
        titulo = nota['nome']
        ocr = nota['confianca_ocr']
        revisado = 'Sim' if nota['revisado'] else 'Não'
        tags = nota['tags']
        
        print(f'Título: {titulo}')
        print(f'Confiança OCR: {ocr}%')
        print(f'Revisado: {revisado}')
        print(f'Tags: {tags}')
        print('-' * 50)

    voltar_ao_menu_principal()


def pesquisar_por_tags_conteudo():
    """
    Pesquisa notas por tags ou por conteúdo específico.

    Funcionamento:
    - Recebe termo de busca do usuário
    - Procura no conteúdo e nas tags
    - Exibe notas que correspondem
    """
    exibir_subtitulo('Pesquisar por Tags/Conteúdo')
    
    # Entrada do termo de busca
    termo_busca = validar_entrada_texto(
        'Digite o termo ou hashtag para buscar (ex: #Prova ou teorema): ',
        'termo'
    ).lower()
    
    # Filtra notas
    notas_encontradas = []
    
    for nota in notas:
        conteudo_lower = nota['conteudo'].lower()
        
        # Verifica se está no conteúdo
        if termo_busca in conteudo_lower:
            notas_encontradas.append(nota)
        else:
            # Verifica se está nas tags
            for tag in nota['tags']:
                if termo_busca in tag.lower():
                    notas_encontradas.append(nota)
                    break
    
    # Se não encontrou nada
    if not notas_encontradas:
        print(f'\nNenhuma nota encontrada com: "{termo_busca}"\n')
        voltar_ao_menu_principal()
        return
    
    # Exibe resultados
    print(f'\n{len(notas_encontradas)} nota(s) encontrada(s):\n')
    
    for nota in notas_encontradas:
        titulo = nota['nome']
        materia = nota['materia']
        conteudo = nota['conteudo']
        tags = nota['tags']
        
        print(f'Título: {titulo}')
        print(f'Matéria: {materia}')
        print(f'Conteúdo: {conteudo}')
        print(f'Tags: {tags}')
        print('-' * 50)

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Captura a opção do usuário e direciona para a função correspondente.

    Estrutura de decisão:
    - Utiliza match-case para roteamento de opções
    - Trata entrada não-numérica com try/except
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # Roteamento com match-case
        match opcao_escolhida:
            case 1:
                capturar_nova_nota()
            case 2:
                listar_notas_por_materia()
            case 3:
                pesquisar_por_tags_conteudo()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    
    except ValueError:
        print('Digite um número válido.\n')
        input('Digite uma tecla para voltar ao menu')
        main()

def limpar_terminal():
    """
    Função que limpa o terminal.
    Utiliza o "cls" se for Windows e "Clear" se for Mac/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Função principal que inicia o programa.

    Responsável por:
    - Limpar a tela
    - Exibir o menu
    - Capturar a opção do usuário
    """
    limpar_terminal()
    exibir_nome_do_programa()
    print()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
