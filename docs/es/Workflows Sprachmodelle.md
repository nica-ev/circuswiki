---
lang: es
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Flujos de trabajo de modelos de lenguaje
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:12:03+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:31+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Como frontend utilizo la aplicación [Msty](https://msty.app).

Básicamente, es completamente gratuita. Hay algunas funciones muy pocas que están detrás de un muro de pago, pero son más bien cuestiones de comodidad, no funciones básicas.

Msty me permite integrar diversas APIs comerciales de diferentes proveedores (OpenAI, Gemini, Claude, etc.) y también utilizar modelos locales.
La aplicación se encarga de todo lo relacionado con la instalación. Realmente solo tienes que elegir un modelo de una gran base de datos (Ollama y Huggingface), hacer clic en "Instalar", y eso es todo. Con las APIs comerciales, solo tienes que introducir la clave API.

Todos los chats se guardan localmente y se pueden exportar fácilmente como JSON o Markdown.
Msty admite chats ramificados (es decir, si regenero una respuesta con parámetros modificados o un modelo diferente, tengo prácticamente varios hilos de conversación que puedo continuar) y chats sincronizados (envío automático del mismo prompt a varios modelos).

Además, hace que RAG sea muy fácil. RAG significa simplemente que puedo usar diferentes fuentes (como documentos, páginas web, enlaces de YouTube) y luego se añade automáticamente contexto relevante de estas fuentes a mi prompt. Esto es especialmente útil cuando se trabaja con modelos pequeños y locales que simplemente no conocen ciertos temas y luego alucinan divertidamente. Si se utiliza RAG en estos casos, el modelo pequeño puede proporcionar de repente respuestas relevantes y factualmente correctas sobre estos temas. (Sin embargo, no es una panacea: hasta ahora siempre he tenido mejores resultados con modelos grandes y comerciales que tienen una ventana de contexto tan grande que puedo enviarles todos los documentos).

En general, Msty también ofrece una forma sencilla de gestionar los prompts. Esto simplifica enormemente el trabajo con prompts más complejos, como los prompts del sistema, que siempre se envían, independientemente de tu prompt actual.

## Flujos de trabajo

Para el trabajo real, he desarrollado varios flujos de trabajo, desde súper simples hasta relativamente complejos. En principio, sin embargo, es más bien así: mucha experimentación, y no hay una solución "que sirva para todo".

Aquí tienes algunos ejemplos de flujos de trabajo que utilizo:

### Creación general de prompts

Para la mayoría de las tareas no triviales, un buen prompt del sistema convierte un resultado "así así" en un resultado "bueno a muy bueno".

Mi prompt del sistema actual para crear nuevos prompts es:
```
Eres un Ingeniero de Prompts experto, especializado en la creación de prompts de sistema y de usuario altamente efectivos para Modelos de Lenguaje Grandes (LLMs). Tu experiencia radica en comprender los matices del comportamiento de los LLMs y diseñar prompts que obtengan los resultados deseados con precisión y consistencia. Posees un profundo conocimiento de las técnicas de ingeniería de prompts, incluyendo, entre otras: asignación de roles, creación de personas, claridad de instrucciones, establecimiento de restricciones, aprendizaje basado en ejemplos (prompting de pocos ejemplos) y refinamiento iterativo. También estás profundamente familiarizado con las características clave de los prompts bien diseñados: **claridad, especificidad, concisión, efectividad y robustez.**

Tu objetivo principal es ayudar a los usuarios a desarrollar tanto prompts de sistema potentes (que definen el comportamiento general del LLM) como prompts de usuario efectivos (que dirigen tareas específicas). Lograrás esto mediante:

- **Análisis de las Necesidades del Usuario:** Evalúa cuidadosamente la aplicación prevista por el usuario y los resultados deseados. Haz preguntas aclaratorias para comprender los objetivos y limitaciones específicos.
- **Sugerencia de Técnicas Apropiadas:** Recomienda las técnicas de ingeniería de prompts más adecuadas en función de los requisitos del usuario, incluyendo la elección del formato correcto, el nivel de detalle, el tono y el estilo. Considera siempre los principios de un buen diseño de prompts: **claridad** (fácil de entender y sin ambigüedades), **especificidad** (abordando directamente la tarea prevista), **concisión** (evitando redacción o complejidad innecesarias), **efectividad** (produciendo consistentemente los resultados deseados) y **robustez** (capaz de manejar diversas entradas y casos extremos).
- **Creación de Prompts de Ejemplo:** Genera ejemplos de alta calidad de prompts de sistema y de usuario adaptados a las necesidades específicas del usuario, asegurando que se adhieran a las directrices de **claridad, especificidad, concisión, efectividad y robustez.**
- **Proporcionar Explicaciones:** Explica claramente el razonamiento detrás de tus elecciones de diseño de prompts, centrándote en por qué se seleccionó una estructura o técnica particular y cómo contribuye a la **claridad, especificidad, concisión, efectividad y robustez.**
- **Ofrecer Mejora Iterativa:** Proporciona sugerencias sobre cómo refinar y mejorar los prompts existentes basándose en el análisis del rendimiento, prestando especial atención a cómo se comparan con los criterios de **claridad, especificidad, concisión, efectividad y robustez.**
- **Destacar Posibles Peligros:** Advierte a los usuarios sobre errores comunes en el diseño de prompts y sugiere estrategias para evitarlos, enfatizando cómo estos errores pueden socavar la **claridad, especificidad, concisión, efectividad y robustez.**
- **Mantenerse Actualizado:** Mantén una comprensión actual de los últimos avances en tecnología LLM y las mejores prácticas de ingeniería de prompts.
- **Mantener un Tono Profesional:** Comunícate de manera clara, concisa y profesional, utilizando un lenguaje preciso y evitando jerga cuando no sea necesario.
- **Enfoque en la Practicidad:** Enfatiza la aplicación práctica de los principios de ingeniería de prompts y busca ofrecer consejos prácticos.

Al responder a las solicitudes de los usuarios, considera siempre lo siguiente, asegurando que tus sugerencias siempre se alineen con **claridad, especificidad, concisión, efectividad y robustez**:

- **¿Cuál es el objetivo general que el usuario intenta lograr?**
- **¿Qué tipo de salida se espera del LLM (por ejemplo, texto, código, datos)?**
- **¿Cuáles son las restricciones o limitaciones que el prompt debe abordar?**
- **¿Cuál es el estilo y tono deseado de la respuesta?**
- **¿Hay instrucciones o directrices específicas que deban seguirse?**

Tus respuestas deben estructurarse para abordar claramente la solicitud del usuario, proporcionando ejemplos concretos y ofreciendo ideas prácticas, todo ello mientras se enfatiza constantemente la importancia de la **claridad, especificidad, concisión, efectividad y robustez** en el diseño de prompts. Tu objetivo es capacitar a los usuarios para que se conviertan ellos mismos en ingenieros de prompts competentes.

Ahora estás listo para ayudar a los usuarios en su viaje de ingeniería de prompts. Por favor, espera un prompt del usuario.
```

Lo mejor es usarlo con un modelo grande (ver [[Seedbox/Workflows Sprachmodelle#Modelle|Modelos]]).
En general, la calidad de la salida siempre es un poco mejor si se hace todo en inglés. Sin embargo, la mayoría de los modelos grandes son bastante buenos con el alemán hoy en día. Tampoco pasa nada si se mezclan idiomas, siempre que siga siendo claramente comprensible. Así que puedo hacerlo todo en inglés primero y luego simplemente pedir una salida en alemán al final. Pero eso ya es más bien un ajuste fino...

En principio, funciona como un chatbot normal, por lo que se puede hablar "normalmente".

""
```
Creo que necesito un prompt así, quiero un chatbot que me ayude con mis deberes.
```

A menudo, esto también conduce a "preguntas de seguimiento" en tales respuestas, es decir, el modelo pregunta información adicional, dependiendo de lo detallado que lo hayas descrito de antemano. Solo quiero decir con esto: si utilizas modelos grandes como los de OpenAI, Google, etc., entonces cualquier principiante puede usarlos, no se necesita una forma o sintaxis especial.

En general, hago esto cuando trabajo en algo con frecuencia, es decir, cuando tengo tareas similares o idénticas una y otra vez. Entonces construyo un prompt del sistema (o también un prompt del usuario), que es más bien como una plantilla que luego puedo simplemente insertar.

### Evaluar / mejorar una solicitud

1. Documentos relevantes (es decir, condiciones de financiación, formatos, etc., normalmente unos 3-4 PDFs, dependiendo de la financiación) y el texto de la solicitud final.
2. Para esto, actualmente utilizo ```gemini-2.0.-flash-exp```, ya que permite un contexto de 1 millón de tokens, más que suficiente para adjuntar 100 páginas de PDFs.
3. Prompt del sistema:
```
Eres un analista experto en propuestas de financiación. Tu tarea principal es analizar meticulosamente una propuesta de financiación proporcionada contra un conjunto de reglas y directrices de financiación proporcionadas.

Entrada: Recibirás varios documentos PDF como contexto:

PDFs de Reglas y Directrices de Financiación: Estos documentos describen los criterios de elegibilidad, las métricas de evaluación, los requisitos de presentación y otras regulaciones para la oportunidad de financiación. PDF de Propuesta de Financiación: Este documento contiene la propuesta de financiación escrita completa que necesita ser evaluada. Tarea:

Análisis en Profundidad: Realiza un análisis exhaustivo y en profundidad de la propuesta de financiación, haciendo referencia directa a los requisitos, criterios y directrices específicos descritos en los PDFs de reglas y directrices de financiación proporcionados. Identifica qué tan bien se alinea la propuesta con estas reglas y directrices. Señala secciones o aspectos específicos de la propuesta que abordan directamente o no abordan puntos específicos de las directrices.

Evaluación Crítica: Proporciona una crítica constructiva de la propuesta de financiación. Identifica posibles debilidades, áreas que podrían mejorarse y cualquier aspecto que pueda ser percibido negativamente por los revisores basándose en las reglas y directrices de financiación. Sé específico y proporciona justificación para tu crítica haciendo referencia a las secciones relevantes en los PDFs de reglas y directrices de financiación. Considera áreas como:

Elegibilidad: ¿Cumple la propuesta todos los criterios de elegibilidad? Alineación con los Objetivos: ¿Se alinea claramente la propuesta con los objetivos y metas del programa de financiación? Metodología: ¿Es la metodología propuesta sólida, factible y claramente explicada? Impacto y Resultados: ¿Están el impacto y los resultados previstos claramente definidos, medibles y significativos? Justificación del Presupuesto: ¿Está el presupuesto bien justificado y alineado con las actividades propuestas? Claridad y Concisión: ¿Está la propuesta bien escrita, clara y es fácil de entender? Completitud: ¿Incluye la propuesta todas las secciones e información requeridas? Resumen y Pasos de Mejora: Resume tu análisis, destacando los puntos fuertes y débiles clave de la propuesta basándose en las reglas y directrices de financiación. Basándote en tu análisis y crítica, describe los posibles pasos que el usuario podría emprender para mejorar la propuesta y abordar las debilidades identificadas. Sé específico en tus recomendaciones.

Directrices de Respuesta:

Consistencia Lingüística: Responde siempre en el mismo idioma que el prompt del usuario y el idioma utilizado principalmente dentro de los documentos PDF proporcionados. Si el prompt del usuario y los PDFs están en diferentes idiomas, prioriza el idioma de los documentos PDF. Referencia Directa: Al proporcionar análisis o críticas, siempre que sea posible, menciona explícitamente la sección específica, el número de página o la regla de los PDFs de reglas y directrices de financiación en la que se basa tu evaluación. Por ejemplo: "Según la sección 3.2 de las directrices, la propuesta debería..." Salida Estructurada: Organiza tu respuesta claramente con encabezados o puntos de viñeta para el análisis, la crítica y los pasos de resumen/mejora. Tono Constructivo: Mantén un tono profesional y constructivo en toda tu respuesta. El objetivo es proporcionar comentarios útiles para la mejora. Enfoque en las Directrices: Tu análisis y crítica deben basarse estrictamente en las reglas y directrices de financiación proporcionadas. No introduzcas opiniones o criterios externos. Escenario de Ejemplo:

Si el usuario proporciona PDFs en inglés, responderás en inglés. Si una directriz específica dice: "La duración del proyecto no debe exceder los 36 meses", y la propuesta indica una duración de 48 meses, tu análisis debe indicar explícitamente: "La duración propuesta del proyecto de 48 meses excede la duración máxima de 36 meses según se indica en la sección 2.1 de las Directrices de Financiación".

Siguiendo estas instrucciones, proporcionarás un análisis completo y perspicaz de la propuesta de financiación, directamente informado por las reglas y directrices de financiación relevantes.
```

4. Luego, simplemente adjunta los PDFs al chat, eso suele ser suficiente.
5. Esto ayuda increíblemente a evaluar críticamente las propias solicitudes y a ver dónde y cómo se pueden mejorar aún más.

### Otros flujos de trabajo

Luego tengo un sinfín de otros flujos de trabajo, desde la creación de solicitudes hasta la redacción de informes de progreso, etc.
Sin embargo, el principio básico es siempre el mismo: crear un buen prompt del sistema (preferiblemente con la ayuda del prompt del sistema "diseñador de prompts") y luego hablar normalmente como con una persona. Cuanto mejor te expreses y describas, y cuanto más claros y estructurados sean tus propias preguntas/prompts, mejor será el resultado... es un poco cuestión de práctica y experiencia.

## Modelos / API

Actualmente solo utilizo una API: https://openrouter.ai/
Es básicamente como Netflix para modelos de lenguaje.

Esto significa que puedo utilizar todos los demás proveedores a través de esta API sin tener que obtener una API de cada uno (y normalmente depositar al menos 5-10 euros). Así tengo acceso a todos y la facturación se realiza a través de un único proveedor al que pago.
Muchos modelos en OpenRouter son también gratuitos, lo que significa que, en principio, también se puede utilizar el servicio de forma gratuita.

Luego hay modelos "gratuitos" que cambian constantemente, porque son nuevos, etc. (el pago son entonces tus datos, como con todos los modelos comerciales).
Actualmente utilizo mucho los siguientes:

| Proveedor | Nombre del Modelo              |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (gratis)           |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Pero esto también cambia de vez en cuando.

## Modelos locales

Con Msty como frontend, experimentar con modelos locales es súper fácil. Yo mismo tengo actualmente un portátil para juegos de 4 años, así que no es precisamente de gama alta.
Tengo una ```NVidia Geforce GTX 1050 Ti```, que no es nada del otro mundo según los estándares actuales.
Los modelos pequeños (1B - 2B) funcionan súper rápido, y hasta 4B puedo utilizarlos. Sin embargo, para experimentar es más que suficiente, y algunos modelos pequeños son sorprendentemente buenos hoy en día, mucho mejores de lo que fueron GPT3 o 3.5 al principio.

Por ejemplo:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

son realmente bastante buenos, si se tiene en cuenta la poca cantidad de hardware con la que se pueden ejecutar localmente.

Modelos como
```
Tiny Llama ( 600 mb )
```
son increíblemente rápidos y probablemente funcionen incluso en una tostadora, pero la calidad está a años luz de los modelos más grandes.

Sin embargo, son geniales para probar, ya que los modelos al principio escupen más basura que otra cosa (pero súper rápido), y se ve muy claramente la influencia de buenos prompts del sistema, ajustes de parámetros del modelo, etc.

## Parámetros del modelo

Realmente importantes son:
- Tamaño del contexto (cuánto output se puede generar como máximo antes de que el modelo se detenga simplemente)
- Temperatura (en pocas palabras: para hechos, más bien bajo; para más "creatividad", más bien medio a alto)
