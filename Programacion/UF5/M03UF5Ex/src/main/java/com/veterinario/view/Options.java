package com.veterinario.view;

import com.veterinario.controller.Manager;
import com.veterinario.model.Pets.*;
import com.veterinario.model.Worker;
import com.veterinario.model.enums.*;
import com.veterinario.model.treatments.Cura;
import com.veterinario.model.treatments.Perruqueria;
import com.veterinario.model.treatments.Revisio;
import com.veterinario.view.messages.Message;
import com.veterinario.exceptions.VetException;
import com.veterinario.view.utilities.Utils;
import com.veterinario.view.utilities.Validator;

import java.util.HashMap;

public class Options {
    private String[] command;
    private Manager m = Manager.getInstance();
    private HashMap<String, Pet> pets;
    private Validator vl = new Validator();
    private Utils u = new Utils();
    private Message ms = new Message();

    public void setCommand(String[] command){
        this.command = command;
    }
    public void registerPet() throws VetException {
        vl.valLength(command,6, 8);
        String name = command[1];
        vl.valPetNotExists(name);
        int age = vl.valInteger(command[2], 0, 50 );
        Gender gender = vl.getGender(command[3]);
        Specimen specimen =  vl.getSpecimen(command[4]);
        pets = m.getPets();
        if (specimen.equals(Specimen.GAT)) {
            vl.valLength(command, 6);
            int sleepHours = vl.valInteger(command[5], 0,24);
            m.addPet(name, new Cat(name, age, gender, specimen, sleepHours));
        } else if (specimen.equals(Specimen.GOS)) {
            vl.valLength(command, 7);
            HairLenght hairLenght = vl.getHairLength(command[5]);
            Size size = vl.getSize(command[6]);
            m.addPet(name, new Dog(name, age, gender, specimen, hairLenght, size));
        } else if (specimen.equals(Specimen.LLORO)) {
            vl.valLength(command, 8);
            int freeTime = vl.valInteger(command[5]);
            YesNo speak = vl.getYesNo(command[6]);
            YesNo sing = vl.getYesNo(command[7]);
            m.addPet(name, new Parrot(name,age, gender, specimen, freeTime, speak, sing));
        } else {
            vl.valLength(command, 7);
            int freeTime = vl.valInteger(command[5]);
            int height = vl.valInteger(command[6], 1, 25);
            m.addPet(name, new Agaporni(name, age, gender, specimen, freeTime, height));
        }
        System.out.println(ms.getMessage(Message.ADDED_PET));
    }

    public void registerTreatment() throws VetException {
        vl.valLength(command, 4);
        vl.valPetExists(command[1]);
        String name = command[1];
        TreatmentEnum treatment = vl.getTreatment(command[2]);
        Worker worker = u.searchWorker(treatment);
        double price = 0;
        if (treatment.equals(TreatmentEnum.PERRUQUERIA)) {
            price += 10;
            YesNo tall = vl.getYesNo(command[3]);
            if (tall.equals(YesNo.SI)) {
                price += 9.99;
            }
            YesNo rentat = vl.getYesNo(command[4]);
            if (rentat.equals(YesNo.SI)) {
                price += 5.15;
            }
            YesNo assecat = vl.getYesNo(command[5]);
            if (assecat.equals(YesNo.SI)) {
                price += 8.75;
            }
            m.addTreatment(name, new Perruqueria(worker, price, tall, rentat, assecat));
        } else if (treatment.equals(TreatmentEnum.REVISIO)) {
            Pet pet = m.getPets().get(name);
            if (pet instanceof Cat || pet instanceof Dog) {
                price = 30;
            } else {
                price = 25;
            }
            m.addTreatment(name, new Revisio(worker, price, command[3]));
        } else if (treatment.equals(TreatmentEnum.CURA)) {
            price = 35.25;
            YesNo trencat = vl.getYesNo(command[3]);
            if (trencat.equals(YesNo.SI)) {
                price += 51.50;
            }
            m.addTreatment(name, new Cura(worker, price, trencat));
        } else {
            throw new VetException(VetException.NOT_IMPLEMENTED);
        }
        int code = m.getTreatmentid() -1;
        String[] args = {String.valueOf(code)};
        System.out.println(ms.getMessage(Message.ADDED_TREATMENT, args));
    }

    public void petDetails() throws VetException {
        vl.valLength(command, 2);
        String name = command[1];
        vl.valPetExists(name);
        throw new VetException(VetException.NOT_IMPLEMENTED);
    }

}
