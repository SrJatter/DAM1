package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.Specimen;
import com.veterinario.model.treatments.Treatment;


import java.util.HashMap;

public class Pet {
    private String name;
    private int age;
    private Gender gender;
    private Specimen specimen;
    //Aqui he usado hashMap para poder identificar los tratamientos su codigo
    private HashMap<Integer, Treatment> treatments;

    public Pet(String name, int age, Gender gender, Specimen specimen) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.specimen = specimen;
        this.treatments = new HashMap<>();
    }

    @Override
    public String toString() {
        return "---     Expedient de  " + name + "      ---\n" +
                "Edat:" + age + " Genere: " + gender + "\n" +
                "----------------------------------------\n" +
                ", specimen=" + specimen +
                ", treatments=" + treatments +
                '}';
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public Gender getGender() {
        return gender;
    }

    public Specimen getSpecimen() {
        return specimen;
    }

    public HashMap<Integer, Treatment> getTreatments() {
        return treatments;
    }
}
