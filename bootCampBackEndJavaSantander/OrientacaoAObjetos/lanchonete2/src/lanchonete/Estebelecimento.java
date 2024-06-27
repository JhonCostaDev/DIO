package lanchonete;

import lanchonete.area.cliente.Cliente;
import lanchonete.atendimento.Atendente;
import lanchonete.atendimento.cozinha.Almoxarife;
import lanchonete.atendimento.cozinha.Cozinheiro;

public class Estebelecimento {
    public static void main(String[] args) {
        Cozinheiro cozinheiro = new Cozinheiro();
        cozinheiro.lavarIngradientes();
        cozinheiro.baterVitaminaLiquidificador();
        cozinheiro.selecionarIngradientesLanche();
        cozinheiro.selecionarIngradientesVitamina();
        cozinheiro.prepararLanche();
        cozinheiro.prepararVitamina();


        //ações que estabelecimento precisa ter
        cozinheiro.adicionarSucoNoBalcao();
        cozinheiro.adicionarLancheNoBalcao();
        cozinheiro.adicionarComboNoBalcao();


        //atendente
        Atendente atendente = new Atendente();
        atendente.pegarLancheCozinha();
        atendente.receberPagamento();
        atendente.receberPagamento();
        atendente.servindoMesa();


        Cliente cliente = new Cliente();
        cliente.escolherLanche();
        cliente.fazerPedido();
        cliente.pagarConta();

        //

        cliente.consultarSaldoAplicativo();


        cozinheiro.pedirTrocaGas(almoxarife);
    }
}
