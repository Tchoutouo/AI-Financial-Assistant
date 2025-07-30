# 📊 Assistant Analyste Financier Intelligent

Ce projet est une application Streamlit qui permet d'analyser des **rapports financiers en PDF** à l'aide d'une **IA locale**. Grâce à la puissance des modèles d'embeddings de Hugging Face et à un index vectoriel en mémoire, vous pouvez poser des questions sur votre rapport et obtenir des réponses contextuelles instantanées.

---

## 🚀 Fonctionnalités

- 📁 Téléversement de fichiers PDF financiers.
- 🔍 Indexation intelligente des pages grâce aux embeddings HuggingFace.
- 🤖 Questions prédéfinies pour extraire les données clés :
  - Chiffre d'affaires
  - Coûts opérationnels
  - Segments performants
  - Ratio de solvabilité (CET1)
  - Risques financiers
  - Évolution des bénéfices
- ✍️ Possibilité de poser des **questions personnalisées**.
- 💡 Résultats contextualisés avec aperçu du contenu des pages pertinentes.

---

## 🧠 Technologies utilisées

- [Streamlit](https://streamlit.io/) — interface utilisateur simple et rapide.
- [LangChain](https://python.langchain.com/) — gestion des documents et des vecteurs.
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers) — vectorisation des textes avec `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`.
- [dotenv](https://pypi.org/project/python-dotenv/) — gestion des clés API via fichier `.env`.

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Tchoutouo/AI-Financial-Assistant.git
cd AI-Financial-Assistant
