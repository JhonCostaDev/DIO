package lanchonete.atendimento.cozinha;

import lanchonete.atendimento.Atendente;

public class Cozinheiro {
    public void adicionarLancheNoBalcao() {
        System.out.println("ADICIONANDO LANCHE NO BALCAO");
    }

    public void adicionarSucoNoBalcao(){
        System.out.println("ADICIONANDO SUCO NO BALCAO");
    }

    private void adicionarComboNoBalcao(){
        adicionarLancheNoBalcao();
        adicionarSucoNoBalcao();
    }

    private void prepararLanche(){
        System.out.println("PREPARANDO LANCHE TIPO ...");
    }

    private void prepararVitamina(){
        System.out.println("PREPARANDO SUCO");
    }

    public void prepararCombo(){
        prepararLanche();
        prepararVitamina();
    }

    private void selecionarIngradientesLanche() {
        System.out.println("SELECIONANDO PAO, SALADA, LEGUMES ...");
    }

    private void selecionarIngradientesVitamina() {
        System.out.println("SELECIONANDO FRUTA, LEITE ...");
    }

    private void lavarIngradientes() {
        System.out.println("LAVANDO OS INGREDIENTES");
    }

    private void baterVitaminaLiquidificador() {
        System.out.println("BATENDO VITAMIN");
    }

    private void fritarIngradientesLanche() {
        System.out.println("FRITANDO A CARNE E OVO");
    }

    private void pedirTrocaGas(Almoxarife meuAmigo) {
        meuAmigo.trocarGas();
    }

    private void pedirIngradientes(Almoxarife almoxarife) {
        almoxarife.entregarIngredientes();
    }
}
