package org.example.model;

public class Vivienda extends Inmueble{
    private int rooms;
    private int bathrooms;

    public Vivienda(int id, int area, String direction, String city, float precio_venta, int rooms, int bathrooms) {
        super(id, area, direction, city, precio_venta);
        this.rooms = rooms;
        this.bathrooms = bathrooms;
    }
    public Vivienda(int id, int area, String direction, String city, float precio_venta, int bathrooms) {
        super(id, area, direction, city, precio_venta);
        this.rooms = 1;
        this.bathrooms = bathrooms;
    }
}
