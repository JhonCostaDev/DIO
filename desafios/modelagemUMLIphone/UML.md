```mermaind
@startuml
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
  - modelo: String
  - numeroSerie: String
  - armazenamento: int
  - bateria: int
  - ligado: boolean
  - musicaAtual: String
  - paginaAtual: String
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
@enduml

```