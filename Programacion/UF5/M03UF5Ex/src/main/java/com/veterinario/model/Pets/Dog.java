package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.HairLenght;
import com.veterinario.model.enums.Size;
import com.veterinario.model.enums.Specimen;

public class Dog extends Pet {
    private HairLenght hairLength;
    private Size size;

    public Dog(String name, int age, Gender gender, Specimen specimen, HairLenght hairLength, Size size) {
        super(name, age, gender, specimen);
        this.hairLength = hairLength;
        this.size = size;
    }

    public HairLenght getHairLenght() {
        return hairLength;
    }

    public Size getSize() {
        return size;
    }
}
