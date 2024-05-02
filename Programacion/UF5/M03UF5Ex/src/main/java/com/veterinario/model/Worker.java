package com.veterinario.model;

import com.veterinario.model.enums.Speciality;

import java.util.HashSet;

public class Worker {
    private String DNI;
    private String name;
    private String lastname;
    private int tel;
    private HashSet<Speciality> specialty;

    public Worker(String DNI, String name, String lastname, int tel, HashSet<Speciality> specialty) {
        this.DNI = DNI;
        this.name = name;
        this.lastname = lastname;
        this.tel = tel;
        this.specialty = specialty;
    }

    public String getDNI() {
        return DNI;
    }

    public String getName() {
        return name;
    }

    public String getLastname() {
        return lastname;
    }

    public HashSet<Speciality> getSpecialty() {
        return specialty;
    }

    public int getTel() {
        return tel;
    }
}
