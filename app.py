import streamlit as st
import graphviz
import plotly.graph_objects as go
import numpy as np
import random
import time

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
    
    .game-card {
        background-color: #dff9fb;
        border: 2px dashed #22a6b3;
        padding: 20px;
        text-align: center;
        border-radius: 15px;
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

# --- Section 3: Interactive Lab Activities ---
st.markdown("## 🧪 Interactive Lab")

tab1, tab2, tab3 = st.tabs(["Part 1: Transcribe (DNA->RNA)", "Part 2: Translate (RNA->Protein)", "Part 3: Mini-Game"])

with tab1:
    st.markdown("### Transcription: Copy the Code")
    st.markdown("""
    <div class="info-card">
        <b>Rules:</b> G ↔️ C, T ➡️ A, A ➡️ U
    </div>
    """, unsafe_allow_html=True)

    # Input
    dna_input = st.text_input("Enter a DNA Sequence (try creating start codon TAC...):", "TACGCGCCA").upper()

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
        with col_dna: st.success(f"DNA: {dna_input}")
        with col_arrow: st.markdown("<h2 style='text-align: center;'>➡️</h2>", unsafe_allow_html=True)
        with col_rna:
            if is_valid:
                st.error(f"RNA: {rna_result}")
            else:
                st.warning("⚠️ Invalid DNA character detected! Use only A, T, C, or G.")

with tab2:
    st.markdown("### Translation: Build the Protein")
    st.write("Now, let's turn that RNA message into Amino Acids!")
    st.info("💡 Proteins are made of chains of Amino Acids. We read RNA in groups of 3 letters called **Codons**.")
    
    # Simplified Codon Map for Middle School
    codon_map = {
        'AUG': 'Start (Met)',
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
        # (This is a simplified list for demonstration)
    }
    
    rna_for_translation = st.text_input("Enter RNA Sequence (grouped by 3s usually):", rna_result if 'rna_result' in locals() and is_valid else "AUGCGC")
    
    if st.button("Translate to Protein"):
        # Split into codons
        codons = [rna_for_translation[i:i+3] for i in range(0, len(rna_for_translation), 3)]
        protein_chain = []
        
        for codon in codons:
            if len(codon) == 3:
                aa = codon_map.get(codon, "???")
                protein_chain.append(aa)
        
        st.write("### Resulting Protein Chain:")
        st.markdown(f"<h3 style='text-align: center; color: green;'>{' - '.join(protein_chain)}</h3>", unsafe_allow_html=True)
        if "STOP" in protein_chain:
            st.balloons()
            st.success("Protein Synthesis Complete!")

with tab3:
    st.markdown("### 🎮 Base Pairing Speed Challenge")
    st.write("How fast can you match the bases? (DNA Mode: A-T, C-G)")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_base' not in st.session_state:
        st.session_state.current_base = random.choice(['A', 'T', 'C', 'G'])

    st.markdown(f"""
    <div class="game-card">
        <h2>Target Base: <span style="font-size: 50px; color: #e74c3c;">{st.session_state.current_base}</span></h2>
        <h4>Score: {st.session_state.score}</h4>
    </div>
    """, unsafe_allow_html=True)

    def check_match(selected_base):
        target = st.session_state.current_base
        correct = False
        if target == 'A' and selected_base == 'T': correct = True
        elif target == 'T' and selected_base == 'A': correct = True
        elif target == 'C' and selected_base == 'G': correct = True
        elif target == 'G' and selected_base == 'C': correct = True
        
        if correct:
            st.session_state.score += 1
            st.toast("Correct! 🎉")
        else:
            st.session_state.score = max(0, st.session_state.score - 1)
            st.toast("Wrong! 💥", icon="❌")
        
        st.session_state.current_base = random.choice(['A', 'T', 'C', 'G'])

    cols = st.columns(4)
    with cols[0]: st.button("Adenine (A)", use_container_width=True, on_click=check_match, args=('A',))
    with cols[1]: st.button("Thymine (T)", use_container_width=True, on_click=check_match, args=('T',))
    with cols[2]: st.button("Cytosine (C)", use_container_width=True, on_click=check_match, args=('C',))
    with cols[3]: st.button("Guanine (G)", use_container_width=True, on_click=check_match, args=('G',))
    
    if st.button("Reset Score"):
        st.session_state.score = 0


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
