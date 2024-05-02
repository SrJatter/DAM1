package org.examen.view;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class InputData {
    private BufferedReader br;

    public InputData() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public int askInt(String message) {
        int number = 0;
        boolean error = true;
        while (error) {
            System.out.println(message);
            try {
                number = Integer.parseInt(br.readLine().trim());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            } catch (NumberFormatException ex) {
                System.out.println("Has d'introduir un nombre sencer.");
            }
        }
        return number;
    }
    public int askInt(String message, String messageError, int min) {
        int number;
        do {
            number = askInt(message);
            if (min > number) {
                System.out.println(messageError);
            }
        } while (min > number);
        return number;
    }

    public String askStr(String message) {
        String str = null;
        boolean error = true;
        while (error) {
            try {
                do {
                    System.out.println(message);
                    str = br.readLine().trim();
                    if (str.isEmpty()) {
                        System.out.println("No es pot deixar buit.");
                    }
                } while (str.isEmpty());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            }
        }
        return str;
    }

    public String askStr(String message, String messageError, String arraytxt) {
        String str = null;
        String[] sizes = arraytxt.split(" ");
        boolean error = true;
        while (error) {
            str = askStr(message).toLowerCase().trim();
            for (String s : sizes) {
                if (s.toLowerCase().equals(str)) {
                    error = false;
                }
            }
            if (error) {
                System.out.println(messageError);
            }
        }
        return str;
    }

    public void askNothing() {
        try {
            br.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public float askFloat(String message) {
        float number = 0;
        boolean error = true;
        while (error) {
            System.out.println(message);
            try {
                number = Float.parseFloat(br.readLine().trim());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            } catch (NumberFormatException ex) {
                System.out.println("Has d'introduir un nombre sencer o decimal.");
            }
        }
        return number;
    }

    public float askFloat(String message, String messageError, int min) {
        float number;
        do {
            number = askFloat(message);
            if (min > number) {
                System.out.println(messageError);
            }
        } while (min > number);
        return number;
    }
}
