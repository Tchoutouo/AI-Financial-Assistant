
import os
import streamlit as st
from dotenv import load_dotenv 
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
#from langchain_core.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

#from getpass import getpass

# HUGGINGFACEHUB_API_TOKEN = getpass()
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
# os.environ["HUGGINGFACEHUB_API_TOKEN"]=hf_XXXXXXXXXXXXXXXXXXXXXXXXX

load_dotenv()

# Titre de l'application
st.title("Assistant Analyste Financier  Intelligent")
st.subheader("Analysez vos rapports financiers avec un assistant IA")

#upload du fichier PDF
uploaded_file = st.file_uploader("Téléchargez votre rapport financier (format PDF)", type=["pdf"])

if uploaded_file :
    # Enregsitrement du fichier PDF localement
    with open("rapport_financier.pdf", "wb") as f:
        f.write(uploaded_file.read())
        
    # Charger le fichier PDF avec PyPDFLoader
    st.write("Chargement du fichier PDF...")
    loader = PyPDFLoader("rapport_financier.pdf")
    
    # Charger les pages de manière asynchrone
    pages = []
    for page in loader.lazy_load():
        pages.append(page)
        
    # Verification que le document contient des pages 
    if not pages:
        st.error("Le document PDF ne contient pas de pages valides.")
    else:
        # Afficher les métadonnées et les 100 premiers caractères de la première page
        st.subheader("Aperçu de la première page")
        st.write(f"**Méta-données :** {pages[0].metadata}")
        st.write(f"**Contenu (100 premiers caractères):** {pages[0].page_content[:100]}...")
        
        # Créer un vecteur de stockage en mémoire
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
        # Créer un index vectoriel a partir des pages
        vector_store = InMemoryVectorStore.from_documents(pages, embedding=embedding)
        # Questions financières par défaut
        st.subheader("Questions prédéfinies")
        default_questions = [
            "Quel est le chiffre d'affaires de l'année dernière ?",
            "Quels sont les principaux coûts opérationels ?",
            "Quels sont les segments les plus performants ?",
            "Quel est le ratio de solvabilité (CET1)?",
            "Quels sont les principaux risques financiers identifiés ?",
            "Quelle est l'évolution des bénéfices par rapport à l'année précédente ?",
        ]
        
        selected_question = st.selectbox("Choisissez une question prédéfinie", default_questions)
        
        #Bouton pour les questions prédéfinies
        if st.button("Obtenir une réponse pour la question prédéfinie"):
            st.write("Recherche en cours pour la question prédéfinie...")
            # Rechercher la réponse dans le vecteur de stockage
            docs = vector_store.similarity_search(selected_question, k=1)
            if docs:
                for doc in docs:
                    st.write(f'page {doc.metadata["page"]}: {doc.page_content[:300]}...')
            else:
                st.error("Aucune réponse trouvée dans le document.")
        
        # Option pour poser une question personnalisée
        st.subheader("Posez une question spécifique ")
        user_question = st.text_input("Entrez votre propre question :", "")
        
        # Bouton pour la question personnalisée
        if st.button("Obtenir une réponse pour la question spécifique"):
            if user_question.strip():
                st.write("Recherche en cours pour votre question...")
                # Rechercher la réponse dans le vecteur de stockage
                docs = vector_store.similarity_search(user_question, k=2)
                if docs:
                    for doc in docs:
                        st.write(f'page {doc.metadata["page"]}: {doc.page_content[:300]}...')
                else:
                    st.error("Aucune réponse trouvée dans le document.")
            else:
                st.warning("Veuillez entrer une question avant de cliquer sur le bouton.")