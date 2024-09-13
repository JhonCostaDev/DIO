#!/bin/bash

# Verificar se o nome da classe foi passado como argumento.

if [ -z "$1" ]; then
	echo "Uso: $0 NomeClasse"
	exit 1
fi

# Nome da classe
CLASS_NAME=$1

#Compilar o arquivo. java
javac -d classes $CLASS_NAME

# Verificar se a compilacao deu certo

if [ $? -eq 0 ]; then
	#executa a classe compilada
	java -cp classes $CLASS_NAME
else
	echo "Erro de Compilação."
fi
 
