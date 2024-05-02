package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.Specimen;

public class Agaporni extends Bird{
    private int height;

    public Agaporni(String name, int age, Gender gender, Specimen specimen, int freeTime, int height) {
        super(name, age, gender, specimen, freeTime);
        this.height = height;
    }

    public int getHeight() {
        return height;
    }
}
