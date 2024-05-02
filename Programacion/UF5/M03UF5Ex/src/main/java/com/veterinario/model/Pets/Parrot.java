package com.veterinario.model.Pets;

import com.veterinario.model.enums.Gender;
import com.veterinario.model.enums.YesNo;
import com.veterinario.model.enums.Specimen;

public class Parrot extends Bird{
    private YesNo speak;
    private YesNo sing;

    public Parrot(String name, int age, Gender gender, Specimen specimen, int freeTime, YesNo speak, YesNo sing) {
        super(name, age, gender, specimen, freeTime);
        this.speak = speak;
        this.sing = sing;
    }

    public YesNo getSpeak() {
        return speak;
    }

    public YesNo isSing() {
        return sing;
    }
}
