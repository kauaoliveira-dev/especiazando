/*Conversão de Moeda:
        Desenvolva um programa que converta uma quantia de uma moeda para outra (ex.: Real para Dólar), utilizando uma taxa de câmbio fornecida pelo usuário.*/

import java.util.Scanner;

public class mConvertMoney {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita ao usuário a quantia a ser convertida
        System.out.print("Digite a quantia a ser convertida: ");
        double quantia = scanner.nextDouble();

        // Solicita ao usuário a taxa de câmbio
        System.out.print("Digite a taxa de câmbio (ex.: 5.23 para Real para Dólar): ");
        double taxaCambio = scanner.nextDouble();

        // Realiza a conversão
        double quantiaConvertida = converterMoeda(quantia, taxaCambio);

        // Exibe o resultado
        System.out.printf("A quantia convertida é: %.2f%n", quantiaConvertida);

        scanner.close();
    }

    public static double converterMoeda(double quantia, double taxaCambio) {
        return quantia * taxaCambio;
    }
}
