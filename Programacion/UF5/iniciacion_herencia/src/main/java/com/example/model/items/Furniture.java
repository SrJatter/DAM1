package com.example.model.items;

import com.example.model.enums.IType;
import com.example.model.enums.Studies;

public class Furniture extends Item {
    private int decorLevel;

    public Furniture(String name, Studies typeStudy, int price) {
        super(name, typeStudy, price, IType.MOBLE);
        this.decorLevel = (int) (price*0.1);
    }

    @Override
    public String toString() {
        return "MOBLE: " + super.toString() + "Decoració: " + decorLevel;
    }

    public int getDecorLevel() {
        return decorLevel;
    }
}
