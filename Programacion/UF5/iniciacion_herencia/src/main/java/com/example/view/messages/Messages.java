package com.example.view.messages;

import java.util.Arrays;
import java.util.List;

public class Messages {
    public static final int PLAYER_REGISTERED = 0;
    public static final int NPC_REGISTERED = 1;
    public static final int ITEM_CREATED = 2;
    public static final int SUCCESSFUL_PURCHASE = 3;
    public static final int SUCCESSFUL_MOVE = 4;
    public static final int RISE_FRIENDSHIP_POINTS = 5;
    public static final int RISE_FRIENDSHIP_POINTS_AND_LVL = 6;

    private final List<String> messages = Arrays.asList(
            "OK: Jugador registrat",
            "OK: Personatge registrat",
            "OK: Objecte registrat",
            "OK: Compra realizada",
            "OK: Moviment realitzat",
            "",
            "");

    public String getMessage(int code) {
        return messages.get(code);
    }
    public String getMessage(int code, String[] args) {
        switch (code) {
            case SUCCESSFUL_PURCHASE:
                return "OK: Compra realitzada. El jugador " + args[1] + " obté l’objecte " + args[2];
            case RISE_FRIENDSHIP_POINTS:
                return " OK: Amistat. Punts guanyats: " + args[1] + ". Punts de " + args[0] + ": " + args[2];
            case RISE_FRIENDSHIP_POINTS_AND_LVL:
                return " OK: Amistat. Punts guanyats: " + args[1] + ". " + args[0] + " puja de nivell. Nivell: " + args[3] + ". Punts: " + args[2] + ". Calacoins: " + args[4];
            default:
                return "";
        }
    }
}
