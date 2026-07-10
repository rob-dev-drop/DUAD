Ejercicios: Internet, HTTP y APIs

El Internet
1. Del Cliente al Servidor 
Explique paso a paso qué ocurre cuando usted escribe www.youtube.com en el navegador hasta que el video aparece en pantalla.

    Debe incluir en su explicación:
        Qué hace el cliente (navegador).
        Qué papel cumple el DNS.
        Qué ocurre con la dirección IP.
        Qué hace el servidor.
        Cómo entra en juego el protocolo HTTP/HTTPS.
    
    Puedes incluir un dibujo o diagrama que muestre cómo viaja la información entre cliente, DNS y servidor.



Respuesta: 

El cliente (el navegador) hace un request a un servidor DNS para transformar el url de https://www.youtube.com/ en la ip publica del servidor de youtube (hacemos un request y recibimos un response del DNS). Ahora el navegador con la informacion brindada por el DNS, hace el request a la ip del servidor de youtube, el cual retorna las respuestas para que cargue la pagina en nuestro navegador. Todo esto ocurre con el protocolo HTTP, el cual el navegador usa para enviar el request del tipo de response que quiere obtener a traves de la ruta y sus parametros, que es lo que hace por defecto con un GET. 

Hay otros pasos intermedios que no hemos visto a fondo como certificados o protocolos TCP, pero creo que eso va mas de la mano con la parde de redes.   