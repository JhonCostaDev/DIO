package lanchonete.atendimento.cozinha;

public class Almoxarife {
    private void controlarEntradas() {
        System.out.println("CONTROLANDO ENTRADA DE  ITENS");
    }

    private void controlarSaida() {
        System.out.println("CONTROLANDO SAIDA DE ITENS");
    }

     void entregarIngredientes() {
        System.out.println("ENTREGANDO INGREDIENTES");
        controlarSaida();
    }

     void trocarGas() {
        System.out.println("ALMOXARIFE TROACANDO O GAS...");
    }
}
