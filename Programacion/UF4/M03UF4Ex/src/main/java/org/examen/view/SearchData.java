package org.examen.view;

import org.examen.model.Plat;

import java.util.ArrayList;

public class SearchData {

    public float priceMedia(ArrayList<Plat> plats) {
        float total = 0;
        for (Plat plat : plats) {
            total += plat.getPrice();
        }
        return total/plats.size();
    }
    public int stockPlats(ArrayList<Plat> plats) {
        int total = 0;
        for (Plat plat : plats) {
            total += plat.getCookedPlat();
        }
        return total;
    }
    public int boughtPlats(ArrayList<Plat> plats) {
        int total = 0;
        for (Plat plat : plats) {
            total += plat.getBoughtQty();
        }
        return total;
    }
    public Plat searchFavPlat(ArrayList<Plat> plats) {
        Plat maxP = null;
        int max = 0;
        for (Plat plat : plats) {
            if (max < plat.getBoughtQty()) {
                max = plat.getBoughtQty();
                maxP = plat;
            }
        }
        return maxP;
    }
    public Plat searchPlat(ArrayList<Plat> plats, String nom) {
        for (Plat plat : plats) {
            if (plat.getName().equals(nom)){
                return plat;
            }
        }
        return null;
    }
    public ArrayList<String> showPlatsByCategory(ArrayList<Plat> plats, String cat) {
        ArrayList<String> names = new ArrayList<>();
        for (Plat plat : plats) {
            if (plat.getCategory().equals(cat)) {
                System.out.println(plat.getName() + " - Preu: " + plat.getPrice() +" - Quantitat disponible: " + plat.getCookedPlat());
                names.add(plat.getName());
            }
        }
        return names;
    }
    public ArrayList<String> showPlatsByCategory2(ArrayList<Plat> plats, String cat) {
        ArrayList<String> names = new ArrayList<>();
        for (Plat plat : plats) {
            if (plat.getCategory().equals(cat)) {
                System.out.println(plat.getName() + " - Preu: " + plat.getPrice() +"€ - Quantitat actual: " + plat.getCookedPlat() + " - Venuts: " + plat.getBoughtQty());
                names.add(plat.getName());
            }
        }
        return names;
    }
}
