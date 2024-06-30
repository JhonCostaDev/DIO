package estados.brasileiros;

public enum EstadosBrasileiros {
    CEARA ("CE", "Fortaleza"),
    SAO_PAULO ("SP", "São Paulo"),
    BAHIA ("BA", "Salvador"),
    GOIAS ("GO", "Goiânia"),
    MARANHAO("MA", "São Luiz");

    private String nome;
    private String sigla;

    private EstadosBrasileiros(String sigla, String nome) {
        this.sigla = sigla;
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public String getSigla() {
        return sigla;
    }

    public String getNomeUpper() {
        return nome.toUpperCase();
    }


}
