package veiculos;

public class Veiculo {

    private String marca;
    private String nome;
    private String modelo;
    private String anoFabricacao;
    private String anoModelo;
    private String placa;

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getAnoModelo() {
        return anoModelo;
    }

    public void setAnoModelo(String anoModelo) {
        this.anoModelo = anoModelo;
    }

    public String getAnoFabricacao() {
        return anoFabricacao;
    }

    public void setAnoFabricacao(String anoFabricacao) {
        this.anoFabricacao = anoFabricacao;
    }
    public void verificarCombustivel() {
        System.out.println("Verificando Combustível ...");
    }

    public void verificarCambio() {
        System.out.println("Câmbio em (P)");
    }

    public void imprimirInformacoes() {
        System.out.printf("""
                -----------RESUMO------------
                NOME: %s,
                MARCA: %s,
                MODELO: %s,
                ANO DE FABRICAÇÃO: %s
                \n""", getModelo(), getMarca(), getNome(), getAnoFabricacao());
    }
}
