package col.hotel.exceptions;

import java.util.Arrays;
import java.util.List;

public class HotelException extends Exception {
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_RESET = "\u001B[0m";
    public static final int WRONG_OPERATION = 0;
    public static final int WRONG_STATUS = 1;
    public static final int WRONG_SERVICE = 2;
    public static final int ROOM_ALREADY_EXISTS = 3;
    public static final int ROOM_DOES_NOT_EXIST = 4;

    private final List<String> messages = Arrays.asList(
            "[ Wrong operation ]",
            "[ Wrong status ]",
            "[ Wrong service ]",
            "[ Room already exists ]",
            "[ Room doesn't exists ]"

    );
    private final int code;

    public HotelException(int code) {
        this.code = code;
    }

    @Override
    public String getMessage() {
        return ANSI_RED + messages.get(code) + ANSI_RESET;
    }
}
