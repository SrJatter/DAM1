package com.example.exceptions;

import java.util.Arrays;
import java.util.List;

public class CrossingException extends Exception{
    public static final int WRONG_OPERATION = 0;
    public static final int WRONG_ARGUMENTS = 1;
    public static final int PLAYER_ALREADY_EXISTS = 2;
    public static final int NPC_ALREADY_EXISTS = 3;
    public static final int WRONG_STUDY = 4;
    public static final int WRONG_LOCATION = 5;
    public static final int WRONG_PREFERENCE = 6;
    public static final int ITEM_ALREADY_EXISTS = 7;
    public static final int WRONG_TYPE = 8;
    public static final int WRONG_DATA = 9;
    public static final int PRICE_OUT_OF_RANGE = 10;
    public static final int WRONG_COLOR = 11;
    public static final int USAGE_OUT_OF_RANGE = 12;
    public static final int PLAYER_NOT_FOUND = 13;
    public static final int ITEM_NOT_FOUND = 14;
    public static final int PLAYER_ALREADY_HAS_ITEM = 15;
    public static final int INSUFFICIENT_CALACOINS = 16;
    public static final int PLAYER_NOT_AT_BAR = 17;
    public static final int NO_ONE_FOUND = 18;
    public static final int PLAYER_AND_NPC_NOT_AT_SAME_PLACE = 19;
    public static final int PLAYER_DOES_NOT_HAVE_ITEM = 20;
    public static final int PERSON_ALREADY_AT_LOCATION = 21;
    public static final int WRONG_PERSON_TYPE = 22;
    public static final int NO_ONES_REGISTERED = 23;
    public static final int NO_ONES_THERE = 24;

    private final List<String> messages = Arrays.asList(
            "ERROR 001: Operació incorrecta",
            "ERROR 002: Núm. d'arguments incorrecte",
            "ERROR 003: Ja existeix un jugador amb aquest nom",
            "ERROR 004: Ja existeix un personatge amb aquest nom",
            "ERROR 005: Estudi incorrecte",
            "ERROR 006: Lloc incorrecte",
            "ERROR 007: Preferència incorrecta",
            "ERROR 008: Ja existeix un objecte amb aquest nom",
            "ERROR 009: Tipus incorrecte",
            "ERROR 010: Dada incorrecta",
            "ERROR 011: Preu fora de rang",
            "ERROR 012: Color incorrecte",
            "ERROR 013: Ús fora de rang",
            "ERROR 014: No existeix un jugador amb aquest nom",
            "ERROR 015: No existeix un objecte amb aquest nom",
            "ERROR 016: El jugador ja té l'objecte",
            "ERROR 017: El jugador no té suficients calacoins per a la compra",
            "ERROR 018: El jugador no està al BAR",
            "ERROR 019: No existeix ningú amb aquest nom",
            "ERROR 020: El jugador i el personatge no estan al mateix lloc",
            "ERROR 021: El jugador no té l'objecte",
            "ERROR 022: Aquesta persona ja es troba en aquest lloc",
            "ERROR 023: Tipus de persona incorrecte",
            "ERROR 024: No hi ha ningú registrat",
            "ERROR 025: No hi ha ningú aquí"
    );
    private final int code;

    public CrossingException(int code) {
        this.code = code;
    }

    @Override
    public String getMessage() {
        return messages.get(code);
    }

}
