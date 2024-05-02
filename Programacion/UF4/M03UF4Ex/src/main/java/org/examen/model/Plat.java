package org.examen.model;

import java.util.ArrayList;

public class Plat {
    private String name;
    private String category;
    private float price;
    private int cookedPlat;
    private int boughtQty;
    private static ArrayList<String> names = new ArrayList<>();

    public Plat(String name, String category, float price) {
        this.name = name;
        this.category = category;
        this.price = price;
        this.cookedPlat = 0;
        this.boughtQty = 0;
        names.add(name);
    }
    public static boolean nameExists(String name) {
        return names.contains(name);
    }
    public void setCookedPlat(int cookedPlat) {
        this.cookedPlat += cookedPlat;
    }
    public void setBoughtQty(int boughtQty) {
        this.boughtQty += boughtQty;
    }
    public String getName() {
        return name;
    }
    public float getPrice() {
        return price;
    }
    public String getCategory() {
        return category;
    }
    public int getCookedPlat() {
        return cookedPlat;
    }
    public int getBoughtQty() {
        return boughtQty;
    }
}
