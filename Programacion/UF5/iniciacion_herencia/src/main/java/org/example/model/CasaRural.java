package org.example.model;

public class CasaRural extends Casa{
    private int distance;
    private int altitude;

    public CasaRural(int id, int area, String direction, String city, float precio_venta, int bathrooms, int floors, int distance, int altitude) {
        super(id, area, direction, city, precio_venta, bathrooms, floors);
        this.distance = distance;
        this.altitude = altitude;
    }
}
