package org.example.model;

public class Casa extends Vivienda{
    private int floors;

    public Casa(int id, int area, String direction, String city, float precio_venta, int rooms, int bathrooms, int floors) {
        super(id, area, direction, city, precio_venta, rooms, bathrooms);
        this.floors = floors;
    }
    public Casa(int id, int area, String direction, String city, float precio_venta, int bathrooms, int floors) {
        super(id, area, direction, city, precio_venta, bathrooms);
        this.floors = floors;
    }
}
