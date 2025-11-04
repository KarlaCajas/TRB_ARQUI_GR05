/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/WebServices/WebService.java to edit this template
 */
package ec.edu.monster.controlador;

import jakarta.jws.WebService;  
import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import ec.edu.monster.servicio.ConversionService;
import ec.edu.monster.servicio.LoginService;


/**
 *
 * @author karly
 */
@WebService(serviceName = "CONUNI")
public class CONUNI {

    // ==========================
    // 🌡️ CONVERSIONES DE TEMPERATURA
    // ==========================

    @WebMethod(operationName = "celsiusAFahrenheit")
    public double celsiusAFahrenheit(@WebParam(name = "celsius") double celsius) {
        ConversionService service = new ConversionService();
        return service.celsiusAFahrenheit(celsius);
    }

    @WebMethod(operationName = "fahrenheitACelsius")
    public double fahrenheitACelsius(@WebParam(name = "fahrenheit") double fahrenheit) {
        ConversionService service = new ConversionService();
        return service.fahrenheitACelsius(fahrenheit);
    }

    @WebMethod(operationName = "celsiusAKelvin")
    public double celsiusAKelvin(@WebParam(name = "celsius") double celsius) {
        ConversionService service = new ConversionService();
        return service.celsiusAKelvin(celsius);
    }

    // ==========================
    // ⚖️ CONVERSIONES DE MASA
    // ==========================

    @WebMethod(operationName = "kilogramosAGramos")
    public double kilogramosAGramos(@WebParam(name = "kilogramos") double kilogramos) {
        ConversionService service = new ConversionService();
        return service.kilogramosAGramos(kilogramos);
    }

    @WebMethod(operationName = "gramosAMiligramos")
    public double gramosAMiligramos(@WebParam(name = "gramos") double gramos) {
        ConversionService service = new ConversionService();
        return service.gramosAMiligramos(gramos);
    }

    @WebMethod(operationName = "toneladasAKilogramos")
    public double toneladasAKilogramos(@WebParam(name = "toneladas") double toneladas) {
        ConversionService service = new ConversionService();
        return service.toneladasAKilogramos(toneladas);
    }

    // ==========================
    // 📏 CONVERSIONES DE LONGITUD
    // ==========================

    @WebMethod(operationName = "kilometrosAMetros")
    public double kilometrosAMetros(@WebParam(name = "kilometros") double kilometros) {
        ConversionService service = new ConversionService();
        return service.kilometrosAMetros(kilometros);
    }

    @WebMethod(operationName = "metrosACentimetros")
    public double metrosACentimetros(@WebParam(name = "metros") double metros) {
        ConversionService service = new ConversionService();
        return service.metrosACentimetros(metros);
    }

    @WebMethod(operationName = "centimetrosAMilimetros")
    public double centimetrosAMilimetros(@WebParam(name = "centimetros") double centimetros) {
        ConversionService service = new ConversionService();
        return service.centimetrosAMilimetros(centimetros);
    }
    
       @WebMethod(operationName = "login")
    public boolean login(@WebParam(name = "usuario") String usuario, @WebParam(name = "contraseña") String contraseña) {
        LoginService service = new LoginService();
        return service.autenticar(usuario,contraseña);
  }

    
}

