# Instrucciones para agregar la imagen de Monster

## Pasos:

1. Guarda la imagen de Monster (el personaje azul con cuernos y lentes) en esta carpeta
2. Nombra el archivo como: **monster.png**
3. La imagen se mostrará de forma circular en el login

## Ubicación:
Esta carpeta: `static/images/`

## Nombre del archivo:
`monster.png` o `monster.jpg`

## Si usas un nombre diferente:
Edita el archivo `templates/login.html` y cambia la línea:
```html
<img src="{{ url_for('static', filename='images/monster.png') }}" alt="Monster Avatar">
```

Cambia `monster.png` por el nombre de tu archivo.
