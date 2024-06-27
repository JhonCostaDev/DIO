package escola2;

 public class Aluno {
    private String nome;
    private String idade;
    private String endereco;    


    
    public Aluno(String nome, String idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String newEndereco) {
        endereco = newEndereco;
    }

    public String getNome() {
        return nome;
    }

    public String getIdade() {
        return idade;
    }
}