package org.solar.model;

public class Panel {
    private int surface;
    private float price;
    private int power;

    public Panel(int surface, float price, int power) {
        this.surface = surface;
        this.price = price;
        this.power = power;
    }
    public int getSurface() {
        return surface;
    }
    public float getPrice() {
        return price;
    }
    public int getPower() {
        return power;
    }
}
