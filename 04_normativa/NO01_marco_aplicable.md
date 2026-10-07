# Marco Normativo Aplicable: Determinación y Árbol de Decisión
## Código: NO01 · Determinación del Marco Regulatorio

---

### 1. Perfil y Naturaleza Jurídica de la Organización

| Atributo Institucional | Detalle de la Organización |
|---|---|
| **Razón Social** | CrediTech Perú S.A.C. |
| **RUC** | 20608945123 |
| **Naturaleza Jurídica** | Persona jurídica de derecho privado (Sociedad Anónima Cerrada) |
| **Sector Económico** | Sistema Financiero no bancario / Tecnología Financiera (*Fintech*) |
| **Actividad Principal** | Otorgamiento de microcréditos 100 % digitales mediante evaluación de riesgo crediticio automatizada (*scoring* algorítmico con Machine Learning), originación y desembolso digital de créditos, y gestión de cobranza. |
| **Dimensión y Estructura** | 64 colaboradores distribuidos en 4 áreas funcionales: Administración y Finanzas (18), Operaciones y Créditos (22), Ventas y Comercial (16) y TI (8). Más de 210,000 operaciones de crédito desembolsadas a nivel nacional. |
| **Infraestructura Tecnológica** | Arquitectura nativa en la nube (*Cloud Native*) desplegada en Amazon Web Services (AWS, región us-east-1 Norte de Virginia) y Google Cloud Platform (GCP, región us-central1 Iowa) para *datalake* y reentrenamiento analítico. |
| **Tipos de Datos Tratados** | **Datos Personales Generales:** Nombres, apellidos, documento de identidad (DNI/CE), número telefónico, correo electrónico, geolocalización de conexión, dirección y referencias familiares.<br/>**Datos Personales Sensibles:** Biometría facial (capturada durante el proceso de *onboarding* digital para verificación de identidad contra RENIEC), información de ingresos económicos, historial crediticio bancario y morosidad histórica.<br/>**Datos Internos:** Planillas laborales, cuentas bancarias de colaboradores, legajos de personal y datos de proveedores personas naturales. |

---

### 2. Aplicación del Árbol de Decisión Normativo

Se aplicó el árbol de decisión metodológico para evaluar la aplicabilidad regulatoria sobre las operaciones tecnológicas y de datos de **CrediTech Perú S.A.C.**:

