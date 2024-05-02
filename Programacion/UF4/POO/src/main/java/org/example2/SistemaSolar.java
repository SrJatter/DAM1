package org.example2;



public class SistemaSolar {
    public static void main(String[] args) {
        Planeta tierra = new Planeta(300, 220, 62, 7000, 1, "Tierra");
        Planeta marte = new Planeta(620, 480, 133, 10000, 2, "Marte");
        tierra.impacto(tierra.getMassa(), 40);
        System.out.println("Planeta: " + tierra.getNom());
        System.out.println("Massa: "+ tierra.getMassa());
        System.out.println("Densidad: "+ tierra.getDensitat());
        System.out.println("Diametro: "+ tierra.getDiametre());
        System.out.println("Distancia: "+ tierra.getDistancia());
        System.out.println("Id: "+ tierra.getId());
        System.out.println();
        marte.impacto(marte.getMassa(), 10000);
        System.out.println("Planeta: " + marte.getNom());
        System.out.println("Massa: "+ marte.getMassa());
        System.out.println("Densidad: "+ marte.getDensitat());
        System.out.println("Diametro: "+ marte.getDiametre());
        System.out.println("Distancia: "+ marte.getDistancia());
        System.out.println("Id: "+ marte.getId());
    }
}
