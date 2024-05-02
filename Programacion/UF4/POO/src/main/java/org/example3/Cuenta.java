package org.example3;

public class Cuenta {
    private String iban;
    private double saldo;
    private String titular;

    public Cuenta(String iban, double saldo, String titular) {
        this.iban = iban;
        this.saldo = saldo;
        this.titular = titular;
    }

    public void ingreso(double cantidad) {
        this.saldo += cantidad;
    }
    public void retiro(double cantidad) {
        this.saldo -= cantidad;
    }
    public String getIban() {
        return iban;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getTitular() {
        return titular;
    }
}
