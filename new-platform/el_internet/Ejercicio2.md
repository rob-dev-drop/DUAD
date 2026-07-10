Frontend y Backend en acción 🧩
Suponga que está construyendo una app web para agendar citas médicas.

1. Indique qué parte del sistema correspondería al frontend y cuál al backend.
2. Mencione tres tecnologías posibles para cada uno.
3. Explique brevemente cómo el frontend se comunicaría con el backend (mencione los conceptos de API, HTTP y request/response).


Respuesta: 

1) El frontend seria la interfaz de usuario la cual los pacientes usarian para agendar las citas. El backend seria la logica del negocio, como la interaccion entre el usuario y el frontend interviene su funcionamiento y su persistencia de datos (en una base de datos, en este caso donde se guardan las citas agendadas.)

2) Frontend: HTML, CSS y JavaScript.
    Backend: Python, C#, GraphQL

3) La interfaz de la app tendria un form donde los usuarios pueden poner la informacion necesaria para agendar una cita. Empezando por la fecha deseada para la cita. Una vez seleccionada la fecha, el cliente (el app) hace un request http por medio de un API tipo get para obtener la informacion de que horas y especialidades estan disponibles para la fecha seleccionada. El servidor recibe el request y responde con la informacion correspondiente solo de las horas y especialidades disponibles para la fecha. El app lee esta informacion mostrandole al usuario que horas puede seleccionar para seguir con el proceso de agendar su cita. Una vez seleccionada la hora, aparece otro form para consolidar la informacion necesaria para agendar: Nombre, Apellido, Cedula. Esta informacion ahora es envidada en un request distinto, de tipo POST para que el servidor la aloje en su base de datos y devuelve un response, en el happy path, un codigo de "success" 200 diciendole al app que su cita ha sido agendada y puede mostrar un mensaje de exito al usuario.


