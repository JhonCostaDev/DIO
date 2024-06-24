Trilha Java Básico - DIO

# Orientação a objetos

## Objetivos do curso
Abordar os conceitos do paradigma e os pilares da orientação a objetos, classes, enums, construtores, Java Bens e UML

## Assuntos
* Conceito POO
* Pacotes e Visibilidade de recursos
* Classes e Construtores
* Java Beans e UML
* Pilares do POO
* Enums e Interfaces


## Conceito POO
POO é um paradigma de programação baseado no conceito de **"Objetos"**, que podem conter dados na forma de campos, também conhecidos como atributos, e código, na forma de procedimentos, também conhecidos como métodos.

Enquanto a programação estruturada é voltada a procedimentos e funções definidas pelo usuário, a programação orientada a objetos é voltada a conceitos como o de classes e objetos.

## Classes
Toda a estrutura de código na linguagem Java é distribuído em arquivos com extensão **.java** denominados de **classe**.

As classes existentes em nosso projeto serão composta por: **Identificador, Características e Comportamentos.

* **Classe**(class): A estrutura e ou represetnação que direciona a criação dos objetos de mesmo tipo.

* **Identificador** (identity): Propósio existencial aos objetos que serão criados.

* **Características** (states): Também conhecidos como **atributos** ou **propriedades**, é toda informação que representa o estado do objeto.

* **Comportamentos** (behavior): Também conhecido como **ações** ou **métodos**, é toda parte comportamental que um objeto dispõe.

* **Instanciar** (new): É o ato de criar um objeto a partir de uma estrutura definida em uma classe. 

### CLASSES E OBJETOS
![](../img/classes.png)

#### Criando uma Classe Student
```Java
//Criando  classe Student
//Com todas as caraterísticas e comportamentos aplicados

public class Student {
    String name;
    int age;
    Color color;
    Sex sex;

    void eating(Food food) {
        //Código aqui
    }

    void drinking(Eat eat) {
        //Código aqui
    }

    void running() {
        //Código aqui
    }
}
```
#### Criando Objetos da classe Student


```Java
public class School {
    public static void main(String [] args) throws Exception {
        Student estudante1 = new Studen();
        estudante1.name = "John";
        estudante1.age = 12;
        estudante1.color = Color.FAIR;
        estudante1.sex = Sex.MALE;

        Student estudante2 = new Studen();
        estudante2.name = "Sophia";
        estudante2.age = 10;
        estudante2.color = Color.DARK;
        estudante2.sex = Sex.FEMALE
    }
}
```

## IMPORTANTE
No exemplo acima, a classe Student **NÃO** foi estruturada com o padrão **Java Beans** com **getters e setters**.

Seguindo algumas convenções, as nossas classes são classificadas como:
* **Classe de modelo(model)**: Classes que representem estrutura de domínio da aplicação, exemplo: Cliente, Pedido, Nota Fiscal e etc.

* **Classe de serviço(service)**: Classes que contém regras de negócio e validação de nosso sistema.

* **Classe de repositório(repository)**: Classes que contém uma integração com banco de dados. 

* **Classe de controle(controller)**: Classes que possuem a finalidade de disponibilizar alguma comunicação externa à nossa aplicação, tipo **http web ou webservices**.

* **Classe Utilitária(util)**: Classe que contém recursos comuns à toda nossa aplicação.