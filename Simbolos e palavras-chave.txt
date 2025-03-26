### 1.1 Operadores Aritméticos
- `+` : Adição
- `-` : Subtração
- `*` : Multiplicação
- `/` : Divisão (retorna um número float)
- `//` : Divisão inteira (resultado inteiro)
- `%` : Módulo (resto da divisão)
- `**` : Exponenciação (potência)

### 1.2 Operadores Relacionais
- `==` : Igual a
- `!=` : Diferente de
- `>` : Maior que
- `<` : Menor que
- `>=` : Maior ou igual a
- `<=` : Menor ou igual a

### 1.3 Operadores Booleanos
- `and` : E lógico
- `or` : Ou lógico
- `not` : Negação lógica

### 1.4 Símbolos de Atribuição
- `=` : Atribuição simples
- `+=` : Atribuição com adição
- `-=` : Atribuição com subtração
- `*=` : Atribuição com multiplicação
- `/=` : Atribuição com divisão
- `//=` : Atribuição com divisão inteira
- `%=` : Atribuição com módulo
- `**=` : Atribuição com exponenciação

### 1.5 Símbolos Identificadores de Tipos de Dados
- `int` : Tipo de dados para inteiros
- `float` : Tipo de dados para números de ponto flutuante
- `str` : Tipo de dados para strings (sequências de caracteres)
- `bool` : Tipo de dados para valores booleanos (`True` ou `False`)
- `list` : Tipo de dados para listas (coleções mutáveis e ordenadas)
- `tuple` : Tipo de dados para tuplas (coleções imutáveis e ordenadas)
- `dict` : Tipo de dados para dicionários (coleções de pares chave-valor)
- `set` : Tipo de dados para conjuntos (coleções não ordenadas e sem elementos duplicados)

### 1.6 Símbolo Identificador de Início de Bloco
No Python, o início de um bloco de código é determinado pela **indentação** (não há símbolos explícitos como `{` ou `}`). As palavras-chave que indicam o início de blocos de código são:
- **`def`**: Define uma função (inicia um bloco de código de função)
- **`class`**: Define uma classe (inicia um bloco de código de classe)
- **`if`**, **`elif`**, **`else`**: Controle de fluxo condicional (inicia um bloco de código condicional)
- **`for`**, **`while`**: Laços de repetição (iniciam blocos de código de loops)
- **`try`**, **`except`**, **`finally`**: Blocos de tratamento de exceções
- **`with`**: Bloco de contexto gerenciado


### 2.1 Identificadora de Blocos
No Python, a indentação define onde um bloco de código começa e termina. Não há uma palavra-chave específica para o início de um bloco, mas as seguintes palavras-chave controlam a execução e o agrupamento do código:
- **`def`**: Define uma função
- **`class`**: Define uma classe
- **`if`**, **`elif`**, **`else`**: Condicionais
- **`for`**, **`while`**: Laços de repetição
- **`try`**, **`except`**, **`finally`**: Tratamento de exceções
- **`with`**: Contextos gerenciados

### 2.2 Tipos de Dados
- **`int`**: Tipo de dados para números inteiros
- **`float`**: Tipo de dados para números de ponto flutuante
- **`str`**: Tipo de dados para strings (sequências de caracteres)
- **`bool`**: Tipo de dados para valores booleanos (`True` ou `False`)
- **`list`**: Tipo de dados para listas
- **`tuple`**: Tipo de dados para tuplas
- **`dict`**: Tipo de dados para dicionários
- **`set`**: Tipo de dados para conjuntos

### 2.3 Funções Built-in
O Python possui diversas funções built-in que estão disponíveis automaticamente:
- **`print()`**: Exibe uma saída no console
- **`len()`**: Retorna o comprimento de um objeto
- **`type()`**: Retorna o tipo de um objeto
- **`int()`**: Converte um valor para inteiro
- **`str()`**: Converte um valor para string
- **`list()`**: Converte um valor para lista
- **`input()`**: Recebe uma entrada do usuário
- **`range()`**: Gera uma sequência de números
- **`sum()`**: Soma os valores de um iterável
- **`min()`**, **`max()`**: Retorna o valor mínimo ou máximo de um iterável
- **`abs()`**: Retorna o valor absoluto de um número

### 2.4 Operadores Booleanos
Os operadores booleanos são usados para realizar operações lógicas:
- **`and`**: Realiza uma operação lógica "E"
- **`or`**: Realiza uma operação lógica "OU"
- **`not`**: Realiza uma operação lógica "NÃO" (negação)

### 2.5 Demais Palavras-chave
- **`import`**: Importa um módulo ou pacote
- **`from`**: Importa uma parte específica de um módulo
- **`in`**: Testa a presença de um valor em uma sequência ou itera sobre uma sequência
- **`as`**: Cria um alias para um módulo ou objeto
- **`global`**: Declara uma variável como global
- **`nonlocal`**: Acessa variáveis não locais em funções aninhadas
- **`assert`**: Verifica uma condição, utilizada para depuração
- **`lambda`**: Define uma função anônima
- **`yield`**: Retorna um valor de uma função geradora
- **`pass`**: Instrução que não faz nada (usada como um marcador de posição)
- **`del`**: Exclui um objeto ou variável
- **`try`**, **`except`**, **`finally`**: Blocos de tratamento de exceções
- **`with`**: Usado para gerenciar contextos, como arquivos ou outros recursos

"""

# Salvar o conteúdo no arquivo Markdown
with open("documentacao_python.md", "w") as file:
    file.write(documentacao)

print("O arquivo 'documentacao_python.md' foi gerado com sucesso!")
