package com.example.model.enums;

import com.example.exceptions.CrossingException;

public enum Color {
    VIOLETA, ROSA, TURQUESA;
    public static Color getColor(String colorName) throws CrossingException {
        switch (colorName.toUpperCase()) {
            case "VIOLETA":
                return Color.VIOLETA;
            case "ROSA":
                return Color.ROSA;
            case "TURQUESA":
                return Color.TURQUESA;
            default:
                throw new CrossingException(CrossingException.WRONG_COLOR);
        }
    }
}
