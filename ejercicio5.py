import pulp



model = pulp.LpProblem(
    "Optimizacion_Cluster_DevOps",
    pulp.LpMaximize
)


x1 = pulp.LpVariable(
    "Backend",
    lowBound=0,
    upBound=6,     
    cat='Integer'
)

x2 = pulp.LpVariable(
    "Data_Worker",
    lowBound=0,
    upBound=7,     
    cat='Integer'
)


model += 300 * x1 + 250 * x2, "Rendimiento_Total"


model += 2 * x1 + 1 * x2 <= 16, "Memoria_RAM"

model += 1 * x1 + 2 * x2 <= 17, "Almacenamiento_SSD"

model += x1 <= 6, "Limite_Backend"

model += x2 <= 7, "Limite_Data_Workers"
model.solve()



print("Estado de la solución:")
print(pulp.LpStatus[model.status])

print("\nCantidad óptima de contenedores:")
print("Backend =", int(x1.varValue))
print("Data Worker =", int(x2.varValue))

print("\nRendimiento máximo por hora:")
print("$", pulp.value(model.objective), "USD")



print("\nUso de recursos:")

print(
    "RAM utilizada =",
    2 * x1.varValue + 1 * x2.varValue,
    "GB de 16 GB"
)

print(
    "SSD utilizado =",
    1 * x1.varValue + 2 * x2.varValue,
    "TB de 17 TB"
)