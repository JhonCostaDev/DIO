public class FormatadorCep {
    public static void main(String[] args) {
        
    }
    static String formatarCep(String cep) throws CepInvalidationException {
        if(cep.length() != 8) {
            throw new CepInvalidationException();

            //simulando cep formatado
            return "12.345-678";
        }
    }    
}
