# QR Code Generator para UABCS

Este es un generador de códigos QR para acceder a los enlaces relacionados con los diferentes grupos y turnos de la Universidad Autónoma de Baja California Sur (UABCS). Los usuarios pueden seleccionar la carrera, semestre, turno y, cuando sea aplicable, el grupo para generar un código QR que los redirigirá a la URL correspondiente.

## Funcionalidades

- **Selección de carrera**: Permite al usuario elegir entre varias carreras disponibles.
- **Selección de semestre**: Permite al usuario elegir el semestre correspondiente.
- **Selección de turno y grupo**: Dependiendo de la carrera y semestre, el usuario puede seleccionar el turno (Matutino o Vespertino) y, en algunos casos, el grupo (A o B).
- **Generación de código QR**: Una vez seleccionados los parámetros, el sistema genera un código QR que lleva al usuario a la URL asociada con los parámetros elegidos.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes:

- `streamlit`
- `qrcode`
- `Pillow`

## Uso
- **Selecciona tu carrera:** Escoge entre las carreras disponibles en el menú desplegable.
- **Selecciona tu semestre:** Elige el semestre correspondiente para tu carrera.
- **Selecciona tu turno:** Dependiendo de la carrera y semestre, elige entre los turnos disponibles (Matutino o Vespertino).
- **Selecciona tu grupo (si aplica):** Si el grupo está disponible, selecciona el grupo correspondiente.
- **Generar el código QR:** Haz clic en el botón "Generate QR Code" para generar un código QR que se redirigirá a la URL seleccionada.


Pasos para el setup

**Instalar Dependencias**

```
python -m pip install -r requirements.txt
```

**Activar el entorno virtual**

```
source dev_env/bin/activate
```

**Correr el servidor web**

```
streamlit run app.py
```

**Salvar cambios en git**

paso 1
```
git add .
```
paso 2
```
git commit -m 'COMENTARIO'
```
paso 3
```
git push origin main
```
