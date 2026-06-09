import pulp



model = pulp.LpProblem(
    "Optimizacion_Almacenamiento_Cloud",
    pulp.LpMinimize
)




x1 = pulp.LpVariable(
    "Almacenamiento_Estandar",
    lowBound=0,
    cat='Continuous'
)

x2 = pulp.LpVariable(
    "Almacenamiento_Premium",
    lowBound=0,
    cat='Continuous'
)



model += 20 * x1 + 60 * x2, "Costo_Total"



model += 1 * x1 + 3 * x2 >= 15, "Velocidad_IOPS"



model += 2 * x1 + 2 * x2 >= 14, "Retencion_Datos"



model.solve()



print("Estado de la solución:")
print(pulp.LpStatus[model.status])

print("\nCantidad óptima de almacenamiento:")

print(
    "Almacenamiento Estándar =",
    round(x1.varValue, 2),
    "TB"
)

print(
    "Almacenamiento Premium =",
    round(x2.varValue, 2),
    "TB"
)

print("\nCosto mínimo mensual:")

print(
    "$",
    round(pulp.value(model.objective), 2),
    "USD"
)



print("\nValidación de restricciones:")

print(
    "Velocidad total =",
    round(1 * x1.varValue + 3 * x2.varValue, 2),
    "unidades"
)

print(
    "Retención total =",
    round(2 * x1.varValue + 2 * x2.varValue, 2),
    "días"
)