from proyecto_lexico import lexico


class sintactico:
    # COLORES PARA LA IMPRESION EN CONSOLA
    OK = "\033[92m"  # FINALIZAR SIN ERRORES
    WARNING = "\033[93m"  # INFORMACION
    FAIL = "\033[91m"  # ERRORES
    ALERT = "\033[38;5;208m"
    RESET = "\033[0m"  # ACTUALIZACIONES
    PURPLE = "\033[95m" # COMENTARIOS
    # DICCIONARIOS
    counter = 0
    # DICCIONARIO CON CLAVE: SIMBOLO_NO TERMINAL, VALOR: NUMERO DE FILA, SIRVE PARA IDENFIFICAR LA FILA DE LA TABLA SINTACTICA
    prod_to_row = {'P': 0, 'PRINCIPAL': 1, 'BLOQUE': 2, 'FUNCIONES': 3, 'FUNCIONES_PRIMA': 4, 'PARAMETROS': 5, 'PARAMETROS_PRIMA': 6, 'RETURN': 7, 'TIPO': 8, 'SECCION_VARIABLES': 9, 'DECLARACION_VARIABLES': 10, 'DECLARACION_VARIABLES_PRIMA': 11, 'LISTA_VARIABLES': 12, 'LISTA_VARIABLES_PRIMA': 13, 'ESTATUTOS': 14, 'ESTATUTO': 15, 'ASIGNACION': 16, 'ASIGNACION_PRIMA': 17, 'FUNCION_BUILT_IN': 18, 'LISTA_ELEMENTO': 19, 'LISTA_ELEMENTO_PRIMA': 20, 'IMPRESION': 21, 'IMPRESION_PRIMA': 22, 'ESTATUTO_IF': 23, 'CONDICION': 24, 'ESTATUTO_CYCLEWHILE': 25, 'ESTATUTO_CYCLEFOR': 26, 'FOR_PRIMA': 27, 'INCREMENTO': 28, 'ESTATUTO_CYCLEREPEAT': 29, 'ESTATUTO_CYCLEDO': 30, 'ELIF': 31, 'RANGE': 32, 'START': 33, 'STOP': 34, 'STEP': 35, 'EXPB': 36, 'EXPB_PRIMA': 37, 'TERMB': 38, 'TERMB_PRIMA': 39, 'EXP': 40, 'EXP_PRIMA': 41, 'TERM': 42, 'TERM_PRIMA': 43, 'FACTOR': 44, 'FUNCT': 45, 'OPER': 46
                   }
    # DICCIONARIO CON CLAVE: TOKEN , VALOR: NUMERO DE COLUMNA, SIRVE PARA IDENFIFICAR LA COLUMNA DE LA TABLA SINTACTICA
    token_to_column = {
        301: 0, 302: 1, 303: 2, 304: 3, 305: 4, 306: 5, 307: 6, 308: 7, 310: 8, 311: 9, 312: 10, 313: 11, 314: 12, 315: 13, 316: 14, 317: 15, 318: 16, 319: 17, 320: 18, 321: 19, 322: 20, 323: 21, 324: 22, 325: 23, 326: 24, 327: 25, 328: 26, 329: 27, 331: 28, 332: 29, 333: 30, 334: 31, 335: 32, 501: 33, 502: 34, 503: 35, 504: 36, 505: 37, 506: 38, 507: 39, 508: 40, 509: 41, 510: 42, 511: 43, 512: 44, 513: 45, 533: 46, 514: 47, 515: 48, 516: 49, 517: 50, 518: 51, 519: 52, 520: 53, 521: 54, 522: 55, 523: 56, 524: 57, 525: 58, 526: 59, 527: 60, 528: 61, 529: 62, 530: 63, 531: 64, 532: 65, 999: 66}
    # DICCIONARIO CON LAS PRODUCCIONES DE LA GRAMATICA, CON CLAVE: NUMERO DE PRODUCCION, VALOR: PRODUCCION
    productions = {
        1: 'PRINCIPAL FUNCIONES SECCION_VARIABLES',
        2: '{ < main > } BLOQUE',
        3: '{ ESTATUTOS }',
        4: 'def identificador ( : PARAMETROS : ) BLOQUE RETURN FUNCIONES_PRIMA',
        5: 'FUNCIONES',
        6: '',
        7: 'TIPO identificador PARAMETROS_PRIMA',
        8: '',
        9: ', PARAMETROS',
        10: '',
        11: 'return LISTA_VARIABLES',
        12: '',
        13: 'numerical',
        14: 'dec',
        15: 'string',
        16: 'logic',
        17: 'list',
        18: '{ : vars : DECLARACION_VARIABLES }',
        19: 'LISTA_VARIABLES : TIPO DECLARACION_VARIABLES_PRIMA',
        20: 'DECLARACION_VARIABLES',
        21: '',
        22: 'identificador LISTA_VARIABLES_PRIMA',
        23: ', LISTA_VARIABLES',
        24: '',
        25: 'ESTATUTO ESTATUTOS',
        26: '',
        27: 'ESTATUTO_CYCLEWHILE',
        28: 'ESTATUTO_CYCLEFOR',
        29: 'ESTATUTO_CYCLEREPEAT',
        30: 'ASIGNACION',
        31: 'ESTATUTO_CYCLEDO',
        32: 'FUNCION_BUILT_IN',
        33: 'ESTATUTO_IF',
        34: 'identificador ASIGNACION_PRIMA',
        35: ':=:: EXP',
        36: '<- [[ LISTA_ELEMENTO ]]',
        37: 'longitud ( identificador )',
        38: 'esnumero ( identificador )',
        39: 'esdecimal ( identificador )',
        40: 'entero ( identificador )',
        41: 'decimal ( identificador )',
        42: 'lectura ( )',
        43: 'absoluto ( EXP )',
        44: 'cadena ( EXP )',
        45: 'potencia ( EXP )',
        46: 'redondear ( EXP )',
        47: 'sumando ( identificador )',
        48: 'minimo ( identificador )',
        49: 'maximo ( identificador )',
        50: 'imprimir ( IMPRESION )',
        51: 'numero LISTA_ELEMENTO_PRIMA',
        52: ', LISTA_ELEMENTO',
        53: '',
        54: 'numero IMPRESION_PRIMA',
        55: 'texto IMPRESION_PRIMA',
        56: ', IMPRESION',
        57: '',
        58: 'ifwhether CONDICION BLOQUE ELIF',
        59: 'in RANGE',
        60: 'EXPB',
        61: 'true',
        62: 'when CONDICION BLOQUE',
        63: 'since FOR_PRIMA',
        64: 'identificador in RANGE BLOQUE',
        65: '( identificador = EXP , EXPB , INCREMENTO ) BLOQUE',
        66: 'identificador ++',
        67: 'repeat BLOQUE CONDICION',
        68: 'do BLOQUE CONDICION',
        69: 'elif EXPB BLOQUE ELIF',
        70: 'else BLOQUE',
        71: '',
        72: 'range ( START , STOP , STEP )',
        73: 'numero',
        74: '',
        75: 'numero',
        76: 'numero',
        77: '',
        78: 'TERMB EXPB_PRIMA',
        79: '&& TERMB EXPB_PRIMA',
        80: '|| TERMB EXPB_PRIMA',
        81: '',
        82: 'EXP TERMB_PRIMA',
        83: 'OPER EXP TERMB_PRIMA',
        84: '',
        85: 'TERM EXP_PRIMA',
        86: '+ TERM EXP_PRIMA',
        87: '- TERM EXP_PRIMA',
        88: '',
        89: 'FACTOR TERM_PRIMA',
        90: '* FACTOR TERM_PRIMA',
        91: '/ FACTOR TERM_PRIMA',
        92: '',
        93: 'identificador FUNCT',
        94: '( EXPB )',
        95: '( PARAMETROS )',
        96: '',
        97: '>!!>',
        98: '<!!<',
        99: '>>!!=',
        100: '<<!!=',
        101: '=!!=',
    }
    # DICIONARIO CON TODOS LOS SIMBOLOS TERMINALES PARA LA CONVERSION DE SIMBOLO NO TERMINAL A NUMERO DE TOKEN, IMPORTANTE CADA SIMBOLO TERMINAL ESTA SEPARADO POR UN ESPACIO
    all_tokens = { '{': 301, '}': 302, '(': 303, ')': 304, ',': 305, '=': 306, '=!!=': 307, ':': 308, ':=::': 310, '-': 311, '[[': 312, ']]': 313, '&&': 314, '||': 315, '+': 316, '++': 317, '*': 318, '/': 319, 'COMENTARIO': 320, '!': 321, '<': 322, '<-': 323, '<<!!=': 324, '<!!<': 325, '>': 326, '>>!!=': 327, '>!!>': 328, 'identificador': 329, 'numero': 331, "numerond": 332, "numeroreal": 333, "numerorend": 334, 'texto': 335, 'absoluto': 501, 'cadena': 502, 'dec': 503, 'decimal': 504, 'def': 505, 'do': 506, 'elif': 507, 'else': 508, 'entero': 509, 'esdecimal': 510, 'esnumero': 511, 'in': 512, 'ifwhether': 513, 'lectura': 514, 'list': 515, 'logic': 516, 'longitud': 517, 'main': 518, 'maximo': 519, 'minimo': 520, 'numerical': 521, 'potencia': 522, 'range': 523, 'redondear': 524, 'repeat': 525, 'return': 526, 'string': 527, 'sumando': 528, 'true': 529, 'vars': 530, 'when': 531, 'since': 532, 'imprimir': 533, 'EOF': 999,
    }
    # VALOR DADO AL ERROR
    E:int = 888
    # MATRIZ SINTACTICA
    matriz_sintactica = [
[1,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[2,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[3,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,4,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[6,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,5,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,8,E,E,E,8,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,7,E,E,E,E,E,E,E,E,E,E,E,E,7,7,E,E,E,E,7,E,E,E,E,E,7,E,E,E,E,E,E,],
[E,E,E,10,9,E,E,10,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[12,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,12,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,11,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,14,E,E,E,E,E,E,E,E,E,E,E,E,17,16,E,E,E,E,13,E,E,E,E,E,15,E,E,E,E,E,E,],
[18,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,19,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,21,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,20,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,22,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[24,E,E,E,23,E,E,24,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,24,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,26,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,25,E,E,E,E,E,25,25,E,25,E,25,E,E,25,25,25,E,25,25,25,E,E,25,E,25,25,E,25,E,25,25,E,E,25,E,E,25,25,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,30,E,E,E,E,E,32,32,E,32,E,31,E,E,32,32,32,E,33,32,32,E,E,32,E,32,32,E,32,E,32,29,E,E,32,E,E,27,28,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,34,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,35,E,E,E,E,E,E,E,E,E,0,E,E,36,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,43,44,E,41,E,E,E,E,40,39,38,E,E,50,42,E,E,37,E,49,48,E,45,E,46,E,E,E,47,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,51,51,51,51,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,52,E,E,E,E,E,E,53,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,54,54,54,54,55,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,57,56,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,58,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,60,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,60,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,59,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,61,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,62,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,63,E,],
[E,E,65,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,64,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,66,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,67,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,68,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,71,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,71,E,E,E,E,E,71,71,E,71,E,71,69,70,71,71,71,E,71,71,71,E,E,71,E,71,71,E,71,E,71,71,E,E,71,E,E,71,71,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,72,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,74,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,73,73,73,73,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,75,75,75,75,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,E,77,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,E,76,76,76,76,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[E,E,78,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,78,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[81,81,E,81,81,E,E,E,E,E,E,E,79,80,E,E,E,E,0,E,E,E,E,E,E,E,E,81,E,E,E,E,E,81,81,E,81,E,81,E,E,81,81,81,E,81,81,81,E,E,81,E,81,81,E,81,E,81,81,E,E,81,E,E,81,81,E,],
[E,E,82,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,82,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[84,84,E,84,84,E,83,E,E,E,E,E,84,84,E,E,E,E,0,E,E,E,83,83,E,83,83,84,E,E,E,E,E,84,84,E,84,E,84,E,E,84,84,84,E,84,84,84,E,E,84,E,84,84,E,84,E,84,84,E,E,84,E,E,84,84,E,],
[E,E,85,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,85,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[88,88,E,88,88,E,88,E,E,87,E,E,88,88,86,E,E,E,0,E,E,E,88,88,E,88,88,88,E,E,E,E,E,88,88,E,88,E,88,E,E,88,88,88,E,88,88,88,E,E,88,E,88,88,E,88,E,88,88,E,E,88,E,E,88,88,E,],
[E,E,89,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,89,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[92,92,E,92,92,E,92,E,E,92,E,E,92,92,92,E,90,91,0,E,E,E,92,92,E,92,92,92,E,E,E,E,E,92,92,E,92,E,92,E,E,92,92,92,E,92,92,92,E,E,92,E,92,92,E,92,E,92,92,E,E,92,E,E,92,92,E,],
[E,E,94,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,E,E,E,E,E,93,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],
[96,96,95,96,96,E,96,E,E,96,E,E,96,96,96,E,96,96,0,E,E,E,96,96,E,96,96,96,E,E,E,E,E,96,96,E,96,E,96,E,E,96,96,96,E,96,96,96,E,E,96,E,96,96,E,96,E,96,96,E,E,96,E,E,96,96,E,],
[E,E,E,E,E,E,101,E,E,E,E,E,E,E,E,E,E,E,0,E,E,E,100,98,E,99,97,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,],

    ]

    # FUNCION PARA OBTENER EL NUMERO DE COLUMNA MEDIANTE EL NUMERO DE TOKEN DEL SIMBOLO TERMINAL
    def get_column(self, token):
        if token in self.token_to_column:
            return self.token_to_column[token]
        else:
            return 888

    # FUNCION PARA OBTENER EL NUMERO DE FILA MEDIANTE EL SIMBOLO NO TERMINAL
    def get_row(self, non_terminal):
        if non_terminal in self.prod_to_row:
            return self.prod_to_row[non_terminal]
        else:
            return 888

    # NOTA: EN LAS 3 FUNCIONES ANTERIORES EN CASO DE NO ENCONTRAR LO QUE DEBE RETORNAR, ENTONCES RETORNARA ERROR (888)

    # FUNCION PARA OBTENER EL NUMERO DE PRODUCCION QUE UTILIZAREMOS USANDO EL NUMERO DE PRODUCCION Y AGREGANDOLO A LA LISTA SINTACTICA
    def get_prod(self, num_prod, syntactic_l):
        if num_prod in self.productions:
            # OBTENEMOS LA PRODUCCION Y LA DIVIDIMOS EN UNA LISTA MEDIANTE LOS ESPACIOS QUE TENGA LA CADENA
            to_convert = self.productions[num_prod].split()
            if to_convert == []:
                # SI ES PRODUCCION NULA
                print(
                    self.WARNING, "PRODUCCION NULA, NO SE AGREGARÁ NADA A LA LISTA", self.RESET)
            else:
                print(self.WARNING, "PRODUCCION: ", num_prod, " : ",
                      to_convert)  # SI NO MOSTRAMOS EL NUMERO DE PRODUCCION JUNTO CON LO QUE SE AÑADIRA A LA LISTA
                to_convert.reverse()  # INVERTIMOS EL ORDEN DE LA LISTA
                print('SE EXTENDERA LA LISTA CON: ', to_convert, self.RESET)

            tokens = []  # LISTA PARA LA CONVERSIÓN DE SIMBOLO NO TERMINAL A NUMERO DE TOKEN
            for convert in to_convert:
                if convert in self.all_tokens:
                    # SI LO QUE ESTA EN EL INDICE DE to_convert ESTA EN LA LISTA DE TODOS LOS TOKENS ENTONCES SE HARA LA CONVERSION Y AÑADIREMOS EL NUMERO DE TOKEN
                    tokens.append(self.all_tokens[convert])
                else:
                    # SI NO SE ENCUENTRA ENTONCES SE AÑADE EL SIMBOLO TAL CUAL
                    tokens.append(convert)

            # LA LISTA DE COMPARACION ENTONCES SE JUNTARA CON LA LISTA TOKENS
            syntactic_l.extend(tokens)
            return syntactic_l

        else:
            # EN CASO DE QUE EL NUMERO DE PRODUCCION NO SE ENCUENTRE EN EL DICCIONARIO DE PRODUCCIONES SE AÑADIRA ERROR (888)
            syntactic_l.extend([888])
            return syntactic_l

    def expected_token(self, num_row, matriz_sintactica):
        counter = 0  # NUMERO DE COLUMNA A BUSCAR
        columns = []  # COLUMNAS QUE NO SEAN ERRORES
        for token in matriz_sintactica[num_row]:
            if token != 888:
                # SI LA POSICION ENTRE EL NUMERO DE FILA Y EL NUMERO DE COLUMNA NO ES 888 ENTONCES SE AÑADIRA EL NUMERO DE COLUMNA
                columns.append(counter)
            counter += 1  # SE AUMENTA EL NUMERO DE COLUMNA A BUSCAR
        return columns

    def analisis_codigo(self, matriz_sintactica, token_l):
        # INICIALIZAMOS LA LISTA SINTACTICA EN ESTE CASO P LLAMARIA A LA PRODUCCION 1 (PRINCIPAL FUNCIONES SECCION_VARIABLES)
        syntactic_l = [999, "P"]
        with open('syntactic_log.txt', 'w') as archivo_salida:
            while token_l != []: # LA EJECUCION PASARA HASTA QUE LA LISTA DE TOKENS SEA UNA LISTA VACIA
                if syntactic_l[-1] == token_l[0]: # SI EL ULTIMO ELEMENTO DE LA LISTA SINTACTICA ES IGUAL AL PRIMER ELEMENTO DE LA LISTA DE TOKENS
                    print(self.WARNING, "SIMBOLO TERMINAL A ELIMINAR:",
                        token_l[0], self.RESET, "\n") #MOSTRARA EL NUMERO DE TOKEN QUE SE ELIMINARA DE LA LISTA SINTACTICA
                    archivo_salida.write(f"SE ELIMINO: {token_l[0]}\n")
                    syntactic_l.pop()
                    token_l.pop(0) # SE ELIMINA DE AMBAS LISTAS DEL ULTIMO ELEMENTO DE LA LISTA SINTACTICA Y DEL PRIMERO DE LA LISTA DE TOKENS
                    print('LISTA SINTACTICA => ', syntactic_l)
                    print("LISTA DE TOKENS => ", token_l)
                    archivo_salida.write(f"{syntactic_l} => {token_l} \n")

                else: #SI NO SE BUSCARA EL NUMERO DE PRODUCCION SACANDO EL NUMERO DE FILA Y COLUMNA PARA DAR CON LA COORDENADA EXACTA
                    col = token_l[0]
                    columna = self.get_column(col)
                    row = syntactic_l[-1]
                    fila = self.get_row(row)
                    
                    num_prod = matriz_sintactica[fila][columna] # NUMERO DE PRODUCCION ENCONTRADO ENTRE LA LISTA SINTACTICA
                    archivo_salida.write(f"SE AGREGO LA PRODUCCION {num_prod}\n")
                    if num_prod == 0: # SI EL NUMERO DE PRODUCCION ES 0 ENTONCES ENCONTRO UN COMENTARIO, SOLO SE ELIMINARA DE LA LISTA DE TOKENS
                        print(self.PURPLE, "COMENTARIO ENCONTRADO", self.RESET, "\n")
                        archivo_salida.write("SE ENCONTRO UN COMENTARIO\n")
                        token_l.pop(0)

                    else:
                        syntactic_l.pop() # EN CASO CONTRARIO SE ELIMINARA DE LA LISTA SINTACTICA
                        syntactic_l = self.get_prod(
                            num_prod, syntactic_l) #BUSCARA LA PRODUCCION Y RETORNARA LA LISTA SINTACTICA JUNTO CON LA PRODUCCION ENCONTRADA
                        print(
                            self.ALERT, "NUEVA LISTA SINTACTICA => ", syntactic_l, "\n")
                        archivo_salida.write(f"LA LISTA SINTACTICA CAMBIO A => {syntactic_l} \n\n")
                        if syntactic_l[-1] == 888:
                            expected = self.expected_token(
                                fila, matriz_sintactica)
                            print(
                                self.FAIL, "ERROR DE SINTAXIS: REVISAR TABLA SINTACTICA PARA VER LO ESPERADO: NUM. FILA: ", fila, " COLUMNAS: ", expected, self.RESET) #SI HAY UN ERROR NOS MOSTRARA LA FILA EN LA CUAL ESTARA EL ERROR Y LOS NUMEROS DE COLUMNA QUE ESPERABA
                            archivo_salida.write(f"ERROR DE SINTAXIS: NUM. FILA: {fila} COLUMNAS: {expected}\n")
                            break

            if (token_l == []):
                archivo_salida.write("----FIN DE ARCHIVO----")
                print(
                    self.OK, "ANALISIS FINALIZADO", self.RESET) # SI SE LLEGA A LISTA VACIA ENTONCES MUESTRA EL ANALISIS FINALIZADO


analizador_lexico = lexico()
codigo_fuente = analizador_lexico.read_code()  # Lee el codigo fuente
tokens = analizador_lexico.analisis_codigo(
    codigo_fuente, analizador_lexico.matriz_estados)
print()
print('NUMERO DE TOKENS: ', len(tokens))
with open(analizador_lexico.ruta_salida, 'w') as archivo_salida:
    for i in tokens:
        for llave, valor in analizador_lexico.palabras_reservadas.items():
            if valor == i:
                print(i, ' : ', llave)
                archivo_salida.write(f"{i}\n")
        if i in analizador_lexico.diccionario_completo:
            print(i, ' : ', analizador_lexico.diccionario_completo[i])
            archivo_salida.write(
                f"{i}\n")
        if i in analizador_lexico.diccionario_errores:
            print('ERROR: ', i, ' : ',
                  analizador_lexico.diccionario_errores[i])
            archivo_salida.write(
                f"ERROR: {i} : {analizador_lexico.diccionario_errores[i]}\n")
            break

sintactico = sintactico()
sintactico.analisis_codigo(sintactico.matriz_sintactica, tokens)
