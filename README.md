# Juego de Pelea Pokémon (Examen T1)

Este proyecto corresponde al **Problema 1** del examen T1 del curso **Análisis de Algoritmos y Estrategias de Programación**.

## 👩‍🎓 Autor
- **Entrenador 1:** Miguelina Dios  
- **Pokémon:** Dracoflame 🔥🐉  

## 📌 Descripción
El programa simula una pelea de Pokémon usando clases, funciones y estructuras básicas en Python.  
Al iniciar el juego, se crea automáticamente el primer entrenador **Miguelina Dios** y su Pokémon **Dracoflame** con estadísticas generadas aleatoriamente.  

El usuario puede elegir:  
- **Pelear (P):** Crear un segundo entrenador y Pokémon, y luchar por turnos hasta que uno pierda toda su vida.  
- **Finalizar (F):** Terminar el juego y mostrar las estadísticas de Dracoflame, junto con el número de encuentros ganados y perdidos.

## ⚙️ Funcionalidades principales
- **Clases:**
  - `Entrenador`: guarda el nombre del entrenador.
  - `Pokemon`: guarda nombre, ataque máximo, vida máxima y vida actual.
- **Funciones:**
  - `crearEntrenadorPokemon()`: crea entrenador y Pokémon.
  - `valorDeAtaque()`: genera un ataque aleatorio.
  - `defender()`: descuenta vida con posibilidad de bloquear ataque.
  - `recuperar()`: restaura la vida al máximo antes de una pelea.

## 🚀 Ejecución del programa
1. Asegúrate de tener **Python 3.8 o superior** instalado.  
2. Clona este repositorio o descarga el archivo `pokemon.py`.  
3. Abre una terminal en la carpeta del proyecto y ejecuta:  
   ```bash
   python pokemon.py
   ```
4. Sigue las instrucciones del menú en pantalla.

## 📸 Evidencia
Adjuntar capturas de pantalla en el archivo **resultado.docx**:
1. Creación del primer entrenador y Pokémon.  
2. Desarrollo de una pelea.  
3. Fin del juego con estadísticas.  

---
✨ *Proyecto desarrollado como parte del curso de Ingeniería de Sistemas Computacionales (2025-2).*
