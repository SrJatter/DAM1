package com.example.model.items;

import com.example.model.enums.Color;
import com.example.model.enums.IType;
import com.example.model.enums.Studies;

public class Flower extends Item {
    private Color color;

    public Flower(String name, Studies typeStudy, int price, Color color) {
        super(name, typeStudy, price, IType.FLOR);
        this.color = color;
    }

    @Override
    public String toString() {
        return "FLOR: " + super.toString() + " - COLOR: " + color;
    }

    public Color getColor() {
        return color;
    }
}
