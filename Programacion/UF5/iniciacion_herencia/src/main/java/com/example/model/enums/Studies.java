package com.example.model.enums;

import com.example.exceptions.CrossingException;

public enum Studies {
    BACHILLERATO, ESO, DAM, ASIC, SMX, COMERCIO, FINANCIAS, JARDINERIA, MANTENIMIENTO;
    public static Studies getStudies(String studiesName) throws CrossingException {
        switch (studiesName.toUpperCase()) {
            case "BACHILLERATO":
                return Studies.BACHILLERATO;
            case "ESO":
                return Studies.ESO;
            case "DAM":
                return Studies.DAM;
            case "ASIC":
                return Studies.ASIC;
            case "SMX":
                return Studies.SMX;
            case "COMERCIO":
                return Studies.COMERCIO;
            case "FINANCIAS":
                return Studies.FINANCIAS;
            case "JARDINERIA":
                return Studies.JARDINERIA;
            case "MANTENIMIENTO":
                return Studies.MANTENIMIENTO;
            default:
                throw new CrossingException(CrossingException.WRONG_STUDY);
        }
    }
}
