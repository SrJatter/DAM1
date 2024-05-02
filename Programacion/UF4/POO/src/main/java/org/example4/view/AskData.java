package org.example4.view;

import javax.management.StringValueExp;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;

public class AskData {
    private BufferedReader br;
    public AskData() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    public int askInt(String message) {
        System.out.println(message);
        int number = 0;
        boolean error = true;
        while (error) {
            try {
                number = Integer.parseInt(br.readLine().trim());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            } catch (NumberFormatException ex) {
                System.out.println("Debes introducir un número entero");
            }
        }
        return number;
    }
    public int askInt(String message, String messageError, int min) {
        int number = 0;
        do {
            number = askInt(message);
            if (min > number) {
                System.out.println(messageError);
            }
        } while (min > number);
        return number;
    }
    public int askInt(String message, String messageError, int min, int max) {
        int number = 0;
        do {
            number = askInt(message);
            if (min > number || number > max) {
                System.out.println(messageError);
            }
        } while (min > number || number > max);
        return number;
    }
    public String askStr(String message) {
        System.out.println(message);
        String str = null;
        boolean error = true;
        while (error) {
            try {
                str = br.readLine().trim();
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            }
        }
        return str;
    }
    public String askStr(String message, boolean chk) {
        String str;
        do {
            str = askStr(message);
            if (str.isEmpty()) {
                System.out.println("No se puede dejar vacio");
            }
        } while (str.isEmpty());
        return str;
    }
}

