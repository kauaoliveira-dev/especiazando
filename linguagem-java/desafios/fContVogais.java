/*Contagem de Vogais:
        Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.*/

import java.util.Scanner;

public class fContVogais {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escreva uma frase");
        String leitura = sc.next();
        System.out.println("você escreveu: " + leitura);
        int cont = leitura.length();
        System.out.println("A quantidade de caracteres são:" + cont);
    }
}
