package com.veterinario.view.messages;

import java.util.Arrays;
import java.util.List;

public class Message {
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_RESET = "\u001B[0m";
    public static final int ADDED_PET = 0;
    public static final int ADDED_TREATMENT = 1;


    public final List<String> messages = Arrays.asList(
            "OK: Mascota registrada",
            "OK: Tractament registrat. Codi: ",
            "Mensaje 3",
            "Mensaje 4"
    );

    public String getMessage(int code) {
        return ANSI_BLUE + messages.get(code) + ANSI_RESET;
    }

    public String getMessage(int code, String[] args){
        switch (code) {
            case ADDED_TREATMENT:
                return ANSI_BLUE + getMessage(ADDED_TREATMENT) + args[0] + ANSI_RESET;
            default:
                return "";
        }
    }

}
