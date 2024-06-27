# VISIBILIDADE DE RECURSOS
Seguindo algumas convenções, as nossas classes são classificadas como:

Classe de modelo(model): Classes que representem estrutura de domínio da aplicação, exemplo: Cliente, Pedido, Nota Fiscal e etc.

Classe de serviço(service): Classes que contém regras de negócio e validação de nosso sistema.

Classe de repositório(repository): Classes que contém uma integração com banco de dados.

Classe de controle(controller): Classes que possuem a finalidade de disponibilizar alguma comunicação externa à nossa aplicação, tipo http web ou webservices.

Classe Utilitária(util): Classe que contém recursos comuns à toda nossa aplicação.

## PACOTES
A linguagem Java é composta por milhares de classes com as finalidades de por exemplo:

* Classes de tipos de dados,
* Representação de texto,
* Números,
* Datas,
* Arquivos e diretórios,
* Conexão a banco de dados

Imagina todas essas classes existirem em um único nível de documento? E as outras desenvolvidas por nós, meros, desenvolvedores de aplicações de vários gêneros. Como ficaria este diretório?

Para prevenir essa bagunça, a linguagem dispõe de um recurso que organiza as classes padrão e criadas por nós, que conhecemos como pacote (package). Os pacotes são subdiretórios a partir da pasta src do nosso projeto onde estão localizadas as classes da linguagem e novas que forem criadas para o projeto. Existem algumas convenções para criação de pacotes já utilizados no mercado.

## VISIBILIDADE DOS RECURSOS
### MODIFICADORES DE ACESSO
Em java, utilizamos três palavras reservadas e um conceito default(sem nenhuma palavra reservada) para definir os quatros tipos de visibilidade de atributos, métodos e até mesmo classes no que se refere ao acesso por outras classes. Para uma melhor ilustração, serão representados os conceitos de visibilidade de recursos através do contexto de uma lanchonete que vende lanche natural e suco.

## Modificador Public
Como o próprio nome representa, quando nossa classe, método e atributo é definido como public, qualquer outra classe em qualquer outro pacote pode visualizar tais recursos.

## Modificador Default
Está fortemente associado a organização das classes por pacotes, algumas implementações não precisam estar disponíveis por todo o projeto, e este modificador de acesso restringe a visibilidade por pacotes.

Dentro do pacote lanchonete, iremos criar dois sub-pacotes para representar a divisão do estabelecimento.

lanchonete.atendimento.cozinha: Pacote que contém classes da parte da cozinha da lanchonete e atendimentos.

lanchonete.area.cliente: Pacote que contém classes relacionadas ao espaço do cliente.

## Reflexão sobre visibilidade ou modificadores de acesso.
Conhecendo as ações disponíveis nas classes Cozinheiro, Almoxarife, Atendente e Cliente, mesmo com a organização da visibilidade por pacote, será se realmente estas classes precisam ser tão explicitas?

Será se o cozinheiro precisa saber que/como o Almoxarife controla as entradas e saídas?

Que o Cliente precisa saber como o Atendente recebe o pedido para servir sua mesa?

que o Atendente precisa saber que antes de pagar o Cliente consulta o saldo no App?

Dienate desses questionamento é que nossas classes precisam continuar mantendo duas ações (métodos) mas nem todas precisam ser vistas por alguém.

## Modificador Private
Depois de restruturar nosso estabelecimento(projeto) onde, temos as divisões(pacotes) espaço do cliente e atendimento, chegou a hora de uma reflexão sobre visibilidade.