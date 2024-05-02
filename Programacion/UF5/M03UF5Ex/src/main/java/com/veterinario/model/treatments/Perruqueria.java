package com.veterinario.model.treatments;

import com.veterinario.model.Worker;
import com.veterinario.model.enums.YesNo;

public class Perruqueria extends Treatment{
    private YesNo tall;
    private YesNo rentat;
    private YesNo assecat;

    public Perruqueria(Worker worker, double price, YesNo tall, YesNo rentat, YesNo assecat) {
        super(worker, price);
        this.tall = tall;
        this.rentat = rentat;
        this.assecat = assecat;
    }
}
