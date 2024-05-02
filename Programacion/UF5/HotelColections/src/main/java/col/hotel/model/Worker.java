package col.hotel.model;

import col.hotel.model.enums.WorkerSkills;

import java.util.HashSet;
import java.util.Set;

public class Worker {
    private int dni;
    private String name;
    private HashSet<WorkerSkills> skills;

    public Worker(int dni, String name, HashSet<WorkerSkills> skills) {
        this.dni = dni;
        this.name = name;
        this.skills = skills;
    }

    public int getDni() {
        return dni;
    }

    public String getName() {
        return name;
    }

    public HashSet<WorkerSkills> getSkills() {
        return skills;
    }
}
