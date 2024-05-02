package org.example;

public class Main {
    public static void main(String[] args) {
        Coche c1 = new Coche("1234ABC", "Volvo");
        System.out.println("Matricula: " + c1.getMatricula());
        System.out.println("Marca: " + c1.getMarca());
        System.out.println("Velocidad: " + c1.getVelocidad());
        Coche c2 = new Coche("8888XXX");
        System.out.println("Matricula: "+ c2.getMatricula());
        System.out.println("Marca: " + c2.getMarca());
        System.out.println("Velocidad: "+ c2.getVelocidad());
        for (int i= 0; i< 10; i++) {
            c1.acelerar();
        }
        c2.acelerar();
        System.out.println("Velocidad coche1: " + c1.getVelocidad());
        System.out.println("Velocidad coche2: " + c2.getVelocidad());
    }

}