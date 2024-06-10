# Sistema para validação de candidados em um processo seletivo

Explorar alguns cenário com fluxo condicionais, repetições e excepcionais.

## Case 1: 
Vamos imaginar um processo seletico onde o valor salarial base é 
de R$ 2000,00, e o salário pretendido pelo candidato. Elaborar um 
controle de fluxo onde:
* Se o valor salario base for maior que o valo de salário pretendido,
retorne (LIGAR PARA O CANDIDATO);

* Senão, se o valor do salário base for igual ao valor do salário pretendido, retorne (LIGAR PARA O CANDIDATO COM CONTRA PROPOSTA);

* Senão retorne: (AGUARDANDO RESULTADO DOS DEMAIS CANDIDATOS).

TODO: Fazer projeto utilizando médotos para cara função da aplicação
Ex: * um para coleta de dados
* outro para comparação
* outro para armazanamento em arrays
TODO: Criar branch secundária para modificação e estudo git

# SELECIONANDO CANDIDATOS

Case 2: Foi solicitado que nosso sistema garanta que diante das inúmeras 
candidaturas, sejam selecionados apenas no máximo 5 candidados para 
entrevista, onde o salário pretendido seja menor ou igual ao salário base.

// array com a lista de candidatos
String[] candidatos = {"FELIPE", "MARCIA", "JULIA", "PAULO", "AUGUSTO", "MONICA", "FABRICIO", "MIRELA", "DANIELA", "JORGE"};

// Método que simula o valor pretendido

import java.util.concurrent.ThreadLocalRandom;

static double valorPretendido() {
return ThreadLocalRandom.current().nextDouble(1800,2200);
}


# IMPRIMINDO LISTA COM CANDIDATOS SELECIONADOS
Case 3: Agora é hora de imprimir a lista dos candidatos selecionados para 
disponibilizar para o RH entrar em contato.

# FAZENDO LIGAÇÕES PARA OS CANDIDATOS SELECIONADOS
Case 4: O rh deverá realizar uma ligação com no máximo 3 tentativas para cada 
candidato selecionado e caso o candidato atenda, deve-se imprimir:
"Conseguimos contato com [candidato] após [tentativas] tentativas"

Caso contrário imprima
"Não conseguimos contato com o candidato[candidato]"




