```mermaid
flowchart TD
    Inicio["<b>Inicio: Evaluación de la Organización</b><br/>CrediTech Perú S.A.C."] --> Q1{"¿Trata datos de personas naturales?<br/><i>(Clientes, colaboradores, postulantes)</i>"}
    
    Q1 -- SÍ --> R1["<b>APLICA: Ley 29733 + D.S. 016-2024-JUS</b><br/>Protección de Datos Personales"]
    R1 --> Q1_1{"¿Trata datos SENSIBLES?<br/><i>(Biometría facial, ingresos, crédito)</i>"}
    Q1_1 -- SÍ --> R1_1["Consentimiento expreso e inequívoco<br/>+ Medidas de seguridad reforzadas"]
    
    R1 --> Q1_2{"¿Almacena/procesa datos fuera del Perú?<br/><i>(Nube AWS us-east-1 / GCP)</i>"}
    Q1_2 -- SÍ --> R1_2["Régimen de Flujo Transfronterizo<br/>(Registro ANPD + Cláusulas contractuales)"]

    Inicio --> Q2{"¿Es entidad de la administración pública?"}
    Q2 -- NO --> R2["<b>DESCARTADO: Marco de Gobierno Digital</b><br/>D.Leg. 1412, D.S. 029-2021-PCM, D.S. 085-2023-PCM<br/>RSGD 005-2018-PCM, RM 119-2018-PCM, PIDE, Transparencia"]

    Inicio --> Q3{"¿Pertenece al sistema financiero o fintech supervisada?<br/><i>(Préstamos y evaluación crediticia)</i>"}
    Q3 -- SÍ --> R3["<b>APLICA: Normativa SBS y UIF</b><br/>Res. SBS 504-2021 (Ciberseguridad SGSI-C)<br/>Res. SBS 11356-2008 (Riesgo Operacional)<br/>Res. SBS 3198-2023 (Conducta de Mercado)<br/>Res. SBS 789-2018 (PLAFT / UIF)"]

    Inicio --> Q4{"¿Emite valores en mercado de valores?"}
    Q4 -- NO --> R4["<b>DESCARTADO: Normativa SMV</b><br/>Reporte de gobierno corporativo"]

    Inicio --> Q5{"¿Usa software de terceros y desarrollo propio?"}
    Q5 -- SÍ --> R5["<b>APLICA: D. Leg. 822 (Derecho de Autor)</b><br/>Licenciamiento de software y protección de código"]

    Inicio --> Q6{"¿Emite comprobantes de pago electrónicos?"}
    Q6 -- SÍ --> R6["<b>APLICA: Normativa SUNAT (R.S. 097-2012)</b><br/>Conservación de XML/CDR por mínimo 5 años"]

    Inicio --> Q7{"¿Usa firma digital con valor legal para créditos?"}
    Q7 -- SÍ --> R7["<b>APLICA: Ley 27269 + D.S. 052-2008-PCM</b><br/>Firma digital y certificados en pagarés digitales"]

    Inicio --> Q8{"¿Relaciones comerciales con consumidores digitales?"}
    Q8 -- SÍ --> R8["<b>APLICA: Ley 29571 + D.S. 011-2011-PCM</b><br/>Libro de Reclamaciones Virtual y protección consumidor"]

    Inicio --> Q9{"¿Es institución educativa superior?"}
    Q9 -- NO --> R9["<b>DESCARTADO: Normativa SUNEDU</b>"]

    classDef aplica fill:#D4EDDA,stroke:#28A745,stroke-width:2px,color:#155724;
    classDef descarta fill:#F8D7DA,stroke:#DC3545,stroke-width:2px,color:#721C24;
    classDef pregunta fill:#E8F1FB,stroke:#16285C,stroke-width:1px,color:#16285C;

    class Q1,Q1_1,Q1_2,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9 pregunta;
    class R1,R1_1,R1_2,R3,R5,R6,R7,R8 aplica;
    class R2,R4,R9 descarta;
```

---

### 3. Síntesis del Marco Aplicable

1. **Protección de Datos Personales (Ley 29733 y D.S. 016-2024-JUS):** La empresa realiza tratamiento automatizado intensivo de datos personales de cientos de miles de ciudadanos peruanos, incluyendo datos sensibles (biometría e ingresos). Obligación de registro ante la ANPD, Oficial de Protección de Datos (OPD), Evaluación de Impacto (EIPD) y régimen de flujo transfronterizo en la nube.
2. **Ciberseguridad y Riesgo Tecnológico Financiero (Res. SBS 504-2021, Res. SBS 11356-2008):** La plataforma opera desembolsos de dinero y custodia transaccional. Debe disponer de un SGSI-C (Sistema de Gestión de Seguridad de la Información y Ciberseguridad), Oficial CISO, *Ethical Hacking* periódico y planes de continuidad de negocio y recuperación ante desastres (BCP/DRP).
3. **Conducta de Mercado y Transparencia Algorítmica (Res. SBS 3198-2023):** Prohíbe sesgos y discriminación en los modelos de scoring, exigiendo explicabilidad para las decisiones automatizadas que rechacen créditos.
4. **Prevención del Lavado de Activos y Financiamiento del Terrorismo (Res. SBS 789-2018):** Obligación de monitoreo automatizado de operaciones no usuales y debida diligencia de conocimiento del cliente (KYC).
5. **Propiedad Intelectual y Software Legal (D. Leg. 822):** Prohibición terminante de uso de software sin licencia válida y protección de la autoría del core crediticio.
6. **Validez Legal de Contratación Electrónica (Ley 27269):** Otorgamiento de plena validez jurídica y no repudio a las solicitudes y pagarés suscritos con certificados digitales acreditados.
7. **Tributario Digital (R.S. 097-2012/SUNAT):** Emisión y custodia obligatoria e inmutable por 5 años de comprobantes electrónicos de pago y comisiones.
8. **Protección al Consumidor (Ley 29571):** Canal obligatorio del Libro de Reclamaciones Virtual con respuesta en máximo 15 días hábiles.

