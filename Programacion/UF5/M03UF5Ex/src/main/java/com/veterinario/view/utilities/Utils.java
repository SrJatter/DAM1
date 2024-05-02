package com.veterinario.view.utilities;

import com.veterinario.controller.Manager;
import com.veterinario.exceptions.VetException;
import com.veterinario.model.Pets.Pet;
import com.veterinario.model.Worker;
import com.veterinario.model.enums.Speciality;
import com.veterinario.model.enums.TreatmentEnum;
import com.veterinario.model.treatments.Treatment;

import java.util.HashMap;
import java.util.HashSet;

public class Utils {
    private Manager m = Manager.getInstance();
    public String capitalize(String str) {
        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }
    public Worker searchWorker(TreatmentEnum treatment) throws VetException {
        HashMap<String, Worker> workers = m.getWorkers();
        for (String key : workers.keySet()) {
            Worker worker = workers.get(key);
            if (treatment.equals(TreatmentEnum.PERRUQUERIA) && worker.getSpecialty().contains(Speciality.PERRUQUERIA)){
                return worker;
            } else if (treatment.equals(TreatmentEnum.VACUNA) && (worker.getSpecialty().contains(Speciality.INFERMERIA) || worker.getSpecialty().contains(Speciality.VETERINARIA))) {
                return worker;
            } else if (treatment.equals(TreatmentEnum.REVISIO) && worker.getSpecialty().contains(Speciality.VETERINARIA)) {
                return worker;
            } else if (treatment.equals(TreatmentEnum.CURA) && (worker.getSpecialty().contains(Speciality.INFERMERIA) || worker.getSpecialty().contains(Speciality.VETERINARIA))) {
                return worker;
            }
        }
        throw new VetException(VetException.NO_WORKER);
    }

    public String searchTreatments(String name) {
        String result = "";
        Pet pet = m.getPets().get(name);
        HashMap<Integer, Treatment> treatments = pet.getTreatments();
        for (Integer key : treatments.keySet()) {
            Treatment treatment = treatments.get(key);
            result += treatment.toString() + "\n";
        }
        return result;
    }
}
