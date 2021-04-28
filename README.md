# djangoAPI

Instrucciones de uso: 
1. Levantar el contenedor de la API abriendo la terminal dentro de la carpeta DjangoPython y ejecutar el comando "docker-compose up".

2. Comprobar que el contenedor este funcionando correctamente, ingresando desde cualquier navegador, al link: https://localhost:8000 

3. Levantar el contenedor de la base de datos abriendo la terminal dentro de la carpeta db y ejecutar el comando "docker-compose up".

4. Para ingresar al contenido de la base de datos, utilizar cualquier administrador de base de datos (HeidiSQL, Workbench, etc) y a cotinuación se deben ingresar las siguientes credenciales:
usuario: mydbuser
contraseña: mydbpassword
puerto: 3306

5. Una vez realizado esto, con ayuda de Insomnia o PostMan, aplicar los métodos descritos en el documento RESTFul API References.pdf
