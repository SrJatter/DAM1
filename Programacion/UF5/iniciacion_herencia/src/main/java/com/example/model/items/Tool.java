package com.example.model.items;

import com.example.model.enums.IType;
import com.example.model.enums.Studies;

public class Tool extends Item {
    private String desc;
    private int usages;

    public Tool(String name, Studies typeStudy, int price, String desc, int usages) {
        super(name, typeStudy, price, IType.EINA);
        this.desc = desc;
        this.usages = usages;
    }

    public void useTool() {
        this.usages -= 1;
        this.price -= 10;
    }

    @Override
    public String toString() {
        return "EINA: " + super.toString() +" - Descripció: " + desc + "Ús: " + usages;
    }

    public String getDesc() {
        return desc;
    }

    public int getUsages() {
        return usages;
    }
}
