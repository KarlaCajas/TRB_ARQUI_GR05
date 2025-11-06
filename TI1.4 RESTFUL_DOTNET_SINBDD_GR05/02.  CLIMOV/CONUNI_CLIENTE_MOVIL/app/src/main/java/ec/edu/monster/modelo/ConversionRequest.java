package ec.edu.monster.modelo;

public class ConversionRequest {
    private String tipoConversion;
    private String unidadOrigen;
    private String unidadDestino;
    private double valor;

    public ConversionRequest() {
    }

    public ConversionRequest(String tipoConversion, String unidadOrigen, String unidadDestino, double valor) {
        this.tipoConversion = tipoConversion;
        this.unidadOrigen = unidadOrigen;
        this.unidadDestino = unidadDestino;
        this.valor = valor;
    }

    public String getTipoConversion() {
        return tipoConversion;
    }

    public void setTipoConversion(String tipoConversion) {
        this.tipoConversion = tipoConversion;
    }

    public String getUnidadOrigen() {
        return unidadOrigen;
    }

    public void setUnidadOrigen(String unidadOrigen) {
        this.unidadOrigen = unidadOrigen;
    }

    public String getUnidadDestino() {
        return unidadDestino;
    }

    public void setUnidadDestino(String unidadDestino) {
        this.unidadDestino = unidadDestino;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
}
