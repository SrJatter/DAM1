package org.example;

public class Error {
    public static void main(String[] name) {
        double x = 3.2;
        double result = Float.parseFloat(name[0]) + x;
        double original = result;
        result = Math.floor(result);
        double resultado = (original - result) * 10;
        resultado = Math.round(resultado);
        System.out.println(resultado);
        resultado = (resultado/10) + result;
        result = resultado;
        System.out.println(result);
        if (result == 7.3) {
            System.out.print("Igual");
        } else {
            System.out.print(result);
        }
    }
}
