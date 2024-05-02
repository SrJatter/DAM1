package org.example2;

import java.security.PrivateKey;

public class Planeta {
    private int massa;
    private int densitat;
    private int diametre;
    private int distancia;
    private int id;
    private String nom;

    public Planeta(int massa, int densitat, int diametre, int distancia, int id, String nom) {
        this.massa = massa;
        this.densitat = densitat;
        this.diametre = diametre;
        this.distancia = distancia;
        this.id = id;
        this.nom = nom;
    }

    public void impacto(int massa, int meteorito) {
        if (massa <= meteorito){
            this.massa = 0;
            this.densitat = 0;
            this.diametre = 0;
        } else if (massa / 2 < meteorito){
            this.massa -= meteorito;
            this.densitat -= (int) (meteorito * 0.5);
            this.diametre -= (int) (meteorito * 0.03);
        } else if (massa / 2 > meteorito) {
            this.massa += meteorito;
            this.densitat += (int) (meteorito * 0.5);
            this.diametre += (int) (meteorito * 0.03);
        }
    }

    public void setDensitat(int densitat) {
        this.densitat = densitat;
    }

    public int getMassa() {
        return massa;
    }

    public int getDensitat() {
        return densitat;
    }

    public int getDiametre() {
        return diametre;
    }

    public int getDistancia() {
        return distancia;
    }

    public int getId() {
        return id;
    }

    public String getNom() {
        return nom;
    }
}
