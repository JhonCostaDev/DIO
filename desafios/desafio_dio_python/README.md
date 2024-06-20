# Desafio: Criando um sistema bancário

## Objetivo Geral
### Separar as funções existentes em funções:
* saque
* deposito
* extrato 

### Criar duas novas funções: 
* Cadastrar Usuário(clinte)
* Cadastrar Conta Bancária.

## Desafio
Precisamos deixar nosso código mais modularizado, para isso vamos crar funções para as operações existentes:
* Sacar
* Depositar
* Visualizar Extrato.

Além disso, para a versão 2 do nosso sistema precimaos criar duas novas funções:
* Criar usuário(Cliente do banco)
* Criar conta corrente (Vincular com usuário) 

## Separação das funções
Devemos criar funções para toas as operações do sistema. Para exercitar tudo o que foi aprendido no módulo de funções. Cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

## Função Saque
Deve receber os argumentos apenas por nome **(keyword only)**. Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

## Função Deposito
Deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valo, extrato. Sugestão de retorno: saldo e extrato.

## Função Extrato
Deve receber os argumentos por posição e nome(positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Novas Funções
Precisamos criar duas novas funções: criar usuário e criar conta corrent. Pode-se criar uma terceira para listar as contas de usuários.

## Criar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: 
* Nome
* Data de nascimento
* CPF
* Endereço

O campo endereço deve ser uma string com o formato:
logradouro, numero - bairro - cidade / UF.

Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.

## Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por:
* Agência
* Número da conta
* Usuário
O número da agência é fixo: **0001**.
O usuário pode ter mais de um o conta, mas um conta pertence a somente um usuário.

## DICA
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.