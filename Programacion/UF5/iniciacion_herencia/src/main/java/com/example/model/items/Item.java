package com.example.model.items;

import com.example.model.enums.IType;
import com.example.model.enums.Studies;

public class Item {
    private String name;
    private Studies study;
    protected int price;
    private IType type;

    public Item(String name, Studies study, int price, IType type) {
        this.name = name;
        this.study = study;
        this.price = price;
        this.type = type;
    }

    @Override
    public String toString() {
        return name + " - " + study + " - Preu: " + price;
    }

    public String getName() {
        return name;
    }

    public Studies getStudy() {
        return study;
    }
    public int getPrice() {
        return price;
    }

    public IType getType() {
        return type;
    }
}
