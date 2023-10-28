# 📄 Práctica: "Ramificación y Salto con y sin Subestimación"

Esta práctica tiene como objetivo explorar y comparar dos métodos de búsqueda heurística comúnmente utilizados en la resolución de problemas de búsqueda en inteligencia artificial: la "<strong>Ramificación y Salto</strong>" (Branch and Bound) y la "<strong>Ramificación y Salto con Subestimación</strong>" (Branch and Bound with Subestimation Heuristic).

# 👥 Equipo de desarrollo (Ctrl + Click para ver los perfiles)

[![GitHub](https://img.shields.io/badge/GitHub-Andrea%20Santana%20Lopez-purple?style=flat-square&logo=github)](https://github.com/AndreaSantalos)

[![GitHub](https://img.shields.io/badge/GitHub-Alejandro%20David%20Arzola%20Saavedra-blue?style=flat-square&logo=github)](https://github.com/AlejandroDavidArzolaSaavedra)
  
## Resumen
El propósito principal de esta práctica es ilustrar cómo ambos métodos generan la misma solución óptima al buscar una ruta entre diferentes ciudades en el contexto del grafo de ciudades de <strong>Rumanía</strong>, como se muestra en la siguiente imagen en la que se utilizo networkx.

<ul align="center">		
  <a href="https://en.wikipedia.org/wiki/Romania" target="_blank">
    <img style="width:30rem"  src="https://i.imgur.com/phIyAEK.png">
  </a>
</ul>

En este caso, hemos aplicado los algoritmos de Ramificación y Acotación, así como Ramificación y Acotación con Subestimación, <strong>la heurística consiste en una línea recta desde el estado en el que nos encontramos hasta el estado final</strong>, donde se encuenta la ruta óptima entre dos ciudades en el grafo de ciudades de Rumanía. A pesar de que ambos métodos alcanzan el mismo resultado, es notable que <strong>la Ramificación y Acotación con la Heurística aplicada expande considerablemente menos nodos en el grafo de búsqueda</strong>, lo que demuestra su eficiencia en términos de recursos computacionales utilizados.

Podemos ver una comparación de las diferencias entre los algoritmos en el siguiente gráfico, donde observamos los nodos expandidos y visitados por distintos algoritmos en diferentes ciudades de Rumanía. Para esto, se utilizó lightweight-charts.

<ul align="center">		
  <a href="https://tradingview.github.io/lightweight-charts/docs" target="_blank">
    <img style="width:50rem"  src="https://i.imgur.com/vsg211K.png">
  </a>
</ul>

Por ultimos mostramos una tablas con todos los datos importantes recopilados de los distintos algoritmos, en las distinas ciudades de Romania:
<ul align="center">		
    <img style="width:40rem"  src="https://i.imgur.com/QI88qqa.png">
</ul>

<ul align="center">		
    <img style="width:40rem"  src="https://i.imgur.com/rGoE3Jm.png">
</ul>

<ul align="center">		
    <img style="width:40rem"  src="https://i.imgur.com/m9880jP.png">
</ul>

<ul align="center">		
    <img style="width:40rem"  src="https://i.imgur.com/ArUzNaS.png">
</ul>

## Cómo Ejecutar
Para ejecutar la práctica y realizar las pruebas, sigue estos pasos:

1. Clona este repositorio en tu máquina local:
```bash
git clone <https://github.com/AlejandroDavidArzolaSaavedra/practicas_fsi>
```
2. Navega al directorio de la práctica:
```bash
cd practicas_fsi
```
3. Ejecuta el programa principal con los archivos modificados:
```bash
python run.py
```
Observa los resultados de las pruebas y las comparaciones entre los métodos.

# 🤝 Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacerlo. Puedes abrir problemas (issues) o enviar solicitudes de extracción (pull requests) para mejorar el código o agregar nuevas características.
