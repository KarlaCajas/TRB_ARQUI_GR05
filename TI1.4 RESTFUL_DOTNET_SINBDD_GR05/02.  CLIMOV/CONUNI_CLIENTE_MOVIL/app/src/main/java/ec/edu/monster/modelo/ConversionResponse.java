package ec.edu.monster.modelo;

public class ConversionResponse {
    private double resultado;
    private String mensaje;
    private boolean exito;

    public ConversionResponse() {
    }

    public ConversionResponse(double resultado, String mensaje, boolean exito) {
        this.resultado = resultado;
        this.mensaje = mensaje;
        this.exito = exito;
    }

    public double getResultado() {
        return resultado;
    }

    public void setResultado(double resultado) {
        this.resultado = resultado;
    }

    public String getMensaje() {
        return mensaje;
    }

    public void setMensaje(String mensaje) {
        this.mensaje = mensaje;
    }

    public boolean isExito() {
        return exito;
    }

    public void setExito(boolean exito) {
        this.exito = exito;
    }
}
