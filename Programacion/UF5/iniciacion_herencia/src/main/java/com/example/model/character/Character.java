package com.example.model.character;

import com.example.model.enums.Place;

public class Character {
    private String name;
    private Place location;

    public Character(String name, Place location) {
        this.name = name;
        this.location = location;
    }

    @Override
    public String toString() {
        return name + " - " + location;
    }

    public void setLocation(Place location) {
        this.location = location;
    }

    public String getName() {
        return name;
    }

    public Place getLocation() {
        return location;
    }
}
