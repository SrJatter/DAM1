package com.veterinario.model.treatments;

import com.veterinario.model.Worker;

public class Vacuna extends Treatment{
    private String name;
    private boolean firstTime;

    public Vacuna(Worker worker, double price, String name, boolean firstTime) {
        super(worker, price);
        this.name = name;
        this.firstTime = firstTime;
    }
}
