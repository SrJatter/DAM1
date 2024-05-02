package org.example;

public class Coche {
    private String matricula;
    private String marca;
    private int velocidad;

    private boolean embrage;

    public Coche(String matricula, String modelo) {
        this.matricula = matricula;
        this.marca = modelo;
        velocidad = 0;
    }

    public Coche(String matricula) {
        this.matricula = matricula;
        marca = "Seat";
        velocidad = 0;
    }

    public void acelerar() {
        velocidad++;
    }

    public void frenar() {
        if (velocidad > 0) {
            velocidad--;
        }
    }

    public String getMatricula() {
        return matricula;
    }

    public String getMarca() {
        return marca;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public boolean isEmbrage() {
        return embrage;
    }
}