package org.example4.model;

import java.util.ArrayList;

public class CoffeShop {
    private String name;
    private String ciudad;
    private ArrayList<CoffeMachine> coffeMachines;
    public CoffeShop(String name, String ciudad) {
        this.name = name;
        this.ciudad = ciudad;
        coffeMachines = new ArrayList<>();
    }
    @Override
    public String toString() {
        return "Nombre: " + name + " Ciudad: " + ciudad;
    }

    public void addCoffeMAchine(CoffeMachine c){
        coffeMachines.add(c);
    }
}