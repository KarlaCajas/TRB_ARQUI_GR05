package ec.edu.monster.controlador;

import org.ksoap2.serialization.Marshal;
import org.ksoap2.serialization.PropertyInfo;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import java.io.IOException;

public class MarshalDouble implements Marshal {

    @Override
    public Object readInstance(org.xmlpull.v1.XmlPullParser parser,
                               String namespace,
                               String name,
                               PropertyInfo expected) throws IOException, org.xmlpull.v1.XmlPullParserException {
        String text = parser.nextText();
        // Extraer solo la parte numérica, mejorando el regex para manejar también números negativos
        text = text.replaceAll("[^0-9.\\-]", "");
        try {
            return Double.parseDouble(text);
        } catch (NumberFormatException e) {
            // En caso de que no se pueda parsear, devolver 0.0
            return 0.0;
        }
    }

    @Override
    public void register(SoapSerializationEnvelope envelope) {
        envelope.addMapping(envelope.xsd, "double", Double.class, this);
        envelope.addMapping(envelope.xsd, "decimal", Double.class, this);
    }

    @Override
    public void writeInstance(org.xmlpull.v1.XmlSerializer writer,
                              Object obj) throws IOException {
        writer.text(obj.toString());
    }
}