package com.example.model.enums;

import com.example.exceptions.CrossingException;

public enum IType {
    EINA,FLOR, MOBLE;

    public static IType getOType(String iTypeName, boolean switchErr) throws CrossingException {
        switch (iTypeName.toUpperCase()) {
            case "EINA":
                return IType.EINA;
            case "FLOR":
                return IType.FLOR;
            case "MOBLE":
                return IType.MOBLE;
            default:
                if (switchErr) {
                    throw new CrossingException(CrossingException.WRONG_PREFERENCE);

                } else {
                    throw new CrossingException(CrossingException.WRONG_TYPE);
                }
        }
    }
}
