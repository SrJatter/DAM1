package com.veterinario.model.treatments;

import com.veterinario.model.Worker;

public class Revisio extends Treatment{
    private String observacion;

    public Revisio(Worker worker, double price, String observacion) {
        super(worker, price);
        this.observacion = observacion;
    }
}
