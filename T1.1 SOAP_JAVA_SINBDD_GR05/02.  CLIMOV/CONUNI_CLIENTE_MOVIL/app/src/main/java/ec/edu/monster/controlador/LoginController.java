package ec.edu.monster.controlador;
import ec.edu.monster.modelo.Usuario;
public class LoginController {
    private final Usuario usuarioValido;

    public LoginController() {
        // Datos quemados (hardcoded)
        usuarioValido = new Usuario("MONSTER", "Monster9");
    }

    public boolean autenticar(String username, String password) {
        return usuarioValido.getUsername().equals(username)
                && usuarioValido.getPassword().equals(password);
    }
}
