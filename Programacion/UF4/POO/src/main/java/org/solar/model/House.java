package org.solar.model;

import java.util.ArrayList;

public class House {
    private String nif;
    private String name;
    private int surface;
    private boolean commute;
    private ArrayList<Panel> panels;
    private ArrayList<Device> devices;
    private static ArrayList<String> nifs = new ArrayList<>();

    public House(String nif, String name, int surface) {
        this.nif = nif;
        this.name = name;
        this.surface = surface;
        this.commute = true;
        panels = new ArrayList<>();
        devices = new ArrayList<>();
        nifs.add(nif);
    }
    public House(String nif, String name, int surface, boolean commute) {
        this.nif = nif;
        this.name = name;
        this.surface = surface;
        this.commute = commute;
        panels = new ArrayList<>();
        devices = new ArrayList<>();
        nifs.add(nif);
    }
    public void addPanel(Panel panel){
        panels.add(panel);
    }
    public void addDevice(Device device){
        devices.add(device);
    }
    public boolean deviceNameExists(String name) {
        for (Device device : devices) {
            if (device.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }
    public static boolean nifExists(String nif) {
        return nifs.contains(nif);
    }
    public String getNif() {
        return nif;
    }
    public String getName() {
        return name;
    }
    public ArrayList<Panel> getPanels() {
        return panels;
    }
    public ArrayList<Device> getDevices() {
        return devices;
    }
    public int getSurface() {
        return surface;
    }
    public boolean isCommute() {
        return commute;
    }
    public void setCommute(boolean commute) {
        this.commute = commute;
    }
}
