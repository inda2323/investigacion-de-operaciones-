import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Storage_Optimization", pulp.LpMinimize)

# 2. Variables de decisión
# x1 = TB de almacenamiento estándar
# x2 = TB de almacenamiento premium

x1 = pulp.LpVariable("Almacenamiento_Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Almacenamiento_Premium", lowBound=0, cat='Integer')

# 3. Función Objetivo
# Minimizar el costo mensual

model += 20 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones

# Velocidad mínima requerida (IOPS)
model += x1 + 3 * x2 >= 15, "Velocidad"

# Retención mínima requerida
model += 2 * x1 + 2 * x2 >= 14, "Retencion"

# 5. Resolver
model.solve()

# 6. Resultados
print("Estado:", pulp.LpStatus[model.status])
print("Almacenamiento Estándar:", x1.varValue, "TB")
print("Almacenamiento Premium:", x2.varValue, "TB")
print("Costo Total Mensual: $", pulp.value(model.objective), "USD")