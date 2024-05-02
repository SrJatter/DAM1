package org.example3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.Objects;
public class Banco {
    public static void main(String[] args) throws IOException {
        Cuenta[] cuentas = new Cuenta[2];
        cuentas[0] = new Cuenta("ES01234", 1200, "Pepe");
        cuentas[1] = new Cuenta("ES3210", 300, "Manolo");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int option;
        int cuentaClienete;
        double dinero;
        int count;
        int count2;
        int cuenta2;
        System.out.println("Que cuenta quieres consultar?");
        count = 1;
        for (Cuenta c : cuentas){
            System.out.println(count + ". Numero de cuenta: "+ c.getIban() + " Titular: " + c.getTitular());
            count += 1;
        }
        cuentaClienete = Integer.parseInt(input.readLine()) -1;
        while (cuentaClienete +1 > cuentas.length){
            System.out.print("Opcion invalida, vuelve a intentarlo: ");
            cuentaClienete = Integer.parseInt(input.readLine()) -1;
        }
        do {
            System.out.println("\n1. Consultar saldo.");
            System.out.println("2. Ingresar dinero.");
            System.out.println("3. Sacar dinero.");
            System.out.println("4. Realizar transferencia (sacar dinero de una cuenta para ponerlos en otra).");
            System.out.println("5. Salir");
            option = Integer.parseInt(input.readLine());
            if (option == 1){
                System.out.println("Tu saldo es: " + cuentas[cuentaClienete].getSaldo());
            } else if (option == 2) {
                System.out.print("Cantidad a ingresar: ");
                dinero = Double.parseDouble(input.readLine());
                cuentas[cuentaClienete].ingreso(dinero);
                System.out.println("Ingreso realizado correctamente");
            } else if (option == 3) {
                System.out.print("Cantidad a retirar: ");
                dinero = Double.parseDouble(input.readLine());
                cuentas[cuentaClienete].retiro(dinero);
                System.out.println("Retiro realizado correctamente");
            } else if (option == 4) {
                System.out.println("\nA que cuenta quieres hacer la transferencia?");
                count = 1;
                count2 = 1;
                for (Cuenta c : cuentas){
                    if (!Objects.equals(c.getIban(), cuentas[cuentaClienete].getIban())){
                        System.out.println(count + ". Numero de cuenta: "+ c.getIban() + " Titular: " + c.getTitular());
                        count2 += 1;
                    }
                    count += 1;
                }
                cuenta2 = Integer.parseInt(input.readLine()) -1;
                while (cuenta2 +1 > count2){
                    System.out.print("Opcion invalida, vuelve a intentarlo: ");
                    cuenta2 = Integer.parseInt(input.readLine()) -1;
                }
                System.out.print("Cuanto dinero quieres transferir: ");
                dinero = Double.parseDouble(input.readLine());
                cuentas[cuentaClienete].retiro(dinero);
                cuentas[cuenta2].ingreso(dinero);
                System.out.println("Transferencia realizada correctamente");
            } else if (option != 5) {
                System.out.println("Opcion invalida");
            }
        } while (option != 5);
    }
}
