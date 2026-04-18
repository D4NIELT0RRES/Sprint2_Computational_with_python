# 📚 StudyCam - Sistema de Gerenciamento de Notas

Um programa simples para capturar, organizar e pesquisar notas.

---

## 🎯 O que faz?

- Capturar notas com validação de qualidade
- Organizar por matérias (Matemática, História, Biologia, Física)
- Pesquisar por tags ou conteúdo

---

## 🚀 Como usar?

1. Execute: `python3 app.py`
2. Escolha uma opção (1, 2, 3 ou 4)
3. Siga as instruções na tela

---

## 📋 Menu

```
1. Capturar Nota
2. Listar por Matéria
3. Pesquisar
4. Sair
```

---

## 💡 Exemplos de Código

### 1. Armazenar Notas
As notas são guardadas em uma lista com dicionários:

```python
notas = [
    {
        'nome': 'Teorema de Pitágoras',
        'materia': 'Matemática',
        'confianca_ocr': 92,
        'revisado': False,
        'tags': ['#Geometria', '#Prova'],
        'conteudo': 'Em um triângulo retângulo...'
    }
]
```

### 2. Validar Entrada do Usuário
A função valida se o usuário digita algo vazio:

```python
def validar_entrada_texto(mensagem_prompt):
    while True:
        entrada = input(mensagem_prompt)
        if entrada == '':
            print('Erro: Não pode estar vazio!')
            continue
        return entrada
```

### 3. Classificar Matéria Automaticamente
O programa identifica a matéria pelas palavras no texto:

```python
def classificar_materia(conteudo):
    conteudo_lower = conteudo.lower()
    
    if 'equação' in conteudo_lower or 'teorema' in conteudo_lower:
        return 'Matemática'
    if 'revolução' in conteudo_lower or 'guerra' in conteudo_lower:
        return 'História'
    
    return 'Geral'
```

### 4. Pesquisar por Termo
A busca procura no conteúdo e nas tags:

```python
for nota in notas:
    conteudo_lower = nota['conteudo'].lower()
    
    if termo_busca in conteudo_lower:
        notas_encontradas.append(nota)
```

### 5. Menu com Match-Case
Escolha qual opção executar:

```python
match opcao_escolhida:
    case 1:
        capturar_nova_nota()
    case 2:
        listar_notas_por_materia()
    case 3:
        pesquisar_por_tags_conteudo()
    case 4:
        finalizar_app()
```

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Terminal (Mac, Linux ou Windows)

---

**Projeto educacional em Python** 🎓
