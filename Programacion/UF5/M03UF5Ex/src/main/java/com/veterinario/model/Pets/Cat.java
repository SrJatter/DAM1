package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.Specimen;

public class Cat extends Pet {
    private int sleepHours;

    public Cat(String name, int age, Gender gender, Specimen specimen, int sleepHours) {
        super(name, age, gender, specimen);
        this.sleepHours = sleepHours;
    }

    public int getSleepHours() {
        return sleepHours;
    }
}
