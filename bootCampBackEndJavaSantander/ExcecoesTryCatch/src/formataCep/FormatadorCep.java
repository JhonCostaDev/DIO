package formataCep;
public class FormatadorCep {
    public static void main(String[] args) {
        try {
            String cepFormatado = formatarCep("98768532");
            System.out.println(cepFormatado);
        } catch (CepInvalidationException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
     
    static String formatarCep(String cep) throws CepInvalidationException{
        if(cep.length()!= 8) {
            throw new CepInvalidationException();
        } 

        return "12.345-678";
    }
}
