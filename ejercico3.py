import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Firewall_Optimization", pulp.LpMaximize)

# 2. Variables de decisión
x1 = pulp.LpVariable("Inspeccion_Basica", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Inspeccion_Profunda", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "Seguridad_Total"

# 4. Restricciones
model += x1 + 3 * x2 <= 18, "CPU"
model += x1 + x2 <= 8, "RAM"

# 5. Resolver
model.solve()

# 6. Resultados
print("Estado:", pulp.LpStatus[model.status])
print("Inspección Básica:", x1.varValue)
print("Inspección Profunda:", x2.varValue)
print("Puntos Totales de Seguridad:", pulp.value(model.objective))