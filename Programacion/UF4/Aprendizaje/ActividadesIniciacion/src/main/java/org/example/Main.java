package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String name = "";
        int entero = 0;
        short pequeno = 2;
        long grande = 12345;
        boolean encontrado = false;
        double decimalGrande = 5.6;
        float decimal = 5.6f;
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Escribe tu nombre");
        name = input.readLine();
        System.out.println("Hola " + name + "!");
        System.out.println("Introduce un numero entero:");
        entero = Integer.parseInt(input.readLine());
        System.out.println("Numero introducido: " + entero);
    }
}
