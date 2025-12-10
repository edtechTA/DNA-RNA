import streamlit as st
import graphviz
import plotly.graph_objects as go
import numpy as np


# --- Page Configuration ---
st.set_page_config(
    page_title="DNA vs RNA: The Code of Life",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- Custom CSS for "Infographic" Feel ---
st.markdown("""
<style>
    /* Main Background and Text */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Custom Headers */
    h1 {
        color: #2c3e50;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h2 {
        color: #e67e22;
        border-bottom: 2px solid #e67e22;
        padding-bottom: 10px;
    }
    h3 {
        color: #2980b9;
    }
    
    /* Cards/Containers */
    .info-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #3498db;
    }
    
    .rna-card {
        border-left: 5px solid #e74c3c;
    }
    
    .highlight {
        background-color: #f1c40f;
        padding: 2px 5px;
        border-radius: 3px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# --- Header Section ---
st.title("🧬 The Blueprint of Life: DNA vs. RNA")
st.markdown("<p style='text-align: center; font-size: 1.2em;'>An Interactive Guide for Middle School Scientists</p>", unsafe_allow_html=True)
st.divider()


# --- Section 1: The Big Difference (Side by Side) ---
col1, col2 = st.columns(2)


with col1:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.header("DNA")
    st.subheader("Deoxyribonucleic Acid")
    st.write("**The Master Plan**")
    st.write("Think of DNA as the **library** that stays safe inside the nucleus. It holds all the instructions for building you!")
    
    # DNA Visual (Double Helix representation)
    st.markdown("### ⛓️ Structure: Double Helix")
    st.write("It looks like a twisted ladder (two strands).")
    
    # DNA Bases
    st.markdown("### 🧱 Bases:")
    st.markdown("- **A**denine")
    st.markdown("- **T**hymine (Only in DNA!)")
    st.markdown("- **C**ytosine")
    st.markdown("- **G**uanine")
    
    st.info("Remember: **A** pairs with **T** (Apples in the Tree)")
    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="info-card rna-card">', unsafe_allow_html=True)
    st.header("RNA")
    st.subheader("Ribonucleic Acid")
    st.write("**The Messenger**")
    st.write("Think of RNA as the **photocopy** of the plan. It carries instructions out of the nucleus to build proteins.")
    
    # RNA Visual
    st.markdown("### 🧶 Structure: Single Strand")
    st.write("It looks like half a ladder (one strand).")
    
    # RNA Bases
    st.markdown("### 🧱 Bases:")
    st.markdown("- **A**denine")
    st.markdown("- **U**racil (Only in RNA!)")
    st.markdown("- **C**ytosine")
    st.markdown("- **G**uanine")
    
    st.error("Remember: **A** pairs with **U** (Apples Under the tree)")
    st.markdown('</div>', unsafe_allow_html=True)


# --- Section 2: Visualizing the Flow (Central Dogma) ---
st.markdown("## 🔄 How Information Flows (The Central Dogma)")
st.write("How do we turn code into a living thing? Follow the path below:")


# Create a graphviz diagram
graph = graphviz.Digraph()
graph.attr(rankdir='LR', bgcolor='transparent')


# Nodes
graph.attr('node', shape='box', style='filled', fillcolor='lightblue', fontname='Helvetica')
graph.node('DNA', 'DNA\n(The Master Plan)')


graph.attr('node', fillcolor='pink')
graph.node('RNA', 'mRNA\n(The Message)')


graph.attr('node', fillcolor='lightgreen')
graph.node('Protein', 'Protein\n(The Result)')


# Edges
graph.edge('DNA', 'RNA', label='Transcription\n(In Nucleus)')
graph.edge('RNA', 'Protein', label='Translation\n(In Ribosome)')


st.graphviz_chart(graph, use_container_width=True)


# --- Section 3: Interactive Transcriber Tool ---
st.markdown("## 🧪 Lab Activity: Transcribe DNA to RNA")
st.markdown("""
<div class="info-card">
    You are inside the nucleus! Your job is to take a strand of DNA and transcribe it into RNA so the cell can build a protein.
    <br><br>
    <b>Rules:</b>
    <ul>
        <li><b>G</b> becomes <b>C</b></li>
        <li><b>C</b> becomes <b>G</b></li>
        <li><b>T</b> becomes <b>A</b></li>
        <li><b>A</b> becomes <b>U</b> (Because RNA doesn't have T!)</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# Input
dna_input = st.text_input("Enter a DNA Sequence (e.g., TACGCG):", "TACGCG").upper()


# Logic
def transcribe_dna(sequence):
    mapping = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ""
    valid = True
    for base in sequence:
        if base in mapping:
            rna += mapping[base]
        elif base == " ":
            continue # Ignore spaces
        else:
            valid = False
            break
    return rna, valid


if dna_input:
    rna_result, is_valid = transcribe_dna(dna_input)
    
    col_dna, col_arrow, col_rna = st.columns([4, 1, 4])
    
    with col_dna:
        st.success(f"DNA: {dna_input}")
    
    with col_arrow:
        st.markdown("<h2 style='text-align: center;'>➡️</h2>", unsafe_allow_html=True)
        
    with col_rna:
        if is_valid:
            st.error(f"RNA: {rna_result}")
        else:
            st.warning("⚠️ Invalid DNA character detected! Use only A, T, C, or G.")


# --- Section 4: Quick Comparison Table ---
st.markdown("## 📊 Quick Comparison")


comparison_data = {
    "Feature": ["Number of Strands", "Sugar Type", "Unique Base", "Location", "Job"],
    "DNA 🧬": ["2 (Double Helix)", "Deoxyribose", "Thymine (T)", "Nucleus", "Stores Genetic Info"],
    "RNA 🧶": ["1 (Single Strand)", "Ribose", "Uracil (U)", "Nucleus & Cytoplasm", "Transfers Info/Makes Protein"]
}
st.table(comparison_data)


# --- Section 5: Quiz ---
st.markdown("## 🧠 Knowledge Check")


with st.expander("Question 1: Which base is found in RNA but NOT in DNA?"):
    q1 = st.radio("Select answer:", ["Adenine", "Thymine", "Uracil", "Guanine"], key="q1")
    if q1 == "Uracil":
        st.success("Correct! Uracil replaces Thymine in RNA.")
    elif q1:
        st.error("Try again! Look at the red card above.")


with st.expander("Question 2: If DNA is the 'Master Plan', what is RNA?"):
    q2 = st.radio("Select answer:", ["The Brick", "The Photocopy/Messenger", "The Builder", "The Cement"], key="q2")
    if q2 == "The Photocopy/Messenger":
        st.success("Correct! It carries the message out of the nucleus.")
    elif q2:
        st.error("Not quite.")


# --- Section 6: 3D Builder ---
st.divider()
st.markdown("## 🧬 Build Your Own 3D DNA Helix")
st.write("Use the buttons below to add base pairs. Watch the helix twist as it grows! You can click and drag the model to rotate it.")


# Initialize Session State for the DNA sequence
if 'dna_sequence' not in st.session_state:
    st.session_state.dna_sequence = []


# Functions to modify the DNA
def add_base_pair(pair):
    st.session_state.dna_sequence.append(pair)


def remove_last_pair():
    if len(st.session_state.dna_sequence) > 0:
        st.session_state.dna_sequence.pop()


def reset_sequence():
    st.session_state.dna_sequence = []


# Controls
b1, b2, b3, b4, b5, b6 = st.columns(6)
with b1: st.button("Add A-T", on_click=add_base_pair, args=('A-T',))
with b2: st.button("Add T-A", on_click=add_base_pair, args=('T-A',))
with b3: st.button("Add G-C", on_click=add_base_pair, args=('G-C',))
with b4: st.button("Add C-G", on_click=add_base_pair, args=('C-G',))
with b5: st.button("↩️ Undo", on_click=remove_last_pair)
with b6: st.button("🗑️ Reset", on_click=reset_sequence)


# 3D Plotting Logic
if st.session_state.dna_sequence:
    num_pairs = len(st.session_state.dna_sequence)
    
    # 1. Calculate Helix Coordinates
    # t is the angle, z is height
    t = np.linspace(0, num_pairs * 0.5, num_pairs)  # 0.5 radian twist per base (~28 degrees)
    z = np.linspace(0, num_pairs, num_pairs)
    radius = 2


    # Strand 1 (The Sugar-Phosphate Backbone)
    x1 = radius * np.cos(t)
    y1 = radius * np.sin(t)


    # Strand 2 (Anti-parallel, offset by PI)
    x2 = radius * np.cos(t + np.pi)
    y2 = radius * np.sin(t + np.pi)


    fig = go.Figure()


    # Draw Backbones
    fig.add_trace(go.Scatter3d(x=x1, y=y1, z=z, mode='lines', line=dict(color='gray', width=5), name='Backbone 1'))
    fig.add_trace(go.Scatter3d(x=x2, y=y2, z=z, mode='lines', line=dict(color='gray', width=5), name='Backbone 2'))


    # Draw Rungs (Base Pairs)
    # We iterate through the sequence to draw lines connecting the strands
    for i in range(num_pairs):
        pair_name = st.session_state.dna_sequence[i]
        
        # Color coding: A-T (Blue), T-A (Yellow), G-C (Green), C-G (Red)
        color_map = {'A-T': '#3498db', 'T-A': '#f1c40f', 'G-C': '#2ecc71', 'C-G': '#e74c3c'}
        color = color_map.get(pair_name, 'black')


        fig.add_trace(go.Scatter3d(
            x=[x1[i], x2[i]], 
            y=[y1[i], y2[i]], 
            z=[z[i], z[i]],
            mode='lines+markers',
            line=dict(color=color, width=5),
            marker=dict(size=5, color=color),
            name=f"BP {i+1}: {pair_name}",
            showlegend=False
        ))


    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.caption(f"Current Sequence Length: {num_pairs} Base Pairs")


else:
    st.info("The DNA strand is empty! Click the buttons above to start building your helix.")




st.divider()
st.caption("Created for Science Class | Powered by Python & Streamlit")