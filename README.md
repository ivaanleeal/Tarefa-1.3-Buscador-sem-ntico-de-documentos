# 📄 Sistema de Xestión e Consulta Semántica de Documentos con ChromaDB e Gradio

Este proxecto implementa unha aplicación sinxela baseada en **Gradio** que permite:

- Crear e xestionar unha colección de documentos en memoria utilizando **ChromaDB**.
- Subir múltiples ficheiros JSON que serán almacenados como documentos na colección.
- Realizar consultas semánticas sobre o contido destes documentos.
- Obter o documento máis relevante segundo a semántica da consulta.

---

## 🚀 Funcionalidades

### 🗂️ 1. Creación da colección en memoria
A aplicación inicializa unha colección en memoria chamada **`documents`** utilizando ChromaDB.  
A colección **non é persistente**, polo que os datos pérdense ao reiniciar a aplicación.

### 📤 2. Subida de ficheiros
- O usuario pode subir **múltiples ficheiros JSON (.json)**.
- Cada ficheiro súbese como un documento único á colección.
- Os documentos conteñen:
  - **ID único**
  - **Contido do ficheiro**
  - **Metadatos**, incluíndo polo menos o nome do ficheiro.

### 🔍 3. Consulta semántica
- O usuario introduce unha pregunta ou consulta en linguaxe humano.
- A aplicación fai unha **búsqueda semántica** na colección.
- Devólvese o documento máis relevante segundo o modelo de embeddings.

### 🖥️ 4. Interfaz gráfica con Gradio
A aplicación inclúe dúas pestanas principais:

1. **Subida de ficheiros**
   - Subida múltiple de documentos.
   - Mostra o estado do proceso.

2. **Consulta**
   - Entrada de texto para a consulta.
   - Mostra o documento máis relevante e os seus metadatos.

---

## 🧰 Tecnoloxías empregadas

- **Python 3.10+**
- **ChromaDB** (modo en memoria)
- **Gradio** (interface web)
- **SentenceTransformers** ou o modelo por defecto de ChromaDB

---
