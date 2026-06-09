import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("VideoGame_Assets_Optimization", pulp.LpMaximize)

# 2. Variables de decisión
# x1 = Modelos 3D de Personajes
# x2 = Modelos 3D de Escenarios

x1 = pulp.LpVariable("Personajes", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Escenarios", lowBound=0, cat='Integer')

# 3. Función Objetivo
# Maximizar el valor total del proyecto

model += 80 * x1 + 60 * x2, "Valor_Total"

# 4. Restricciones

# Tiempo máximo de renderizado (GPU)
model += 2 * x1 + x2 <= 12, "Renderizado"

# Memoria máxima disponible (VRAM)
model += x1 + 2 * x2 <= 14, "VRAM"

# 5. Resolver
model.solve()

# 6. Resultados
print("Estado:", pulp.LpStatus[model.status])
print("Personajes:", x1.varValue)
print("Escenarios:", x2.varValue)
print("Valor Total del Proyecto: $", pulp.value(model.objective), "USD")