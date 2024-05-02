package col.hotel.model.enums;

import col.hotel.exceptions.HotelException;

public enum RoomStatus {
    CLEAN, UNCLEAN, BROKEN, RESERVED;

    public static RoomStatus getrRoomStatus(String status) throws HotelException {
        try {
            return RoomStatus.valueOf(status.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new HotelException(HotelException.WRONG_STATUS);
        }
    }
}
