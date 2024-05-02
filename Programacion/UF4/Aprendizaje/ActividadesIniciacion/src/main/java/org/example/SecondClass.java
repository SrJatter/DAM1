package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SecondClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println("Introduce tu edad:");
//        int edad = Integer.parseInt(br.readLine());
//        if (edad >= 50) {
//            System.out.println("Estas en la mejor edad");
//        } else if (edad >= 30) {
//            if (edad >= 40) {
//                System.out.println("Edad de oro");
//            }
//            System.out.println("Ni chicha ni limoná");
//        } else {
//            System.out.println("Disfruta de la vida");
//        }
//        System.out.println("De que instrumento quieres partituras?");
//        String instrumento = br.readLine();
//        switch (instrumento.toLowerCase()) {
//            case "piano":
//                System.out.println("8888 partituras");
//                break;
//            case "guitarra":
//                System.out.println("324 partituras");
//                break;
//            case "saxofon":
//                System.out.println("56 partituras");
//                break;
//            default:
//                System.out.println("No hay partituras de ese instrumento");
//        }
        String str = "Hola";
        for (String i = str; !i.equals("exit"); i = str){
            str = br.readLine();
        }
    }
}
