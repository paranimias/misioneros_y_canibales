# misioneros_y_canibales

## Cosas por hacer

- [ ] Revisar si ya está implementado darle click a los sprites para subirlos al bote, deberia ser parte de
  ejecutar el movimiento
- [ ] Darle click al bote según el lado en el que está
- [ ] (Bajar cosas del bote) Función que reciba numero de sprites que van moviéndose y en qué lado está el bote para determinar si o bien
  iterar las 2 posibles ubicaciones del sprite o darle click al que esté solo
- [ ] Crear un test

## Funcionamiento

1. El ambiente inicia y retorna un screenshot
2. El agente recibe la percepcion (screenshot) y su método compute ejecuta la acción con el mouse y retorna un
   caracter, que nos india si seguimos enviando screenshots o si ya terminó el juego

## Movimientos

Los movimientos del agente son los clicks, el Agente hará una serie de clicks guardados en una dequeue
Ya sabemos que si necesitamos cierto número de Misioneros o canibales, tenemos donde encontrarlos (actual_state) y
por tanto, en **donde hacer click**. Ahora tenemos que saber cómo bajarlos de la balsa/ Para eso necesitamos 6
coordenadas distintas que debemos revisar 2 si estamos moviendo a 2 al tiempo o un solo lugar para hacer click en
caso de que solo haya uno

### Desglose de movimientos

Un movimiento implica:
1. Subir cosas al bote (uno o dos clicks a las coordenadas en actual_coordinates["M"|"C"])

2. Darle click al bote (un solo click en actual_coordinates["B"])

3. Darle click a lo que queremos que se baje

- [x] Lista de coordenadas para bajar cosas del bote

4. Vuelve a empezar otro movimiento

## Datos importantes

### Colores

- Color de canibal (BGR): (24,93,160)
- Color del misionero (BGR): (157,178,255)


### Coordenadas de sprites de la derecha


fila, columna = y,x
|Canibal  |Posición |
|---------|---------|
|Canibal 1|1645, 387|
|Canibal 2|1504, 470|
|Canibal 3|1645, 722|


|Misionero  |Posición |
|-----------|---------|
|Misionero 1|1601, 559|
|Misionero 2|1476, 790|
|Misionero 3|1637, 930|

### Coordenadas de sprites de la izquierda

(fila, columna) = (y,x)
```
1.        |
  2.     /
6.  3.  | 
  4.   / 
5.    / 
```
 1. (380, 365) 
 2. (452, 488) 
 3. (559, 603) 
 4. (623, 454) 
 5. (737, 315) 
 6. (560, 280) 

### Coordenadas para bajar sprites de la barca

```
         /~ _________    ~    ~    ~       |       
 orilla /  / 1. 2. /   ~  rio    ~   ~     | orilla
       /  /_______/ ~  ~  ~    ~   ~  ~    |       

         /~ _________    ~    ~    ~       |       
 orilla /  /   3.  /   ~  rio    ~   ~     | orilla
       /  /_______/ ~  ~  ~    ~   ~  ~    |       

         /    ~    ~    ~       ~ _________|       
 orilla /   ~  rio    ~   ~      / 4. 5. / | orilla
       /    ~  ~    ~   ~  ~    /_______/ ~|       

         /    ~    ~    ~       ~ _________|       
 orilla /   ~  rio    ~   ~      /   6.  / | orilla
       /    ~  ~    ~   ~  ~    /_______/ ~|       
```

(fila, columna) = (y,x)
1. (745, 545)
2. (739, 654)
3. (745, 763)
4. (745, 1045)
5. (739, 1154)
6. (745, 1263)