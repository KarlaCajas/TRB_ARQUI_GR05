package ec.edu.monster.controlador;

import org.ksoap2.SoapEnvelope;
import org.ksoap2.serialization.SoapObject;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import org.ksoap2.transport.HttpTransportSE;

public class TransformacionController {
    private static final String NAMESPACE = "http://controlador.monster.edu.ec/";
    private static final String URL = "http://192.168.10.104:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl";

    public String convertirCelsiusAFahrenheit(double valor) {
        return llamarServicio("celsiusAFahrenheit", "celsius", valor);
    }

    public String convertirFahrenheitACelsius(double valor) {
        return llamarServicio("fahrenheitACelsius", "fahrenheit", valor);
    }

    public String convertirCelsiusAKelvin(double valor) {
        return llamarServicio("celsiusAKelvin", "celsius", valor);
    }

    public String convertirKilogramosAGramos(double valor) {
        return llamarServicio("kilogramosAGramos", "kilogramos", valor);
    }

    public String convertirGramosAMiligramos(double valor) {
        return llamarServicio("gramosAMiligramos", "gramos", valor);
    }

    public String convertirToneladasAKilogramos(double valor) {
        return llamarServicio("toneladasAKilogramos", "toneladas", valor);
    }

    public String convertirKilometrosAMetros(double valor) {
        return llamarServicio("kilometrosAMetros", "kilometros", valor);
    }

    public String convertirMetrosACentimetros(double valor) {
        return llamarServicio("metrosACentimetros", "metros", valor);
    }

    public String convertirCentimetrosAMilimetros(double valor) {
        return llamarServicio("centimetrosAMilimetros", "centimetros", valor);
    }

    public String llamarServicio(String metodo, String parametro, double valor) {
        try {
            SoapObject request = new SoapObject(NAMESPACE, metodo);
            request.addProperty(parametro, valor);

            SoapSerializationEnvelope envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
            envelope.setOutputSoapObject(request);
            envelope.dotNet = false;

            new MarshalDouble().register(envelope);

            HttpTransportSE transporte = new HttpTransportSE(URL);
            transporte.debug = true;
            transporte.call(NAMESPACE + metodo, envelope);

            String responseDump = transporte.responseDump;
            System.out.println("SOAP Response: " + responseDump);

            java.util.regex.Pattern pattern = java.util.regex.Pattern.compile("<return>(.*?)</return>");
            java.util.regex.Matcher matcher = pattern.matcher(responseDump);

            if (matcher.find()) {
                String valorRespuesta = matcher.group(1);
                String numeroStr = valorRespuesta.replaceAll("[^0-9.\\-]", "");
                try {
                    Double.parseDouble(numeroStr);
                    return numeroStr;
                } catch (NumberFormatException e) {
                    return "Error: Formato numerico invalido - " + valorRespuesta;
                }
            }

            return "Error: No se pudo extraer el valor numerico";

        } catch (Exception e) {
            e.printStackTrace();
            return "Error: " + e.getClass().getSimpleName() + " - " + e.getMessage();
        }
    }
}
