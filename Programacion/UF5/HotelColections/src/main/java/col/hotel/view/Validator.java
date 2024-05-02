package col.hotel.view;

import col.hotel.controller.Hotel;
import col.hotel.exceptions.HotelException;
import col.hotel.model.Room;

import java.util.Map;

public class Validator {
    private Hotel hotel = Hotel.getInstance();
    private Map<String, Room> rooms;
    public void checkRoomNotExist(String code) throws HotelException {
        rooms = hotel.getRooms();
        if (rooms.containsKey(code)) {
            throw new HotelException(HotelException.ROOM_ALREADY_EXISTS);
        }
    }
    public void checkRoomExist(String code) throws HotelException {
        rooms = hotel.getRooms();
        if (!rooms.containsKey(code)) {
            throw new HotelException(HotelException.ROOM_DOES_NOT_EXIST);
        }
    }
}
