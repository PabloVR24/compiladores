import re


class lexico:
    current_state = 0  # esta variable nos indicara en que estado estamos
    counter = 0  # nos deja saber en que caracter vamos
    previous_state = 0  # nos deja saber cual fue el estado anterior
    final_states = []  # lista donde se van a guardar los tokens.
    current_lexem = ''  # nos ayuda a guardar los caracteres que se van leyendo
    current_string = ''
    reset_states = [306, 308, 316, 322, 326, 329, 331, 332, 333, 334, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531]

    # Matriz de estados del automata, cada posicion de una lista es una columna, cada lista es una fila
    matriz_estados = [
[301,302,303,304,305,1,410,4,311,7,8,9,10,11,318,12,321,16,22,38,28,28,29,410,0,0,],
[306,306,306,306,306,306,306,306,306,306,306,306,306,306,306,306,2,306,306,306,306,306,306,306,306,306,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,3,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,307,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,],
[308,308,308,308,308,5,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,308,],
[410,410,410,410,410,410,410,6,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,310,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,],
[400,400,400,400,400,400,400,400,400,312,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,],
[401,401,401,401,401,401,401,401,401,401,313,401,401,401,401,401,401,401,401,401,401,401,401,401,401,401,],
[402,402,402,402,402,402,402,402,402,402,402,314,402,402,402,402,402,402,402,402,402,402,402,402,402,402,],
[403,403,403,403,403,403,403,403,403,403,403,403,315,403,403,403,403,403,403,403,403,403,403,403,403,403,],
[316,316,316,316,316,316,316,316,316,316,316,316,316,317,316,316,316,316,316,316,316,316,316,316,316,316,],
[319,319,319,319,319,319,319,319,319,319,319,319,319,319,13,319,319,319,319,319,319,319,319,319,319,319,],
[404,404,404,404,404,404,404,404,404,404,404,404,404,404,15,404,404,404,404,404,14,14,14,404,14,404,],
[404,404,404,404,404,404,404,404,404,404,404,404,404,404,15,404,404,404,404,404,14,14,14,404,14,404,],
[404,404,404,404,404,404,404,404,404,404,404,404,404,404,404,320,404,404,404,404,404,404,404,404,404,404,],
[322,322,322,322,322,322,322,322,323,322,322,322,322,322,322,322,20,17,322,322,322,322,322,322,322,322,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,18,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,19,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,324,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,21,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,325,410,410,410,410,410,410,410,410,],
[326,326,326,326,326,326,326,326,326,326,326,326,326,326,326,326,26,326,23,326,326,326,326,326,326,326,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,24,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,25,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,327,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,27,410,410,410,410,410,410,410,410,410,],
[410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,410,328,410,410,410,410,410,410,410,],
[329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,329,28,28,28,329,329,],
[331,331,331,331,331,331,33,331,331,331,331,331,331,331,331,331,331,331,331,331,30,411,29,331,331,331,],
[406,406,406,406,406,406,406,406,31,406,406,406,406,31,406,406,406,406,406,406,31,406,406,406,406,406,],
[406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,32,406,406,406,],
[332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,332,411,32,332,332,332,],
[407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,407,34,407,407,407,],
[333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,333,35,408,34,333,333,333,],
[408,408,408,408,408,408,408,408,36,408,408,408,408,36,408,408,408,408,408,408,36,408,408,408,408,408,],
[408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,408,407,37,408,408,408,],
[334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,334,408,37,334,334,334,],
[409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,335,39,39,39,409,39,409,],
[409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,409,335,39,39,39,409,39,409,],

    ]

    # Lista de palabras reservadas del automata
    palabras_reservadas = { 'absoluto': 501, 'cadena': 502, 'dec': 503, 'decimal': 504, 'def': 505, 'do': 506, 'elif': 507, 'else': 508, 'entero': 509, 'esdecimal': 510, 'esnumero': 511, 'in': 512, 'ifwhether': 513, 'lectura': 514, 'list': 515, 'logic': 516, 'longitud': 517, 'main': 518, 'maximo': 519, 'minimo': 520, 'numerical': 521, 'potencia': 522, 'range': 523, 'redondear': 524, 'repeat': 525, 'return': 526, 'string': 527, 'sumando': 528, 'true': 529, 'vars': 530, 'when': 531}

    # Columas de la tabla de caracteres
    diccionario_caracteres = { '{': 0, '}': 1, '(': 2, ')': 3, ',': 4, '=': 5, '.': 6, ':': 7, '-': 8, '[': 9, ']': 10, '&': 11, '|': 12, '+': 13, '*': 14, '/': 15, '!': 16, '<': 17, '>': 18, '"': 19, 'E': 20, '[a-zA-Z]': 21, '[0-9]': 22, '_': 23, ' ': 24, '\n': 25}

    diccionario_errores = { 400: "Simbolo [ invalido", 401: "Simbolo ] invalido", 402: "Simbolo & invalido", 403: "Simbolo | invalido", 404: "Comentario mal construido", 406: "Número entero con NA mal construido", 408: "Número real con NA mal construido", 407: "Número real mal construido", 409: "Texto mal construido", 410: 'Numero Entero mal construido', 411: "Número entero mal construido", 499: "Desconocido: Verificar codigo"}

    diccionario_completo = { 301: "{", 302: "}", 303: "(", 304: ")", 305: ",", 306: "=", 307: "=!!=", 308: ":", 310: ":=::", 311: "-", 312: "[[", 313: "]]", 314: "&&", 315: "||", 316: "+", 317: "++", 318: "*", 319: "/", 320: "COMENTARIO", 321: "!", 322: "<", 323: "<-", 324: "<<!!=", 325: "<!!<", 326: ">", 327: ">>!!=", 328: ">!!>", 329: "IDENTIFICADOR", 331: "NUMERO ENTERO", 332: "NUMERO ENTERO CON NOTACION DESARROLLADA", 333: "NUMERO REAL", 334: "NUMERO REAL CON NOTACION DESARROLLADA", 335: "CADENA DE TEXTO", 999: "EOF"}

    # Está función se utiliza para abrir el archivo fuente, leerlo, guardar su información y cerrarlo.
    def read_code(self):
        f = open('lexico/archivo_lexico.txt', 'r')
        code = f.read()
        f.close()
        return code
    
    # Detectar columna usando el diccionario_caracteres haciendo validaciones para las letras, digitos y E
    def columna_tabla(self, car, prevState):
        col = 499
        if re.match("[a-zA-Z]", car):
            if car == "E" and (prevState == 29 or prevState == 30 or prevState == 34 or prevState == 35):
                col = self.diccionario_caracteres['E']
            else:
                col = self. diccionario_caracteres['[a-zA-Z]']
        elif re.match("[0-9]", car):
            col = self.diccionario_caracteres['[0-9]']
        elif car in self.diccionario_caracteres:
            col = self.diccionario_caracteres[car]

        return col

    def restart(self, state: int):
        
        self.current_state = 0
        self.current_lexem = ''

        if (state in self.reset_states):
            self.counter -= 1
        self.final_states.append(state)

    def analisis_codigo(self, inftxt, matriz_estados):
        # nos da el numero de caracteres en el archivo de texto
        inftxt = inftxt + '\n'
        car_length = len(inftxt)
        # mientras el contador sea distinto a la longitud (en caracteres) del archivo
        while self.counter != car_length:
            palabra_reservada = False
            caracter = inftxt[self.counter]  # Se obtiene el caracter
            columna = self.columna_tabla(caracter, self.previous_state) 
            if (columna == 499):
                self.final_states.append(499)
                return self.final_states
    
            self.current_lexem += caracter  # se va sumando el caracter a una cadena string
            self.current_state = matriz_estados[self.current_state][columna]
            #print(self.current_state, ' -> ', caracter)
           
            if (self.current_state >= 300):
                if (self.current_state >= 400 and self.current_state < 500):
                    self.final_states.append(self.current_state)
                    return self.final_states
            
                if (self.current_state == 329):
                    self.current_string = self.current_lexem[:-1].strip()
                    if (self.current_string in self.palabras_reservadas):
                        self.restart(self.palabras_reservadas[self.current_string.strip()])
                        self.current_string = ''
                        palabra_reservada = True
                if(not palabra_reservada):
                    self.restart(self.current_state)
                    palabra_reservada = False

            self.previous_state = self.current_state
            
            self.counter += 1
        
        self.final_states.append(999)
        return self.final_states


analizador_lexico = lexico()
codigo_fuente = analizador_lexico.read_code()  # Lee el codigo fuente
aux = analizador_lexico.analisis_codigo(
    codigo_fuente, analizador_lexico.matriz_estados)
print()
for i in aux:
    # print(i) !DESACTIVAR COMENTARIO PARA SOLO LOS ESTADOS Y COMENTAR LOS SIGUIENTES
    for llave, valor in analizador_lexico.palabras_reservadas.items():
        if valor == i:
            print(i, ' : ', llave)
    if i in analizador_lexico.diccionario_completo:
        print(i,' : ',analizador_lexico.diccionario_completo[i])
    if i in analizador_lexico.diccionario_errores:
        print('ERROR: ',i,' : ',analizador_lexico.diccionario_errores[i])
