package org.examen.view;

public class Menu {
    InputData input = new InputData();
    Options op = new Options();

    public void menu(){
        String option;
        do{
            showMainMenu();
            option = input.askStr("Indica una opció:").trim();
            switch (option){
                case "1":
                    op.addPlat();
                    break;
                case "2":
                    op.cookPlat();
                    break;
                case "3":
                    op.sellPlat();
                    break;
                case "4":
                    op.favPlat();
                    break;
                case "5":
                    op.showCarta();
                    break;
                case "6":
                    op.stats();
                    break;
                case "7":
                    System.out.println("Sortint del programa...");
                    break;
                default:
                    System.out.println("Opció invàlida");
                    System.out.println("Prem enter per continuar:");
                    input.askNothing();
            }
        } while (!option.equals("7"));
    }
    public void showMainMenu(){
        System.out.println("***** Tàpers Thor Tilla *****");
        System.out.println("1. Registrar plat");
        System.out.println("2. Cuinar plat");
        System.out.println("3. Vendre plat");
        System.out.println("4. Plat favorit");
        System.out.println("5. Mostrar carta");
        System.out.println("6. Estadístiques");
        System.out.println("7. Sortir");
    }
}
