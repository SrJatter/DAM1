package org.solar.view;

import org.solar.model.Device;
import org.solar.model.House;
import org.solar.model.Panel;

import java.util.ArrayList;

public class Utilities {
    private Integer numberI;
    private Float numberF;

    public boolean overPowered(House house) {
        int power = totalPower(house);
        int consum = actualConsum(house);
        if (power < consum) {
            house.setCommute(false);
            for (Device device : house.getDevices()) {
                device.setCommute(false);
            }
            System.out.println("Error: Han saltado los plomos. La casa queda completamente apagada.");
            return true;
        }
        return false;
    }
    public int actualConsum(House house) {
        int consum = 0;
        for (Device device : house.getDevices()) {
            if (device.isCommute()) {
                consum += device.getPower();
            }
        }
        return consum;
    }
    public int totalPower(House house){
        int power = 0;
        for (Panel panel : house.getPanels()) {
            power += panel.getPower();
        }
        return power;
    }
    public void showDevicesName(House house) {
        for (Device device : house.getDevices()) {
            if (device.isCommute()) {
                System.out.println("\t- " + device.getName());
            }
        }
    }
    public float totalInversion(House house){
        float inversion = 0;
        for (Panel panel : house.getPanels()) {
            inversion += panel.getPrice();
        }
        return inversion;
    }
    public boolean checkCommuteInFile(String comm) {
        return comm.equals("On");
    }
    public String commuteCheckHouse(House house) {
        if (house.isCommute()) {
            return "On";
        } else {
            return "Off";
        }
    }
    public String commuteCheckDevice(Device device) {
        if (device.isCommute()) {
            return "On";
        } else {
            return "Off";
        }
    }
    public String commutedHouse(House house) {
        if (house.isCommute()) {
            return "encendido";
        } else {
            return "apagado";
        }
    }
    public int avalibleHouseSurface(House house) {
        int avalible = house.getSurface();
        for (Panel panel : house.getPanels()){
            avalible -= panel.getSurface();
        }
        return avalible;
    }
    public Device searchDeviceByName(House house, String name){
        for (Device device : house.getDevices()) {
            if (device.getName().equals(name)) {
                return device;
            }
        }
        return null;
    }
    public boolean isHouseSurfaceFull(House house) {
        int avalible = house.getSurface();
        for (Panel panel : house.getPanels()){
            avalible -= panel.getSurface();
        }
        if (avalible == 0) {
            System.out.println("Error: No hay espacio disponible para instalar la placa.");
            return true;
        }
        return false;
    }
    public boolean checkTotalPanelSurface(House house, int newSurf){
        int panelsSurface = newSurf;
        for (Panel panel: house.getPanels()){
            panelsSurface += panel.getSurface();
        }
        if (house.getSurface() < panelsSurface){
            return false;
        } else {
            return true;
        }
    }
    public House searchHouseByNif(ArrayList<House> houses, String nif){
        for (House house : houses) {
            if (house.getNif().equals(nif)) {
                return house;
            }
        }
        return null;
    }
    public boolean checkHouseNotVoid(ArrayList<House> houses){
        return !houses.isEmpty();
    }
    public boolean checkCommand(String[] co, int num) {
        if (co.length != num) {
            System.out.println("Error: Número de parámetros incorrectos.");
            return false;
        }
        return true;
    }
    public boolean checkCommand(String[] co, int num, String uso) {
        if (co.length != num) {
            System.out.println("Error: Número de parámetros incorrectos.");
            System.out.println(uso);
            return false;
        }
        return true;
    }
    public Integer checkInt(String num, String formatError) {
        try {
            numberI = Integer.parseInt(num);
        } catch (NumberFormatException ex) {
            System.out.println(formatError);
            return null;
        }
        return numberI;
    }
    public Integer checkInt(String num, String formatError, String messageError, int min) {
        numberI = checkInt(num, formatError);
        if (numberI == null){
            return null;
        }
        if (min >= numberI) {
            System.out.println(messageError);
            return null;
        }
        return numberI;
    }
    public Float checkFloat(String num, String formatError) {
        try {
            numberF = Float.parseFloat(num);
        } catch (NumberFormatException ex) {
            System.out.println(formatError);
            return null;
        }
        return numberF;
    }
    public Float checkFloat(String num, String formatError, String messageError, int min) {
        numberF = checkFloat(num, formatError);
        if (numberF == null){
            return null;
        }
        if (min >= numberF) {
            System.out.println(messageError);
            return null;
        }
        return numberF;
    }
}
