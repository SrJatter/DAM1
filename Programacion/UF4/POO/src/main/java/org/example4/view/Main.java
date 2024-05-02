package org.example4.view;

import org.example4.model.CoffeMachine;
import org.example4.model.CoffeShop;

import java.io.IOException;
import java.security.PublicKey;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // HashMap<String, CoffeShop>
        ArrayList<CoffeShop> cafeterias = new ArrayList<>();
        AskData askData = new AskData();
        int opcion;
        int subopcion1;
        int subopcion2;
        String nombreCafeteria;
        int nrCafeteria;
        String nombreCafetera;
        int maxCapacity;
        int capacity;
        String ciudad;
        do {
            clearScreen();
            showMenu();
            opcion = askData.askInt("Escoge una opción:");
            switch (opcion) {
                case 1:
                    clearScreen();
                    nombreCafeteria = askData.askStr("Introduce el nombre de la cafeteria:", true);
                    ciudad = askData.askStr("Introduce la ciudad:", true);
                    cafeterias.add(new CoffeShop(nombreCafeteria, ciudad));
                    break;
                case 2:
                    clearScreen();
                    if (!cafeterias.isEmpty()) {
                        System.out.println("Selecciona una de las cafeterias");
                        showCoffeStores(cafeterias);
                        nrCafeteria = askData.askInt("Selecciona una de las cafeterias:", "Numero incorrecto", 1, cafeterias.size())-1;
                        subopcion1 = askData.askInt("Escoge una opcion:", "Opcion incorrecta", 1, 3);
                        switch (subopcion1) {
                            case 1:
                                cafeterias.get(nrCafeteria).addCoffeMAchine(new CoffeMachine());
                                break;
                            case 2:
                                maxCapacity = askData.askInt("Introduce la capacidad maxima de la cafetera:","El numero ha de ser mayor a 0", 1);
                                cafeterias.get(nrCafeteria).addCoffeMAchine(new CoffeMachine(maxCapacity));
                                break;
                            case 3:
                                maxCapacity = askData.askInt("Introduce la capacidad maxima de la cafetera:","El numero ha de ser mayor a 0", 1);
                                capacity = askData.askInt("Introduce la capacidad actual de la cafetera");
                                cafeterias.get(nrCafeteria).addCoffeMAchine(new CoffeMachine(capacity, maxCapacity));
                                break;
                        }
                        System.out.println("Cafetera registrada correctamente");
                        askData.askStr("Pulsa enter para continuar");
                    } else {
                        System.out.println("No hay cafeterias registradas");
                    }
                    break;
                case 3:
                    do {
                        clearScreen();
                        System.out.println("Selecciona una de las cafeterias");
                        showCoffeStores(cafeterias);
                        nrCafeteria = askData.askInt("Selecciona una de las cafeterias:", "Numero incorrecto", 1, cafeterias.size())-1;
                        showSubMenu2();
                        subopcion2 = askData.askInt("Escoge una opcion:");
                        switch (subopcion2) {
                            case 1:
                                System.out.println("Selecciona una de las cafeterias");
                                showCoffeStores(cafeterias);
                                nrCafeteria = askData.askInt("Selecciona una de las cafeterias:", "Numero incorrecto", 1, cafeterias.size())-1;

                                break;
                            case 2:

                                break;
                            case 3:
                                break;
                            case 4:
                                break;
                            case 5:
                                break;
                            case 6:
                                askData.askStr("Presiona enter para volver al menu principal");
                                break;
                            default:
                                System.out.println("Opción incorrecta");
                        }

                    } while (subopcion2 != 6);
                    break;
                case 4:
                    System.out.println("Cafeterias registradas");
                    showCoffeStores(cafeterias);
                    askData.askStr("Pulsa enter para continuar");
                    break;
                case 5:
                    System.out.println("Hasta la próxima");
                    break;
                default:
                    System.out.println("Opción incorrecta");
            }
        } while (opcion != 5);
    }
    public static void showMenu() {
        System.out.println("Cafeterías La Pera Limonera");
        System.out.println("1. Registrar cafetería");
        System.out.println("2. Registrar cafetera");
        System.out.println("3. Trabajar en una cafetería.");
        System.out.println("4. Mostrar cafeterías");
        System.out.println("5. Salir");
    }
    public static void showSubMenu1(){
        System.out.println("Que tipo de cafetera quieres añadir?");
        System.out.println("1. Nueva");
        System.out.println("2. Llena");
        System.out.println("3. Usada");
    }
    public static void showSubMenu2() {
        System.out.println("Que accion quieres realizar?");
        System.out.println("1. Seleccionar otra cafeteria");
        System.out.println("2. Llenar la cafetera");
        System.out.println("3. Vaciar cafetera");
        System.out.println("4. Añadir cafe");
        System.out.println("5. Servir un Cafe");
        System.out.println("6. Atrás");
    }
    public static void showCoffeStores(ArrayList<CoffeShop> storeList) {
        for (int i = 0; i < storeList.size(); i++) {
            System.out.println((i + 1) + ". " + storeList.get(i));
        }
    }
    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
}