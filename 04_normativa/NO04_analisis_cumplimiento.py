#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_normativa/NO04_analisis_cumplimiento.py
Análisis cuantitativo de la Matriz de Cumplimiento Normativo del PETI
SI-886 · Planeamiento Estratégico de TI · Semana 08
Organización: CrediTech Perú S.A.C.
Autor: Fabricio Ramos (2023076798)
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Asegurar codificación utf-8
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    csv_path = os.path.join(os.path.dirname(__file__), "NO03_matriz_cumplimiento.csv")
    if not os.path.exists(csv_path):
        print(f"Error: no se encontró {csv_path}")
        return

    df = pd.read_csv(csv_path)
    total_obligaciones = len(df)

    salida_lineas = []
    def log(msg=""):
        print(msg)
        salida_lineas.append(msg)

    log("=" * 80)
    log("  REPORTE DE CUMPLIMIENTO NORMATIVO Y GOBERNANZA TECNOLÓGICA — PETI v0.8")
    log("  ORGANIZACIÓN: CrediTech Perú S.A.C. | RUC: 20608945123")
    log("=" * 80)
    log()

    # 1. Resumen cuantitativo por Estado
    estado_counts = df["Estado"].value_counts()
    estado_pct = (df["Estado"].value_counts(normalize=True) * 100).round(1)
    resumen_df = pd.DataFrame({"Cantidad": estado_counts, "Porcentaje (%)": estado_pct})
    
    log("--- 1. RESUMEN CUANTITATIVO DEL ESTADO DE CUMPLIMIENTO ---")
    log(resumen_df.to_string())
    log(f"\nTotal de obligaciones evaluadas: {total_obligaciones}")
    
    pct_cumple = estado_pct.get("Cumple", 0.0)
    pct_parcial = estado_pct.get("Parcial", 0.0)
    pct_nocumple = estado_pct.get("No cumple", 0.0)
    
    log(f"  • Cumplimiento total   : {estado_counts.get('Cumple', 0)} ({pct_cumple}%)")
    log(f"  • Cumplimiento parcial : {estado_counts.get('Parcial', 0)} ({pct_parcial}%)")
    log(f"  • Incumplimiento total : {estado_counts.get('No cumple', 0)} ({pct_nocumple}%)")
    log(f"  --> Brecha de riesgo legal/regulatorio: {round(pct_parcial + pct_nocumple, 1)}% de las obligaciones requieren intervención.")
    log()

    # 2. Obligaciones sin responsable asignado
    sin_resp = df[df["Área responsable"].isna() | (df["Área responsable"].str.strip() == "")]
    num_sin_resp = len(sin_resp)
    
    log("--- 2. DETECCIÓN DE OBLIGACIONES SIN RESPONSABLE ASIGNADO ---")
    log(f"Total sin área responsable: {num_sin_resp}")
    if num_sin_resp > 0:
        log("ALERTA CRÍTICA DE GOBERNANZA: Una obligación legal sin responsable no se gestiona;")
        log("se descubre únicamente al momento de una fiscalización o incidente sancionatorio.\n")
        for idx, row in sin_resp.iterrows():
            log(f"  [!] ID: {row['id']} | Norma: {row['Norma']} | Art: {row['Artículo']}")
            log(f"      Obligación : {row['Obligación concreta']}")
            log(f"      Consecuencia: {row['Consecuencia del incumplimiento']}")
            log(f"      Acción recomendada: Asignar formalmente al área correspondiente en el MOF institucional.\n")
    else:
        log("Todas las obligaciones cuentan con un área institucional formalmente asignada.")
    log()

    # 3. Distribución por Marco Normativo / Autoridad
    log("--- 3. OBLIGACIONES EVALUADAS POR MARCO NORMATIVO ---")
    norma_counts = df["Norma"].value_counts()
    for norma, count in norma_counts.items():
        cumple_n = len(df[(df["Norma"] == norma) & (df["Estado"] == "Cumple")])
        parcial_n = len(df[(df["Norma"] == norma) & (df["Estado"] == "Parcial")])
        nocumple_n = len(df[(df["Norma"] == norma) & (df["Estado"] == "No cumple")])
        log(f"  • {norma:<30} : {count:>2} obligaciones (Cumple: {cumple_n}, Parcial: {parcial_n}, No cumple: {nocumple_n})")
    log()

    # 4. Proyectos No Negociables
    log("--- 4. PROYECTOS NO NEGOCIABLES DERIVADOS DE OBLIGACIONES LEGALES ---")
    log("Principio PETI: Los proyectos derivados de mandatos legales vencidos o perentorios")
    log("ingresan directamente al Portafolio (Sección 7.1) sin competir en priorización (Sección 7.2).\n")
    
    proyectos_no_negociables = df[df["Estado"].isin(["No cumple", "Parcial"])][
        ["id", "Plazo", "Proyecto que la cierra", "Norma", "Consecuencia del incumplimiento"]
    ].copy()
    
    # Ordenar por criticidad de plazo
    orden_plazo = {"Inmediato": 1, "30 días": 2, "45 días": 3, "60 días": 4, "90 días": 5}
    proyectos_no_negociables["Orden"] = proyectos_no_negociables["Plazo"].map(lambda x: orden_plazo.get(x, 99))
    proyectos_no_negociables = proyectos_no_negociables.sort_values(by=["Orden", "id"]).drop(columns=["Orden"])
    
    log(f"{'ID':<6} | {'Plazo':<11} | {'Proyecto que Cierra la Brecha':<55} | {'Norma Reguladora'}")
    log("-" * 105)
    for _, row in proyectos_no_negociables.iterrows():
        log(f"{row['id']:<6} | {row['Plazo']:<11} | {row['Proyecto que la cierra'][:53]:<55} | {row['Norma']}")
    log()
    log("=" * 80)
    log("  FIN DEL REPORTE DE ANÁLISIS DE CUMPLIMIENTO")
    log("=" * 80)

    # Guardar salida en evidencias
    salidas_dir = os.path.join(os.path.dirname(__file__), "..", "docs", "evidencias", "S08", "salidas")
    os.makedirs(salidas_dir, exist_ok=True)
    out_file = os.path.join(salidas_dir, "salida_analisis_cumplimiento.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(salida_lineas) + "\n")
    print(f"\n[OK] Salida textual guardada en: {out_file}")

    # 5. Generar Gráficos con Matplotlib
    graficos_dir = os.path.join(os.path.dirname(__file__), "..", "graficos")
    os.makedirs(graficos_dir, exist_ok=True)

    # Gráfico 1: Estado de Cumplimiento (Barras + Torta)
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    colores = {'Cumple': '#28a745', 'Parcial': '#ffc107', 'No cumple': '#dc3545'}
    estados = ['Cumple', 'Parcial', 'No cumple']
    valores = [estado_counts.get(e, 0) for e in estados]
    color_list = [colores[e] for e in estados]

    # Barras
    bars = ax1.bar(estados, valores, color=color_list, edgecolor='#333333', linewidth=1.2, width=0.55)
    ax1.set_title('Estado de Cumplimiento Normativo (Frecuencia)', fontsize=13, fontweight='bold', pad=12)
    ax1.set_ylabel('Número de Obligaciones', fontsize=11)
    ax1.set_ylim(0, max(valores) + 4)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.4, f"{yval} ({yval/total_obligaciones*100:.1f}%)", 
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Torta
    wedges, texts, autotexts = ax2.pie(
        valores, labels=estados, autopct='%1.1f%%', startangle=140, 
        colors=color_list, explode=(0.05, 0.05, 0.08),
        wedgeprops=dict(edgecolor='#333333', linewidth=1.2)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_weight('bold')
        at.set_fontsize(11)
    ax2.set_title('Distribución Porcentual del Cumplimiento', fontsize=13, fontweight='bold', pad=12)

    plt.suptitle('CrediTech Perú S.A.C. · Diagnóstico de Cumplimiento Normativo del PETI (N=26)', 
                 fontsize=15, fontweight='bold', y=0.98)
    plt.tight_layout()
    chart1_path = os.path.join(graficos_dir, "NO_cumplimiento_resumen.png")
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico de resumen guardado en: {chart1_path}")

    # Gráfico 2: Obligaciones por Marco Normativo
    fig, ax = plt.subplots(figsize=(12, 6))
    normas_sorted = norma_counts.index.tolist()
    
    cumple_vals = [len(df[(df["Norma"] == n) & (df["Estado"] == "Cumple")]) for n in normas_sorted]
    parcial_vals = [len(df[(df["Norma"] == n) & (df["Estado"] == "Parcial")]) for n in normas_sorted]
    nocumple_vals = [len(df[(df["Norma"] == n) & (df["Estado"] == "No cumple")]) for n in normas_sorted]

    y_pos = range(len(normas_sorted))
    ax.barh(y_pos, cumple_vals, label='Cumple', color='#28a745', edgecolor='#333')
    ax.barh(y_pos, parcial_vals, left=cumple_vals, label='Parcial', color='#ffc107', edgecolor='#333')
    ax.barh(y_pos, nocumple_vals, left=[c + p for c, p in zip(cumple_vals, parcial_vals)], label='No cumple', color='#dc3545', edgecolor='#333')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(normas_sorted, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel('Cantidad de Obligaciones Evaluadas', fontsize=11)
    ax.set_title('Evaluación de Cumplimiento por Dispositivo Legal / Marco Regulatorio', fontsize=13, fontweight='bold', pad=12)
    ax.legend(loc='lower right', frameon=True)
    plt.tight_layout()
    chart2_path = os.path.join(graficos_dir, "NO_distribucion_normas.png")
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico de distribución de normas guardado en: {chart2_path}")

if __name__ == "__main__":
    main()
