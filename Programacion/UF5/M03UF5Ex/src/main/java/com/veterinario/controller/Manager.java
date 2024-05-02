package com.veterinario.controller;

import com.veterinario.model.Pets.Pet;
import com.veterinario.model.Worker;
import com.veterinario.model.enums.Speciality;
import com.veterinario.model.enums.TreatmentEnum;
import com.veterinario.model.treatments.Treatment;

import java.util.HashMap;
import java.util.HashSet;

public class Manager {
    private static Manager instance;
    // Estos tres son hashMap para poder identificarlos los por clave
    private HashMap<String, Pet> pets;
    private HashMap<String, Worker> workers;
    private HashMap<String, TreatmentEnum> specialPets;
    private int treatmentid = 1;

    private Manager() {
        this.pets = new HashMap<>();
        this.workers = new HashMap<>();
        //Aqui he usado hashSet ya que no habran valores repetidos y tampoco necesito buscar por clave
        HashSet<Speciality> specialities = new HashSet<>();
        specialities.add(Speciality.VETERINARIA);
        specialities.add(Speciality.PERRUQUERIA);
        workers.put("12345678A", new Worker("12345678A", "Mireia", "Montana Mares", 666112233, specialities));
        specialities = new HashSet<>();
        specialities.add(Speciality.VETERINARIA);
        workers.put("55555555Z", new Worker("55555555Z", "Aitor", "Menta Rayos", 656565656, specialities));
        specialities = new HashSet<>();
        specialities.add(Speciality.PERRUQUERIA);
        workers.put("11111111X", new Worker("11111111X", "Leo", "Palomo Sanchez", 646444444, specialities));
        specialities = new HashSet<>();
        specialities.add(Speciality.INFERMERIA);
        workers.put("22222222F", new Worker("22222222F", "Paloma", "Posada Alamo", 619999999, specialities));
    }

    public static Manager getInstance() {
        if(instance == null){
            instance = new Manager();
        }
        return instance;
    }
    public void addPet(String name, Pet pet) {
        pets.put(name, pet);
    }
    public HashMap<String, Pet> getPets() {
        return pets;
    }
    public HashMap<String, Worker> getWorkers() {
        return workers;
    }

    public void addTreatment(String name, Treatment treatment) {
        pets.get(name).getTreatments().put(treatmentid, treatment);
        this.treatmentid ++;
    }

    public int getTreatmentid() {
        return treatmentid;
    }
}
