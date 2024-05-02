package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.Specimen;

public class Bird extends Pet {
    private int freeTime;

    public Bird(String name, int age, Gender gender, Specimen specimen, int freeTime) {
        super(name, age, gender, specimen);
        this.freeTime = freeTime;
    }
    public int getFreeTime() {
        return freeTime;
    }

}
