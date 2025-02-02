/*Verificação de Palíndromo:
        Escreva um programa que verifique se uma string é um palíndromo (lê-se da mesma forma de trás para frente)*/

import java.util.Scanner;

public class fVerificPalíndromo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escreva um palindromo");
        String leitura = sc.next();
        System.out.println("você escreveu: "+leitura);
        String leitura2 = new StringBuilder(leitura).reverse().toString();
        System.out.println(leitura+" "+leitura2);
        if (leitura == leitura && leitura == leitura2){
            System.out.println("Isso é um palíndromo.");
        }
    else {
            System.out.println("Isso não é um palíndromo.");
        }
    }
}
