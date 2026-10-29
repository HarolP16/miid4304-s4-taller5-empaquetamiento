# Taller 5 - Empaquetamiento de modelos

Repositorio académico del Taller 5 del curso MIID 4304 - Despliegue de Soluciones Analíticas.

## Estructura

- `package-src/`: código fuente, configuración, datos de entrenamiento y pruebas del paquete `model-abandono`.
- `test/`: datos y script que comprueban el paquete instalado desde el archivo Wheel.

## Flujo de trabajo

1. Entrenar el modelo con Tox.
2. Ejecutar las pruebas automatizadas.
3. Construir las distribuciones `.tar.gz` y `.whl`.
4. Instalar y probar el paquete desde `test/`.
5. Actualizar el modelo y construir la versión 0.0.2.

Las llaves privadas, ambientes virtuales y artefactos generados se excluyen del repositorio.
