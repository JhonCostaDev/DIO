package edu.jhoncostadev.servicosmensagem.app;

public abstract class ServicoMensagem {
    public abstract void enviarMensagem();
    public abstract void receberMensagem();

    //somente os filhos conhecem este metodo.
    protected void validarConexaoInterner() {
        System.out.println("Validando conexão com a Internet...");
    }
}
