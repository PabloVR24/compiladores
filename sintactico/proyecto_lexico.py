import re


class lexico:
    current_state: int = 0  # ESTA VARIABLE NOS INDICARA EN QUE ESTADO ESTAMOS
    counter: int = 0  # NOS DEJA SABER EN QUE CARACTER VAMOS
    previous_state: int = 0  # NOS DEJA SABER CUAL FUE EL ESTADO ANTERIOR
    final_states: list[int] = []  # LISTA DONDE SE VAN A GUARDAR LOS TOKENS.
    current_lexem: str = ''  # NOS AYUDA A GUARDAR LOS CARACTERES QUE SE VAN LEYENDO
    current_string: str = ''
    current_identifiers: list[str] = []
    #LISTA QUE NOS INDICA CON CUALES TOKENS SE DEBE REGRESAR UNA POSICION EN LA EJECUCION
    reset_states: list[int] = [306, 308, 316, 322, 326, 329, 331, 332, 333, 334, 501, 502, 503, 504, 505, 506, 507, 508, 509,
                               510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533]
    # ruta_entrada:str = 'archivo_lexico.txt'
    # ruta_salida:str = 'archivo_salida.txt'
    ruta_entrada: str = 'archivo_lexico.txt'
    ruta_salida: str = 'archivo_salida.txt'
    # MATRIZ DE ESTADOS
    matriz_estados: list[list[int]] = [
        [301, 302, 303, 304, 305, 1, 410, 4, 311, 7, 8, 9, 10,
            11, 318, 12, 321, 16, 22, 38, 28, 28, 29, 410, 0, 0,],
        [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306,
            306, 306, 306, 2, 306, 306, 306, 306, 306, 306, 306, 306, 306,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 3, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 307, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [308, 308, 308, 308, 308, 5, 308, 308, 308, 308, 308, 308, 308, 308,
            308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308,],
        [410, 410, 410, 410, 410, 410, 410, 6, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 310, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [400, 400, 400, 400, 400, 400, 400, 400, 400, 312, 400, 400, 400,
            400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400,],
        [401, 401, 401, 401, 401, 401, 401, 401, 401, 401, 313, 401, 401,
            401, 401, 401, 401, 401, 401, 401, 401, 401, 401, 401, 401, 401,],
        [402, 402, 402, 402, 402, 402, 402, 402, 402, 402, 402, 314, 402,
            402, 402, 402, 402, 402, 402, 402, 402, 402, 402, 402, 402, 402,],
        [403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 315,
            403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 403, 403,],
        [316, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316,
            317, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316, 316,],
        [319, 319, 319, 319, 319, 319, 319, 319, 319, 319, 319, 319, 319,
            319, 13, 319, 319, 319, 319, 319, 319, 319, 319, 319, 319, 319,],
        [404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404,
            404, 15, 404, 404, 404, 404, 404, 14, 14, 14, 404, 14, 404,],
        [404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404,
            404, 15, 404, 404, 404, 404, 404, 14, 14, 14, 404, 14, 404,],
        [404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404,
            404, 404, 320, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404,],
        [322, 322, 322, 322, 322, 322, 322, 322, 323, 322, 322, 322, 322,
            322, 322, 322, 20, 17, 322, 322, 322, 322, 322, 322, 322, 322,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 18, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 19, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 324, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 21, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 325, 410, 410, 410, 410, 410, 410, 410, 410,],
        [326, 326, 326, 326, 326, 326, 326, 326, 326, 326, 326, 326, 326,
            326, 326, 326, 26, 326, 23, 326, 326, 326, 326, 326, 326, 326,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 24, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 25, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 327, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 27, 410, 410, 410, 410, 410, 410, 410, 410, 410,],
        [410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410, 410,
            410, 410, 410, 410, 410, 328, 410, 410, 410, 410, 410, 410, 410,],
        [329, 329, 329, 329, 329, 329, 329, 329, 329, 329, 329, 329, 329,
            329, 329, 329, 329, 329, 329, 329, 329, 28, 28, 28, 329, 329,],
        [331, 331, 331, 331, 331, 331, 33, 331, 331, 331, 331, 331, 331,
            331, 331, 331, 331, 331, 331, 331, 30, 411, 29, 331, 331, 331,],
        [406, 406, 406, 406, 406, 406, 406, 406, 31, 406, 406, 406, 406,
            31, 406, 406, 406, 406, 406, 406, 31, 406, 406, 406, 406, 406,],
        [406, 406, 406, 406, 406, 406, 406, 406, 406, 406, 406, 406, 406,
            406, 406, 406, 406, 406, 406, 406, 406, 406, 32, 406, 406, 406,],
        [332, 332, 332, 332, 332, 332, 332, 332, 332, 332, 332, 332, 332,
            332, 332, 332, 332, 332, 332, 332, 332, 411, 32, 332, 332, 332,],
        [407, 407, 407, 407, 407, 407, 407, 407, 407, 407, 407, 407, 407,
            407, 407, 407, 407, 407, 407, 407, 407, 407, 34, 407, 407, 407,],
        [333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333,
            333, 333, 333, 333, 333, 333, 333, 35, 408, 34, 333, 333, 333,],
        [408, 408, 408, 408, 408, 408, 408, 408, 36, 408, 408, 408, 408,
            36, 408, 408, 408, 408, 408, 408, 36, 408, 408, 408, 408, 408,],
        [408, 408, 408, 408, 408, 408, 408, 408, 408, 408, 408, 408, 408,
            408, 408, 408, 408, 408, 408, 408, 408, 407, 37, 408, 408, 408,],
        [334, 334, 334, 334, 334, 334, 334, 334, 334, 334, 334, 334, 334,
            334, 334, 334, 334, 334, 334, 334, 334, 408, 37, 334, 334, 334,],
        [409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409,
            409, 409, 409, 409, 409, 409, 335, 39, 39, 39, 409, 39, 409,],
        [409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409, 409,
            409, 409, 409, 409, 409, 409, 335, 39, 39, 39, 409, 39, 409,],

    ]

    # LISTA DE PALABRAS RESERVADAS DEL AUTOMATA
    palabras_reservadas = {'absoluto': 501, 'cadena': 502, 'dec': 503, 'decimal': 504, 'def': 505, 'do': 506, 'elif': 507, 'else': 508, 'entero': 509, 'esdecimal': 510, 'esnumero': 511, 'in': 512, 'ifwhether': 513, 'lectura': 514, 'list': 515,
                           'logic': 516, 'longitud': 517, 'main': 518, 'maximo': 519, 'minimo': 520, 'numerical': 521, 'potencia': 522, 'range': 523, 'redondear': 524, 'repeat': 525, 'return': 526, 'string': 527, 'sumando': 528, 'true': 529, 'vars': 530, 'when': 531, 'since': 532, 'imprimir': 533}

    # COLUMNAS DE LA TABLA DE CARACTERES
    diccionario_caracteres = {'{': 0, '}': 1, '(': 2, ')': 3, ',': 4, '=': 5, '.': 6, ':': 7, '-': 8,
                              '[': 9, ']': 10, '&': 11, '|': 12, '+': 13, '*': 14, '/': 15, '!': 16, '<': 17, '>': 18, '"': 19, 'E': 20, '[a-zA-Z]': 21, '[0-9]': 22, '_': 23, ' ': 24, '\n': 25}
    # POSIBLES ERRORES PARA MOSTRAR
    diccionario_errores = {400: "Simbolo [ invalido", 401: "Simbolo ] invalido", 402: "Simbolo & invalido", 403: "Simbolo | invalido", 404: "Comentario mal construido", 406: "Número entero con NA mal construido",
                           408: "Número real con NA mal construido", 407: "Número real mal construido", 409: "Texto mal construido", 410: 'Numero Entero mal construido', 411: "Número entero mal construido", 499: "Desconocido: Verificar codigo"}
    # DICCIONARIO CON TODOS LOS TOKENS 
    diccionario_completo = {301: "{", 302: "}", 303: "(", 304: ")", 305: ",", 306: "=", 307: "=!!=", 308: ":", 310: ":=::", 311: "-", 312: "[[", 313: "]]", 314: "&&", 315: "||", 316: "+", 317: "++", 318: "*", 319: "/", 320: "COMENTARIO", 321: "!", 322: "<", 323: "<-",
                            324: "<<!!=", 325: "<!!<", 326: ">", 327: ">>!!=", 328: ">!!>", 329: "IDENTIFICADOR", 331: "NUMERO ENTERO", 332: "NUMERO ENTERO CON NOTACION DESARROLLADA", 333: "NUMERO REAL", 334: "NUMERO REAL CON NOTACION DESARROLLADA", 335: "CADENA DE TEXTO", 999: "EOF"}

    # ESTÁ FUNCIÓN SE UTILIZA PARA ABRIR EL ARCHIVO FUENTE, LEERLO, GUARDAR SU INFORMACIÓN Y CERRARLO.
    def read_code(self):
        f = open(self.ruta_entrada, 'r')
        code = f.read()
        f.close()
        return code

    # DETECTAR COLUMNA USANDO EL DICCIONARIO_CARACTERES HACIENDO VALIDACIONES PARA LAS LETRAS, DIGITOS Y E
    def columna_tabla(self, car, prevState):
        col = 499
        if re.match("[a-zA-Z]", car):
            if car == "E" and (prevState == 29 or prevState == 30 or prevState == 34 or prevState == 35):
                col = self.diccionario_caracteres['E'] # TOMAMOS LA E COMO VALIDA EN CASO DE QUE SEA UN NUMERO CON NOTACION DESARROLLADA
            else:
                col = self. diccionario_caracteres['[a-zA-Z]']
        elif re.match("[0-9]", car):
            col = self.diccionario_caracteres['[0-9]']
        elif car in self.diccionario_caracteres:
            col = self.diccionario_caracteres[car]
        return col
    
    # ESTA FUNCION SE MANDA A LLAMAR PARA RESTABLECER EL ESTADO A 0
    def restart(self, state: int):
        self.current_state = 0
        self.current_lexem = ''

        if (state in self.reset_states):
            self.counter -= 1 # EN DADO CASO QUE EL ESTADO ESTE EN LA LISTA DE LOS QUE DEBEN REGRESAR UNA POSICION EL CONTADOR SE REGRESA
        self.final_states.append(state)

    def analisis_codigo(self, inftxt, matriz_estados):
        # SE AGREGA UN SALTO DE LINEA AL ARCHIVO AL FINAL
        inftxt = inftxt + '\n'
        # NOS DA EL NUMERO DE CARACTERES EN EL ARCHIVO DE TEXTO
        car_length = len(inftxt)
        # MIENTRAS EL CONTADOR SEA DISTINTO A LA LONGITUD (EN CARACTERES) DEL ARCHIVO
        while self.counter != car_length:
            palabra_reservada = False
            caracter = inftxt[self.counter]  # SE OBTIENE EL CARACTER
            columna = self.columna_tabla(caracter, self.previous_state)
            if (columna == 499):
                self.final_states.append(499)
                return self.final_states

            self.current_lexem += caracter  # SE VA SUMANDO EL CARACTER A UNA CADENA STRING
            self.current_state = matriz_estados[self.current_state][columna] # SE BUSCA EL ESTADO EN LA TABLA

            if (self.current_state >= 300): # SIMBOLOS
                if (self.current_state >= 400 and self.current_state < 500):
                    self.final_states.append(self.current_state)
                    return self.final_states
                if (self.current_state == 329): # IDENTIFICADOR
                    self.current_string = self.current_lexem[:-1].strip()
                    if (self.current_string in self.palabras_reservadas): # PALABRAS RESERVADAS
                        self.restart(
                            self.palabras_reservadas[self.current_string.strip()])
                        self.current_string = ''
                        palabra_reservada = True # ESTO ES PARA QUE NO SE REGRESE OTRA POSICION SIENDO PALABRA RESERVADA
                if (not palabra_reservada): # SI NO ES PALABRA RESERVADA ENTONCES REGRESA UNA POSICION SOLAMENTE
                    self.restart(self.current_state)
                    palabra_reservada = False # SI NO LO PONIA REGRESABA 2 POSICIONES EN LAS PALABRAS RESERVADAS

            self.previous_state = self.current_state

            self.counter += 1 # SE AUMENTA EL CONTADOR

        self.final_states.append(999) # SE AGREGA $EOF
        return self.final_states
