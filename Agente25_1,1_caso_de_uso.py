from pyDatalog import pyDatalog
import re


pyDatalog.clear()

# Definir términos y predicados
pyDatalog.create_terms('Eliminar, Mantener, Fusionar, Reformular, Frase, EsSimilar, EsRedundante, ResumenFinal, X, Y')

# Caso de Uso: Generación de Resúmenes Automáticos
# Escenario: Un investigador sube un artículo académico y el agente extrae frases clave,
# elimina información irrelevante y genera un resumen coherente.

# Texto de entrada (Ejemplo de artículo científico)
texto = """
El cambio climático es una de las problemáticas más relevantes de la actualidad. 
Investigaciones recientes han demostrado un aumento en la temperatura global de 1.2°C en comparación con la era preindustrial. 
Esto ha generado impactos significativos en los ecosistemas, afectando la biodiversidad y provocando fenómenos climáticos extremos. 
Los gobiernos y organizaciones internacionales han implementado diversas estrategias para mitigar estos efectos, incluyendo la reducción de emisiones de CO2, 
el uso de energías renovables y la reforestación. Sin embargo, algunos sectores económicos aún dependen de combustibles fósiles, lo que dificulta la transición energética.
"""

# Dividir el texto en frases
frases = [f.strip() for f in re.split(r'\. ', texto.strip())]

# Definir las frases como hechos
for f in frases:
    +Frase(f)

# Definir frases que deben mantenerse (frases clave del resumen)
+Mantener('Investigaciones recientes han demostrado un aumento en la temperatura global de 1.2°C')
+Mantener('Esto ha generado impactos significativos en los ecosistemas, afectando la biodiversidad y provocando fenómenos climáticos extremos')
+Mantener('Los gobiernos han implementado estrategias para mitigar estos efectos, incluyendo la reducción de emisiones de CO2 y el uso de energías renovables')

# Definir frases similares que pueden fusionarse
+EsSimilar('Investigaciones recientes han demostrado un aumento en la temperatura global de 1.2°C', 'El cambio climático es una de las problemáticas más relevantes de la actualidad')

# Definir frases redundantes que pueden reformularse
+EsRedundante('Sin embargo, algunos sectores económicos aún dependen de combustibles fósiles, lo que dificulta la transición energética')

# Definir la regla para eliminar frases irrelevantes
Eliminar(Frase) <= (Frase(Frase) & ~Mantener(Frase))

# Definir la regla para fusionar frases similares
Fusionar(X) <= EsSimilar(X, Y)
Fusionar(Y) <= EsSimilar(X, Y)

# Definir la regla para reformular frases redundantes
Reformular(Frase) <= EsRedundante(Frase)

# Generar el resumen final con frases clave
ResumenFinal(Frase) <= Mantener(Frase)


def imprimir_lista(titulo, consulta):
    resultados = list(consulta)
    if resultados:
        print(f"\n{titulo}:")
        print("-" * 40)
        for f in resultados:
            print(f[0].strip())  

# Consultas 
imprimir_lista("Frases eliminadas (las que NO están en Mantener)", Eliminar(Frase))
imprimir_lista("Fusión de frases similares", Fusionar(Frase))
imprimir_lista("Reformulación de frases redundantes", Reformular(Frase))
imprimir_lista("Resumen Final Generado", ResumenFinal(Frase))
