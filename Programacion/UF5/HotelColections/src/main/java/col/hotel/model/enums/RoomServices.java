package col.hotel.model.enums;

import col.hotel.exceptions.HotelException;

public enum RoomServices {
    TV, BALCO, LLITDOBLE, JACUZZI, MINIBAR, TELEFON, SATELITE, SUITE;

    public static RoomServices getRoomServices(String service) throws HotelException {
        try {
            return RoomServices.valueOf(service.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new HotelException(HotelException.WRONG_SERVICE);
        }
    }
}
