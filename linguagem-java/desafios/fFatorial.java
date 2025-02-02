/*Fatorial:
        Crie uma função que calcule o fatorial de um número inteiro positivo fornecido pelo usuário.*/

import java.util.Scanner;

public class fFatorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escreva um numero acima de zero e que não seja letra");
        int leitura = sc.nextInt();
        System.out.println("Você escreveu: " + leitura);
        for (int i = leitura-1; i >= 1; i--){
                leitura *= i;
                System.out.println(leitura);
        }

    }
}
