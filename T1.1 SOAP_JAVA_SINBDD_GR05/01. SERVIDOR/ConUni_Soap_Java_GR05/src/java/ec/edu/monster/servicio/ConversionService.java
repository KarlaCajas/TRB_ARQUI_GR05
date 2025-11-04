/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.monster.servicio;

/**
 *
 * @author karly
 */

public class ConversionService {

    // ==========================
    // 🌡️ CONVERSIONES DE TEMPERATURA
    // ==========================
    public double celsiusAFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    public double fahrenheitACelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public double celsiusAKelvin(double celsius) {
        return celsius + 273.15;
    }

    // ==========================
    // ⚖️ CONVERSIONES DE MASA
    // ==========================
    public double kilogramosAGramos(double kilogramos) {
        return kilogramos * 1000;
    }

    public double gramosAMiligramos(double gramos) {
        return gramos * 1000;
    }

    public double toneladasAKilogramos(double toneladas) {
        return toneladas * 1000;
    }

    // ==========================
    // 📏 CONVERSIONES DE LONGITUD
    // ==========================
    public double kilometrosAMetros(double kilometros) {
        return kilometros * 1000;
    }

    public double metrosACentimetros(double metros) {
        return metros * 100;
    }

    public double centimetrosAMilimetros(double centimetros) {
        return centimetros * 10;
    }
}
