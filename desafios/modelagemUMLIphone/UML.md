```mermaind

interface Telefone {
  + ligar()
  + atender()
  + iniciarCorreioVoz()
}

interface ReprodutorMusical {
  + tocar()
  + pausar()
  + selecionarMusica()
}

interface Internet {
  + exibirPagina()
  + adicionarNovaAba()
  + atualizarPagina()
}

class Iphone {
  + ligar()
  + desligar()
  + conectarInternet()
  + fazerLigacao(numero: String)
  + reproduzirMusica(musica: String)
  + abrirNavegador()
}
Iphone -> Telefone
Iphone -> ReprodutorMusical
Iphone -> Internet


```
