package com.example.view;

import com.example.exceptions.CrossingException;


public class Menu {
    InputData input = new InputData();
    Options op = new Options();
    public void menu(){
        String option;
        do {
            System.out.print("> ");
            String[] command = input.askStr().trim().split(" ");
            op.setCommand(command);
            option = command[0].toLowerCase();
            try {
                switch (option) {
                    case "r":
                        op.registerPlayer();
                        break;
                    case "a":
                        op.registerNPC();
                        break;
                    case "c":
                        op.createItem();
                        break;
                    case "i":
                        op.infoPlayer();
                        break;
                    case "b":
                        op.buyItem();
                        break;
                    case "m":
                        op.move();
                        break;
                    case "f":
                        op.makeFriends();
                        break;
                    case "p":
                        op.seeCharactersInPlace();
                        break;
                    case "v":
                        op.showAllData();
                        break;
                    case "k":
                        op.ranking();
                        break;
                    case "x":
                        System.out.println("Saliendo...");
                        break;
                    default:
                        throw new CrossingException(CrossingException.WRONG_OPERATION);
                }
            } catch (CrossingException e){
                System.out.println(e.getMessage());
            }
        } while (!option.equals("x"));
    }
}
