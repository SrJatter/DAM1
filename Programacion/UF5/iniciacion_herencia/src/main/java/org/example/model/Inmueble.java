package org.example.model;

public class Inmueble {
    private int id;
    private int area;
    private String direction;
    private String city;
    private float precio_venta;

    public Inmueble(int id, int area, String direction, String city, float precio_venta) {
        this.id = id;
        this.area = area;
        this.direction = direction;
        this.city = city;
        this.precio_venta = precio_venta;
    }
}
