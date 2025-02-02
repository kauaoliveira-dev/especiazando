/*Calculadora Simples:
        Crie uma calculadora simples que possa realizar operações básicas (adição, subtração, multiplicação e divisão) entre dois números fornecidos pelo usuário.*/

import java.util.Scanner;

public class mCalculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o primeiro número:");
        double num1 = scanner.nextDouble();

        System.out.println("Digite o segundo número:");
        double num2 = scanner.nextDouble();

        System.out.println("Escolha a operação (+, -, *, /):");
        char operacao = scanner.next().charAt(0);

        double resultado;

        switch (operacao) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    resultado = num1 / num2;
                } else {
                    System.out.println("Erro: Divisão por zero não é permitida.");
                    return;
                }
                break;
            default:
                System.out.println("Operação inválida.");
                return;
        }

        System.out.println("O resultado é: " + resultado);
    }
}
