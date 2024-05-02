package com.veterinario.model.treatments;

import com.veterinario.model.Worker;
import com.veterinario.model.enums.YesNo;

public class Cura extends Treatment{
    private YesNo trencat;

    public Cura(Worker worker, double price, YesNo trencat) {
        super(worker, price);
        this.trencat = trencat;
    }
}
