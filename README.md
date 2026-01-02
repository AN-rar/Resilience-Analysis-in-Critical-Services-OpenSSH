# Resilience-Analysis-in-Critical-Services-OpenSSH

**IN ENGLESH:**

🧑‍💻 Researcher Profile
This project was developed self-taught at the age of 15. By leveraging open-source documentation, independent research, and the consultative support of Artificial Intelligence (Gemini), I conceptualized, programmed, and executed this security laboratory from the ground up.

1. Context and Objectives
The research focuses on the stability of the SSH protocol (Port 22) under stress conditions. The environment utilizes a Red Team/Blue Team architecture to evaluate the response of the sshd.exe process when subjected to massive malformed data delivery (Fuzzing).

2. Methodology and Development
I developed two custom auditing tools in Python to observe different levels of impact on the target system:

Incremental Fuzzing Script: Designed to identify the server's processing threshold using "junk" data payloads with predefined limits.

Continuous Saturation Script (Flood): An optimized version for uninterrupted traffic delivery, aiming for the total exhaustion of the service's execution threads.

3. Results Analysis (DoS)
Two critical behaviors were identified during testing:

CPU Saturation: Using the limited-load script, the server reached 100% CPU utilization. While the service remained active, the resulting system latency rendered it inoperable for legitimate users.

Denial of Service (DoS): By deploying the infinite-flow script, the input buffer overload and socket exhaustion caused the service to collapse entirely (Timeout). This confirmed a Resource Exhaustion vulnerability.

**EN ESPAÑOL:**

🧑‍💻 Perfil del Investigador
Este proyecto fue desarrollado de forma autodidacta a la edad de 15 años. Utilizando recursos de documentación abierta, investigación propia y el apoyo consultivo de herramientas de Inteligencia Artificial (Gemini), logré conceptualizar, programar y ejecutar este laboratorio de seguridad.

1. Contexto y Objetivos
La investigación se centra en la estabilidad del protocolo SSH (Puerto 22) bajo condiciones de estrés. El escenario utiliza una arquitectura de Red/Blue Team para evaluar cómo responde el proceso sshd.exe ante el envío masivo de paquetes malformados (Fuzzing).

2. Metodología y Desarrollo
Desarrollé dos herramientas de auditoría en Python para observar diferentes niveles de impacto en el sistema víctima:

Script de Fuzzing Incremental: Diseñado para identificar el umbral de procesamiento del servidor mediante cargas de texto "basura" con límites predefinidos.

Script de Saturación Continua (Flood): Una versión optimizada para enviar tráfico de forma ininterrumpida, buscando el agotamiento total de los hilos de ejecución del servicio.

3. Análisis de Resultados (DoS)
Durante las pruebas, se identificaron dos comportamientos críticos:

Saturación de CPU: Con el script de carga limitada, el servidor alcanzó un 100% de uso de CPU. Aunque el servicio permaneció activo, la latencia del sistema lo hizo inoperable para usuarios legítimos.

Denegación de Servicio (DoS): Al utilizar el script de flujo infinito, la sobrecarga en el búfer de entrada y el agotamiento de sockets provocaron que el servicio colapsara por completo (Timeout). Esto confirmó una vulnerabilidad por agotamiento de recursos.
