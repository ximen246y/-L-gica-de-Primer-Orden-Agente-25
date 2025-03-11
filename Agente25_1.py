from pyDatalog import pyDatalog


pyDatalog.clear()

# Definir términos y predicados
pyDatalog.create_terms('Eliminar, Mantener, Fusionar, Reformular, Frase, EsSimilar, EsRedundante, X')

# Definir frases que deben mantenerse
+Mantener('frase importante')
+Mantener('dato relevante')

# Definir frases generales
+Frase('frase importante')
+Frase('dato relevante')
+Frase('información irrelevante')
+Frase('texto sin valor')
+Frase('comentario innecesario')
+Frase('oración repetitiva')
+Frase('oración casi idéntica')
+Frase('explicación larga innecesaria')

# Definir frases similares que pueden fusionarse
+EsSimilar('oración repetitiva', 'oración casi idéntica')

# Definir frases redundantes que pueden reformularse
+EsRedundante('explicación larga innecesaria')

# Definir la regla para eliminar frases irrelevantes
Eliminar(Frase) <= (Frase(Frase) & ~Mantener(Frase))

# Definir la regla para fusionar frases similares
Fusionar(Frase) <= EsSimilar(Frase, X)

# Definir la regla para reformular frases redundantes
Reformular(Frase) <= EsRedundante(Frase)

# Consultas

print("\nFrases eliminadas (las que NO están en Mantener):")
print("----------------------------------")
for f in Eliminar(Frase):
    print(f[0])

print("\nFusión de frases similares:")
print("----------------------------------")
for f in Fusionar(Frase):
    print(f[0])

print("\nReformulación de frases redundantes:")
print("----------------------------------")
for f in Reformular(Frase):
    print(f[0])
