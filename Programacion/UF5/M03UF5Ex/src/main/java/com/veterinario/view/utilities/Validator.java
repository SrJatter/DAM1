package com.veterinario.view.utilities;

import com.veterinario.controller.Manager;
import com.veterinario.exceptions.VetException;
import com.veterinario.model.Pets.Pet;
import com.veterinario.model.enums.*;

import java.util.HashMap;

public class Validator {
    private Manager manager = Manager.getInstance();

    public void valLength(String[] command, int expectedLength) throws VetException {
        if(command.length != expectedLength){
            throw new VetException(VetException.WRONG_NUM_ARGS);
        }
    }

    public void valLength(String[] commandParts, Integer min, Integer max) throws VetException {
        if(commandParts.length < min || commandParts.length > max ) {
            throw new VetException(VetException.WRONG_NUM_ARGS);
        }
    }

    public int valInteger(String num) throws VetException {
        try{
            return Integer.parseInt(num);
        } catch (NumberFormatException e){
            throw new VetException(VetException.WRONG_NUM_FORMAT);
        }
    }

    public int valInteger(String num, Integer min, Integer max) throws VetException {
        int iNum = valInteger(num);
        if (min != null && iNum < min) {
            throw new VetException(VetException.NUM_OUT_OF_RANGE);
        }
        if (max != null && iNum > max) {
            throw new VetException(VetException.NUM_OUT_OF_RANGE);
        }
        return iNum;
    }

    public double valDouble(String num) throws VetException {
      try {
          return Double.parseDouble(num);
      } catch (NumberFormatException e){
          throw new VetException(VetException.WRONG_NUM_FORMAT);
      }
    }

    public double valDouble(String num, Double min, Double max) throws VetException {
        double dNum = valDouble(num);
        if (min != null && dNum < min) {
            throw new VetException(VetException.WRONG_NUM_FORMAT);
        }
        if (max != null && dNum > max) {
            throw new VetException(VetException.WRONG_NUM_FORMAT);
        }
        return dNum;
    }

    public Gender getGender(String gender) throws VetException {
        try{
            return Gender.valueOf(gender.toUpperCase());
        } catch (IllegalArgumentException e){
            throw new VetException(VetException.WRONG_GENDER);
        }
    }

    public Size getSize(String size) throws VetException {
        try {
            return Size.valueOf(size.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_SIZE);
        }
    }

    public Speciality getSpeciality(String speciality) throws VetException {
        try {
            return Speciality.valueOf(speciality.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_SPECIALITY);
        }
    }

    public Specimen getSpecimen(String specimen) throws VetException {
        try {
            return Specimen.valueOf(specimen.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_SPECIMEN);
        }
    }
    public HairLenght getHairLength(String lenght) throws VetException {
        try {
            return HairLenght.valueOf(lenght.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_LENGTH);
        }
    }
    public YesNo getYesNo(String yn) throws VetException {
        try {
            return YesNo.valueOf(yn.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_YES_NO);
        }
    }
    public TreatmentEnum getTreatment(String treatment) throws VetException {
        try {
            return TreatmentEnum.valueOf(treatment.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new VetException(VetException.WRONG_TREATMENT);
        }
    }

    public void valPetNotExists(String name) throws VetException {
        HashMap<String, Pet> pets = manager.getPets();
        if(pets.containsKey(name)){
            throw new VetException(VetException.PET_ALREADY_EXISTS);
        }
    }


    public void valPetExists(String name) throws VetException {
        HashMap<String, Pet> pets = manager.getPets();
        if(!pets.containsKey(name)){
            throw new VetException(VetException.PET_NOT_EXISTS);
        }
    }
}