---

### 4. Normas Descartadas y Fundamentación Jurídico-Técnica

| Dispositivo Legal Descartado | Materia Regulada | Fundamento Técnico y Jurídico del Descarte |
|---|---|---|
| **D. Leg. N.° 1412** y **D.S. N.° 029-2021-PCM** | Ley de Gobierno Digital y su Reglamento | **No aplicable por el alcance subjetivo de la norma.** El Art. 2 del D. Leg. 1412 establece que la norma rige con carácter obligatorio para las entidades de la Administración Pública señaladas en el Art. I del Título Preliminar de la Ley 27444. CrediTech Perú S.A.C. es una persona jurídica privada sujeta al régimen societario mercantil. |
| **D.S. N.° 085-2023-PCM** | Política Nacional de Transformación Digital al 2030 | **No aplicable como mandato coercitivo.** Constituye un instrumento multisectorial de política pública de alcance nacional que fija metas para el Estado peruano, sin imponer sanciones operativas directas a personas jurídicas de derecho privado. |
| **RSGD N.° 005-2018-PCM/SEGDI** | Lineamientos para el Plan de Gobierno Digital (PGD) | **No aplicable.** Regula la formulación técnica obligatoria del PGD para entidades del sector público. La organización formula un PETI corporativo privado bajo marcos internacionales de la industria (COBIT 2019 e ISO/IEC 27001). |
| **RM N.° 119-2018-PCM** | Creación del Comité de Gobierno Digital y Líder de Gobierno Digital | **No aplicable.** Estructura de gobernanza exigible exclusivamente al aparato estatal. La empresa gobierna sus tecnologías mediante su Directorio, Comité de TI y las figuras de CISO y CIO. |
| **RSGTD N.° 003-2023-PCM/SGTD** | Uso obligatorio de la NTP-ISO/IEC 27001 en el Estado | **No aplicable la resolución administrativa.** Aunque la norma ISO/IEC 27001 se implementa en la organización como buena práctica y en cumplimiento de la Res. SBS 504-2021, la resolución de la SGTD aplica sólo a entidades públicas. |
| **Ley N.° 27806** | Ley de Transparencia y Acceso a la Información Pública | **No aplicable.** CrediTech Perú S.A.C. no administra fondos públicos ni presta servicios públicos en régimen de concesión monopólica; los derechos de acceso del usuario se ejercen por el régimen de derechos ARCO de la Ley 29733. |
| **Ley N.° 28716** | Ley de Control Interno de las Entidades del Estado | **No aplicable.** Marco de fiscalización y control gubernamental a cargo del Sistema Nacional de Control y la Contraloría General de la República sobre fondos públicos. |
| **Estándares de Interoperabilidad PIDE** | Plataforma de Interoperabilidad del Estado | **No aplicable como proveedor obligado.** La PIDE articula el intercambio de datos entre entidades públicas. La Fintech consume servicios de verificación de identidad mediante contratos comerciales y APIs privadas. |
| **Normativa SMV** | Mercado de Valores y Buen Gobierno Corporativo para emisores | **No aplicable.** CrediTech Perú S.A.C. no lista instrumentos de deuda ni acciones en la Bolsa de Valores de Lima (BVL) ni oferta públicamente valores mobiliarios. |
| **Normativa SUNEDU** | Ley Universitaria N.° 30220 y condiciones básicas | **No aplicable.** La empresa no brinda servicios educativos universitarios. |
