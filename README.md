# SI-886 · Planeamiento Estratégico de TI
## Taller de Laboratorio 08: Matriz de Cumplimiento Normativo del PETI

**Autor:** Ramos Atahuachi, Fabricio Farid Edmilson (Código: 2023076798)  
**Docente:** Dr. Oscar Juan Jimenez Flores  
**Universidad Privada de Tacna · Escuela Profesional de Ingeniería de Sistemas**  
**Versión / Tags:** `taller-08` · `v0.8`

---

### Estructura del Repositorio

```
SI886-S08-TALLER-RamosFabricio/
├── INFORME-TALLER-S08.md              # Informe formal académico del taller (Secciones 1 a 6)
├── 3-TALLER.md                       # Guía de laboratorio oficial del taller
├── 04_normativa/
│   ├── NO01_marco_aplicable.md       # Determinación del marco aplicable y árbol de decisión
│   ├── NO02_normas_aplicables.csv    # Tabla de normas aplicables y descartadas con fundamento
│   ├── NO03_matriz_cumplimiento.csv  # Matriz de cumplimiento normativo (26 obligaciones)
│   ├── NO04_analisis_cumplimiento.py # Script en Python para cálculo de métricas y gráficos
│   ├── NO05_calendario.csv           # Calendario de obligaciones periódicas (10 hitos)
│   ├── NO06_calendario.py            # Script en Python para análisis del calendario
│   └── 4.1_marco_normativo.md        # Sección 4.1 completa del PETI
├── docs/
│   └── evidencias/S08/salidas/
│       ├── salida_analisis_cumplimiento.txt # Salida oficial de ejecución del análisis
│       └── salida_calendario.txt            # Salida oficial del calendario
└── graficos/
    ├── NO_cumplimiento_resumen.png     # Gráfico de barras y torta del estado de cumplimiento
    ├── NO_distribucion_normas.png      # Gráfico de cumplimiento por norma y autoridad
    └── NO_calendario_periodicidad.png  # Gráfico de frecuencia de obligaciones periódicas
```

---

### Ejecución de Scripts

#### 1. Análisis Cuantitativo de Cumplimiento Normativo
```bash
python 04_normativa/NO04_analisis_cumplimiento.py
```
El script procesa `NO03_matriz_cumplimiento.csv`, calcula frecuencias y porcentajes por estado (Cumple, Parcial, No cumple), detecta obligaciones sin responsable asignado, extrae los proyectos no negociables con su plazo normativo más exigente y genera los gráficos en `graficos/`.

#### 2. Análisis del Calendario de Obligaciones Periódicas
```bash
python 04_normativa/NO06_calendario.py
```
El script analiza `NO05_calendario.csv`, agrupa las obligaciones por periodicidad (Anual, Semestral, Trimestral, Mensual), valida la asignación de responsables y genera el gráfico de distribución temporal en `graficos/`.