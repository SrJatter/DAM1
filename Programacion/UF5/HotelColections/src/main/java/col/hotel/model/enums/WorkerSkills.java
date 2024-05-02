package col.hotel.model.enums;

import col.hotel.exceptions.HotelException;

public enum WorkerSkills {
    MANTENIMENT, NETEJA, PISCINA, SPA, BAR, MENJAR, BUGADERIA;

    public static WorkerSkills getWorkerSkill(String skill) throws HotelException {
        try {
            return WorkerSkills.valueOf(skill.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new HotelException(HotelException.WRONG_SERVICE);
        }
    }
}
