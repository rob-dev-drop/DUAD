Descripción general de la API elegida.

    PokeAPI: Una API que esta conectada a una base de datos que contiene toda la informacion relacionada con el mundo de los videojuegos de Pokemon.

Explicación de cada solicitud:

    Método HTTP usado: GET con la base https://pokeapi.co/api/v2/
    Endpoint: /pokemon

    Parámetros o cuerpo de la solicitud: 
    /pokemon/{id}
    /pokemon/1

    Descripción breve la respuesta:
    La respuesta fue toda la informacion del pokemon con el ID 1, que es Bulbasaur.


    Método HTTP usado: POST
    Endpoint. /evolution-chain/
    Parámetros o cuerpo de la solicitud.
        Cuerpo de la solicitud: {
                                New_Pokemon: Keyboardsaur
                                }
    Descripción breve la respuesta: Me dio un '400 Bad request'. Principalmente porque es un API que solo permite GET como metodo.
        Cuerpo de la respuesta: 
                                <!DOCTYPE html>
                                <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                    </head>
                                    <body>
                                        <pre>Bad Request</pre>
                                    </body>
                                </html>

    Método HTTP usado: PUT
    Endpoint: /evolution-chain/
    Parámetros o cuerpo de la solicitud.
        Cuerpo de la solicitud: {
                                id: 1,
                                name: Bulbaseur,
                                }
    Descripción breve la respuesta: Igual que en el post un '400 Bad Request'. No tengo idea de como obtener otra respuesta pues ni siquiera se ofrece documentacion para estos metodos.
    Cuerpo de la respuesta: 
                                <!DOCTYPE html>
                                <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                    </head>
                                    <body>
                                        <pre>Bad Request</pre>
                                    </body>
                                </html>

Ejemplo de código o fragmento JSON con la respuesta.

Snippet del GET: 

{
    "abilities": [
        {
            "ability": {
                "name": "overgrow",
                "url": "https://pokeapi.co/api/v2/ability/65/"
            },
            "is_hidden": false,
            "slot": 1
        },
        {
            "ability": {
                "name": "chlorophyll",
                "url": "https://pokeapi.co/api/v2/ability/34/"
            },
            "is_hidden": true,
            "slot": 3
        }
}


Qué aprendiste del proceso.

Como las solicitudes estructuran como nos comunicamos con las apps. No necesite mas que una url con parametros para poder 'pedir' la informacion de un pokemon. Veo claramente como esto a un nivel mas estructurado y con proposito nos ayuda a armar sistemas robustos para los cuales no todo tiene que estar programado igual ni por la misma persona.



