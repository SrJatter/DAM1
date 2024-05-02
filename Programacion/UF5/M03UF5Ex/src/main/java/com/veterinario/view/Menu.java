package com.veterinario.view;

import com.veterinario.exceptions.VetException;
import com.veterinario.view.utilities.Validator;

public class Menu {
    InputData input = new InputData();
    Options op = new Options();
    Validator vl = new Validator();

    public void menu(){
        String option;
        do{
            String[] command = input.askStr().trim().split("-");
            op.setCommand(command);
            option = command[0].toLowerCase();
            try{
                switch(option){
                    case "p":
                        op.registerPet();
                        break;
                    case "r":
                        op.registerTreatment();
                        break;
                    case "v":
                        op.petDetails();
                        break;
                    case "e":
                        vl.valLength(command, 1);
                        System.out.println("Saliendo...");
                        break;
                    default:
                        throw new VetException(VetException.WRONG_OPERATION);
                }
            } catch (VetException e){
                System.out.println(e.getMessage());
            }
        } while(!option.equals("e"));
    }
}

