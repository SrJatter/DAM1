package com.example.model.character;

import com.example.model.enums.IType;
import com.example.model.enums.Place;
import com.example.model.enums.Studies;

public class NPC extends Character{
    private Studies study;
    private IType preference;

    public NPC(String name, Studies study, Place location, IType preference) {
        super(name, location);
        this.study = study;
        this.preference = preference;
    }
    @Override
    public String toString() {
        return super.toString() + " - Estudi: " + study + " - Preferència: " + preference;
    }

    public Studies getStudy() {
        return study;
    }

    public IType getPreference() {
        return preference;
    }
}
