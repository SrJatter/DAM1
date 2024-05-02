package com.veterinario.exceptions;

import java.util.Arrays;
import java.util.List;

public class VetException extends Exception {
    private static final String ANSI_RED = "\033[31m";
    private static final String ANSI_RESET = "\033[0m";
    public static final int WRONG_OPERATION = 0;
    public static final int WRONG_NUM_ARGS = 1;
    public static final int PET_ALREADY_EXISTS = 2;
    public static final int PET_NOT_EXISTS = 3;
    public static final int WRONG_NUM_FORMAT = 4;
    public static final int NUM_OUT_OF_RANGE = 5;
    public static final int WRONG_GENDER = 6;
    public static final int WRONG_SIZE = 7;
    public static final int WRONG_SPECIALITY = 8;
    public static final int WRONG_SPECIMEN = 9;
    public static final int WRONG_LENGTH = 10;
    public static final int WRONG_YES_NO = 11;
    public static final int WRONG_TREATMENT = 12;
    public static final int NO_WORKER = 13;
    public static final int NOT_IMPLEMENTED = 14;


    private final List<String> messages = Arrays.asList(
            "ERROR: Operació incorrecte",
            "ERROR: Numero d'arguments incorrecte",
            "ERROR: Ja existeix una mascota amb aquest nom",
            "ERROR: No existeix cap mascota amb aquest nom",
            "ERROR: Error s'ha d'introduir un numero",
            "ERROR: Numero fora del rang",
            "ERROR: Genere incorrecte ha de ser F o M",
            "ERROR: Grandària incorrecte ha de ser Gran, Mitja o Petit",
            "ERROR: Especialitat incorrecte",
            "ERROR: Especie incorrecte",
            "ERROR: Llarg del pel incorrecte",
            "ERROR: Si o No",
            "ERROR: No existeix el tractament",
            "ERROR: No hi ha treballadors per fer el tractament",
            "ERROR: No se ha implementado"
    );

    public final int code;

    public VetException(int code){
        this.code = code;
    }

    @Override
    public String getMessage(){
        return ANSI_RED + messages.get(code) + ANSI_RESET;
    }

}
