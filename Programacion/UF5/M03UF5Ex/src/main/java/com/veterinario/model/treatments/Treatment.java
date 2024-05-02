package com.veterinario.model.treatments;

import com.veterinario.model.Worker;

public class Treatment {
    private Worker worker;
    private double price;

    public Treatment(Worker worker, double price) {
        this.worker = worker;
        this.price = price;
    }
}
