package com.example.model.enums;

import com.example.exceptions.CrossingException;

public enum Place{
    SECRETARIA, BIBLIOTECA, BAR, AULA100, AULA200, AULA300, AULA400, TERRAZA;
    public static Place getPlace(String placeName) throws CrossingException {
        switch (placeName.toUpperCase()) {
            case "SECRETARIA":
                return Place.SECRETARIA;
            case "BIBLIOTECA":
                return Place.BIBLIOTECA;
            case "BAR":
                return Place.BAR;
            case "AULA100":
                return Place.AULA100;
            case "AULA200":
                return Place.AULA200;
            case "AULA300":
                return Place.AULA300;
            case "AULA400":
                return Place.AULA400;
            case "TERRAZA":
                return Place.TERRAZA;
            default:
                throw new CrossingException(CrossingException.WRONG_LOCATION);
        }
    }
}
