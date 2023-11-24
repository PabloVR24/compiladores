# Lexico: Pablo Valera Rangel

## Lista de Simbolos

- `301 : {`
- `302 : }`
- `303 : (`
- `304 : )`
- `305 : ,`
- `306 : =`
- `307 : =!!=`
- `308 : :`
- `310 : :=::`
- `311 : -`
- `312 : [[`
- `313 : ]]`
- `314 : &&`
- `315 : ||`
- `316 : +`
- `317 : ++`
- `318 : *`
- `319 : /`
- `321 : !`
- `322 : <`
- `323 : <-`
- `324 : <<!!=`
- `325 : <!!<`
- `326 : >`
- `327 : >>!!=`
- `328 : >!!>`

## Palabras Reservadas

- `501 : absoluto`
- `502 : cadena`
- `503 : dec`
- `504 : decimal`
- `505 : def`
- `506 : do`
- `507 : elif`
- `508 : else`
- `509 : entero`
- `510 : esdecimal`
- `511 : esnumero`
- `512 : in`
- `513 : ifwhether`
- `514 : lectura`
- `515 : list`
- `516 : logic`
- `517 : longitud`
- `518 : main`
- `519 : maximo`
- `520 : minimo`
- `521 : numerical`
- `522 : potencia`
- `523 : range`
- `524 : redondear`
- `525 : repeat`
- `526 : return`
- `527 : string`
- `528 : sumando`
- `529 : true`
- `530 : vars`
- `531 : when`

## Expresiones Regulares

### Identificadores

$ \text{letra} \left( \text{letra /}{\text{ dígito /} \, \ \_} \right)^* $

### Numeros enteros

$\left({\text{dígito}} \right)^+ $

### Numeros reales

$\left({\text{dígito}} \right)^+ {\text{ . }} \left({\text{dígito}} \right)^+ $

### Numeros enteros con ND

$\left({\text{dígito}} \right)^+ {\text{E(+ / - / E)}} \left({\text{dígito}} \right)^+$

### Numeros reales con ND

$\left({\text{dígito}}\right)^+ {\text{ . }} \left({\text{dígito}} \right)^+ {\text{E(+ / - / E)}} \left({\text{dígito}} \right)^+$

### Comentarios
${\text{/*}} \left({\text{letra / digito / espacio}}\right)^+ {\text{*/}}$

### Texto
${\text{"}} \left({\text{letra / digito / espacio}}\right)^+ {\text{"}}$