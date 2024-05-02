package org.examen.view;

import org.examen.model.Plat;

import java.util.ArrayList;

public class Options {
    private ArrayList<Plat> plats;
    private Plat plat;
    private InputData input = new InputData();
    private SearchData sd = new SearchData();
    private String name;
    private String cat;
    private int qty;
    public Options(){
        plats = new ArrayList<>();
    }
    public void addPlat(){
        int first = 0;
        do {
            if (first != 0) {
                System.out.println("Aquest plat ja esta registrat.");
            }
            name = input.askStr("Nom del plat:").toLowerCase();
            first = 1;
        } while (Plat.nameExists(name));
        float price = input.askFloat("Introdueix el preu:", "El preu ha de ser mes gran de 3€.", 3);
        cat = input.askStr("Introdueix el tipus de plat, Entrant, Principal, Postre:","Tipus invàlid.", "entrant principal postre");
        plats.add(new Plat(name, cat, price));
        System.out.println("Plat registrat correctament.");
        System.out.println("Prem enter per continuar:");
        input.askNothing();
    }
    public void cookPlat(){
        if (!plats.isEmpty()) {
            int first = 0;
            do {
                if (first != 0) {
                    System.out.println("Aquest plat no esta registrat.");
                }
                name = input.askStr("Nom del plat:").toLowerCase();
                first = 1;
            } while (!Plat.nameExists(name));
            qty = input.askInt("Quantitat cuinada:", "La quantitat ha de ser almenys 1.", 1);
            plat = sd.searchPlat(plats, name);
            plat.setCookedPlat(qty);
            System.out.println("Racions incorporades al sistema.");
            System.out.println("Total de racions disponibles del plat: " + plat.getCookedPlat());
        } else {
            System.out.println("No hi han plats registrats.");
        }
        System.out.println("Prem enter per continuar:");
        input.askNothing();
    }
    public void sellPlat(){
        if (!plats.isEmpty()) {
            cat = input.askStr("Introdueix el tipus de plat, Entrant, Principal, Postre:", "Tipus invàlid.", "entrant principal postre");
            ArrayList<String> names = sd.showPlatsByCategory(plats, cat);
            if (!names.isEmpty()) {
                int first = 0;
                do {
                    if (first != 0) {
                        System.out.println("Has de introduir un plat de la lista.");
                    }
                    name = input.askStr("Quin plat vols comprar?").toLowerCase();
                    first = 1;
                } while (!names.contains(name));
                plat = sd.searchPlat(plats, name);
                qty = input.askInt("Quantes racions vols?", "La quantitat ha de ser almenys 1.", 1);
                if (!(plat.getCookedPlat() - qty < 0)) {
                    plat.setCookedPlat(-qty);
                    plat.setBoughtQty(qty);
                    System.out.println("Comanda realitzada. Preu total: " + plat.getPrice() * qty);
                } else {
                    System.out.println("No n'hi han plats suficients, la quantitat actual es: " + plat.getCookedPlat());
                }
            } else {
                System.out.println("No hi han plats registrats d'aquest tipus");
            }
        } else {
            System.out.println("No hi han plats registrats.");
        }
        System.out.println("Prem enter per continuar:");
        input.askNothing();
    }
    public void favPlat(){
        if (!plats.isEmpty()) {
            plat = sd.searchFavPlat(plats);
            if (plat != null) {
                System.out.println("* El plat favorit dels nostres clients és: *");
                System.out.println("Nom del plat: " + plat.getName());
                System.out.println("Tipus de plat: " + plat.getCategory());
                System.out.println("Preu del plat: " + plat.getPrice());
                System.out.println("S'han venut un total de " + plat.getBoughtQty() + " racions.");
            } else {
                System.out.println("No ni ha plat favorit (Encara no sa venut res).");
            }
            System.out.println("Prem enter per continuar:");
            input.askNothing();
        } else {
            System.out.println("No hi han plats registrats.");
        }
    }
    public void showCarta(){
        System.out.println("***** Carta de Plats *****");
        System.out.println("ENTRANTS:");
        if (sd.showPlatsByCategory2(plats, "entrant").isEmpty()) {
            System.out.println("No hi ha plats ENTRANT registrats actualment.");
        }
        System.out.println("---------------------");
        System.out.println("PRINCIPALS:");
        if (sd.showPlatsByCategory2(plats, "principal").isEmpty()) {
            System.out.println("No hi ha plats PRINCIPAL registrats actualment.");
        }
        System.out.println("---------------------");
        System.out.println("POSTRES:");
        if (sd.showPlatsByCategory2(plats, "postre").isEmpty()) {
            System.out.println("No hi ha plats POSTRE registrats actualment.");
        }
        System.out.println("Prem enter per continuar:");
        input.askNothing();
    }
    public void stats(){
        if (!plats.isEmpty()) {
            System.out.println("* --- Estadístiques --- *");
            System.out.println("Plats registrats: " + plats.size());
            System.out.println("Preu mig: " + sd.priceMedia(plats));
            int stock = sd.stockPlats(plats);
            if (stock != 0) {
                System.out.println("Plats en estoc actualment: " + stock);
            } else{
                System.out.println("No n'hi han plats en estoc.");
            }
            int bought = sd.boughtPlats(plats);
            if (bought != 0) {
                System.out.println("Plats venuts fins ara: " + bought);
            } else {
                System.out.println("No s'han venut plats.");
            }
        } else {
            System.out.println("No hi han plats registrats.");
        }
        System.out.println("Prem enter per continuar:");
        input.askNothing();
    }
}
