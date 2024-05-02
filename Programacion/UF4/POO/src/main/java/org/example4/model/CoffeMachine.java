package org.example4.model;
public class CoffeMachine {
    private int qty;
    private int maxCapacity;
    public CoffeMachine(int qty, int maxCapacity) {
        if (qty > maxCapacity) {
            qty = maxCapacity;
        }
        this.qty = qty;
        this.maxCapacity = maxCapacity;
    }
    public CoffeMachine(int maxCapacity) {
        this(maxCapacity, maxCapacity);
    }
    public CoffeMachine() {
        this(0, 1000);
    }
    public void omplirCafetera() {
        qty = maxCapacity;
    }
    public void servirTassa(int qty) {
        if (qty > this.qty) {
            this.qty = 0;
        } else {
            this.qty -= qty;
        }
    }
    public void buidarCafetera() {
        qty = 0;
    }
    public void afegirCafe(int qty) {
        if (this.qty + qty > maxCapacity) {
            this.qty = maxCapacity;
        } else {
            this.qty += qty;
        }
    }
    public int getQty() {
        return qty;
    }
    public int getMaxCapacity() {
        return maxCapacity;
    }
    @Override
    public String toString() {
        String cadena = "";
        cadena += "Máxima capacidad: " + maxCapacity + ". ";
        if (qty == 0) {
            cadena += "La cafetera está vacía";
        } else if (qty == maxCapacity) {
            cadena += "La cafetera está llena";
        } else {
            cadena += "Cantidad actual: " + qty;
        }
        return cadena;
    }
}