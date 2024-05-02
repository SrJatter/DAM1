package org.solar.model;

import java.util.ArrayList;

public class Device {
    private String name;
    private int power;
    private boolean commute;

    public Device(String name, int power) {
        this.name = name;
        this.power = power;
        this.commute = false;
    }
    public Device(String name, int power, boolean commute) {
        this.name = name;
        this.power = power;
        this.commute = commute;
    }
    public String getName() {
        return name;
    }
    public int getPower() {
        return power;
    }
    public boolean isCommute() {
        return commute;
    }
    public void setCommute(boolean commute) {
        this.commute = commute;
    }
}
