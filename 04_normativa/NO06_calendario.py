#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_normativa/NO06_calendario.py
Análisis del Calendario de Obligaciones Periódicas del PETI
SI-886 · Planeamiento Estratégico de TI · Semana 08
Organización: CrediTech Perú S.A.C.
Autor: Fabricio Ramos (2023076798)
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    csv_path = os.path.join(os.path.dirname(__file__), "NO05_calendario.csv")
    if not os.path.exists(csv_path):
        csv_path = "NO05_calendario.csv"

    c = pd.read_csv(csv_path)

    salida_lineas = []
    def log(msg=""):
        print(msg)
        salida_lineas.append(msg)

    log("=" * 80)
    log("  CALENDARIO DE OBLIGACIONES PERIÓDICAS — PETI v0.8")
    log("  ORGANIZACIÓN: CrediTech Perú S.A.C. | RUC: 20608945123")
    log("=" * 80)
    log()
    log("--- DISTRIBUCIÓN POR PERIODICIDAD ---")
    log(c.groupby("Periodicidad").size().to_string())
    log(f"\nObligaciones periódicas: {len(c)}")
    log(f"Sin responsable asignado: {c.Responsable.isna().sum()}")
    log("\n→ Este calendario se incorpora a la sección 10 Supervisión: son los hitos")
    log("  de cumplimiento que el tablero del plan debe monitorear.")
    log()
    log("--- DETALLE DE OBLIGACIONES PERIÓDICAS Y PRÓXIMOS VENCIMIENTOS ---")
    for _, row in c.iterrows():
        log(f"[{row['id']}] {row['Obligación periódica']}")
        log(f"     Norma: {row['Norma']} | Periodicidad: {row['Periodicidad']} | Vence: {row['Próximo vencimiento']}")
        log(f"     Responsable: {row['Responsable']} | Evidencia: {row['Evidencia que se genera']}\n")
    log("=" * 80)

    # Guardar en archivo de evidencias
    salidas_dir = os.path.join(os.path.dirname(__file__), "..", "docs", "evidencias", "S08", "salidas")
    os.makedirs(salidas_dir, exist_ok=True)
    out_file = os.path.join(salidas_dir, "salida_calendario.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(salida_lineas) + "\n")
    print(f"\n[OK] Salida textual guardada en: {out_file}")

    # Generar gráfico de distribución por periodicidad
    graficos_dir = os.path.join(os.path.dirname(__file__), "..", "graficos")
    os.makedirs(graficos_dir, exist_ok=True)
    
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(9, 5))
    
    period_counts = c["Periodicidad"].value_counts()
    colores_period = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars = ax.bar(period_counts.index, period_counts.values, color=colores_period[:len(period_counts)], edgecolor='#333', width=0.5)
    
    ax.set_title('Distribución de Obligaciones Periódicas por Frecuencia Temporal', fontsize=12, fontweight='bold', pad=12)
    ax.set_ylabel('Número de Obligaciones', fontsize=10)
    ax.set_xlabel('Periodicidad', fontsize=10)
    ax.set_ylim(0, max(period_counts.values) + 1.5)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f"{yval}", ha='center', va='bottom', fontsize=11, fontweight='bold')
        
    plt.tight_layout()
    chart_path = os.path.join(graficos_dir, "NO_calendario_periodicidad.png")
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico de calendario guardado en: {chart_path}")

if __name__ == "__main__":
    main()
