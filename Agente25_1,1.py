from pyDatalog import pyDatalog
import re

# Limpiar reglas previas
pyDatalog.clear()

# Definir términos y predicados
pyDatalog.create_terms('Eliminar, Mantener, Fusionar, Reformular, Frase, EsSimilar, EsRedundante, X, Y')

# Texto de entrada
texto = """
Esta es una frase importante. Este es un dato relevante. Sin embargo, esta información no es necesaria. 
Un texto sin valor agregado. Este comentario no aporta nada. Una oración repetitiva. Una oración casi idéntica. 
Además, esta explicación es larga e innecesaria. Otra explicación extensa sin relevancia. Un comentario irrelevante.
Una frase redundante que no aporta mucho. Otra frase redundante que es innecesaria.
"""

# Dividir el texto en frases
frases = re.split(r'\. ', texto.strip())  

# Definir las frases como hechos
for f in frases:
    +Frase(f)

# Definir frases que deben mantenerse
+Mantener('Esta es una frase importante')
+Mantener('Este es un dato relevante')

# Definir frases similares que pueden fusionarse
+EsSimilar('Una oración repetitiva', 'Una oración casi idéntica')
+EsSimilar('Una frase redundante que no aporta mucho', 'Otra frase redundante que es innecesaria')

# Definir frases redundantes que pueden reformularse
+EsRedundante('Además, esta explicación es larga e innecesaria')
+EsRedundante('Otra explicación extensa sin relevancia')
+EsRedundante('Un comentario irrelevante')

# Definir la regla para eliminar frases irrelevantes
Eliminar(Frase) <= (Frase(Frase) & ~Mantener(Frase))

# Definir la regla para fusionar frases similares
Fusionar(X) <= EsSimilar(X, Y)
Fusionar(Y) <= EsSimilar(X, Y)

# Definir la regla para reformular frases redundantes
Reformular(Frase) <= EsRedundante(Frase)

# Consultas
print("\n-Frases eliminadas (las que NO están en Mantener):")
print("----------------------------------")
for f in Eliminar(Frase):
    print(f[0])

print("\n-Fusión de frases similares:")
print("----------------------------------")
for f in Fusionar(Frase):
    print(f[0])

print("\n-Reformulación de frases redundantes:")
print("----------------------------------")
for f in Reformular(Frase):
    print(f[0])
