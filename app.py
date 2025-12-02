import chromadb
import gradio as gr
import os

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="documents")

def subir_archivos(files):
    
    if not files:
        return "No se seleccionaron archivos."

    docs = []
    ids = []
    metadatas = []

    try:
        for f in files:
            filepath = f.name
            filename = os.path.basename(filepath) 
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            docs.append(content)
            ids.append(filename)
            metadatas.append({"filename": filename})

        collection.add(
            documents=docs,
            ids=ids,
            metadatas=metadatas
        )

        return f"{len(files)} archivo(s) subido(s) correctamente a la colección 'documents'."

    except Exception as e:
        return f"Error al subir archivos: {str(e)}"
    


def consultar_documento(query):
    
    try:
        result = collection.query(
            query_texts=[query],
            n_results=1
        )

        
        documento = result["documents"][0][0]
        filename = result["metadatas"][0][0]["filename"]
        
        score = result["distances"][0][0]

        return (
            f"Documento más relevante encontrado:\n"
            f"--- Nombre de Fichero: **{filename}** ---\n"
            f"--- Relevancia (Distancia): **{score:.4f}** ---\n\n"
            f"Contenido:\n{documento}"
        )

    except Exception as e:
        return f"Error en la consulta: {str(e)}"
    


with gr.Blocks(title="Buscador Semántico de Documentos (ChromaDB)") as demo:
    gr.Markdown("# 📚 Buscador Semántico con ChromaDB (In-Memory)")

    with gr.Tab("📂 Subir Archivos"):
        gr.Markdown("### Sube tus documentos de texto (.json) aquí.")
        file_input = gr.File(
            file_types=[".json"], 
            file_count="multiple", 
            label="Selecciona Ficheros  JSON"
        )
        subir_btn = gr.Button("🚀 Subir Documentos")
        status = gr.Textbox(label="Estado de la Operación", lines=2)
        
        subir_btn.click(
            fn=subir_archivos, 
            inputs=file_input, 
            outputs=status
        )
    
    with gr.Tab("🔍 Consulta Semántica"):
        gr.Markdown("### Introduce tu pregunta para encontrar el documento más relevante.")
        query_input = gr.Textbox(label="Introduce tu pregunta o consulta")
        consultar_btn = gr.Button("🔎 Consultar")
        resultado = gr.Textbox(label="Resultado de la Búsqueda", lines=10)
        
        consultar_btn.click(
            fn=consultar_documento, 
            inputs=query_input, 
            outputs=resultado
        )

demo.launch()