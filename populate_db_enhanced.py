from app import app, db, Topic

def add_enhanced_topics():
    # Unit 1: Chemistry of Life (Chapters 1-5)
    topics_unit1 = [
        {
            "title": "Introduction to Biology",
            "content": """
            <div class="content-section">
                <h3>Evolution, the Themes of Biology, and Scientific Inquiry</h3>
                <div class="diagram">
                    <img src="/static/images/levels_of_organization.svg" alt="Levels of Biological Organization">
                    <p class="caption">Figure 1.1: Levels of biological organization from molecules to the biosphere</p>
                </div>
                <ul>
                    <li>Five unifying themes of biology:
                        <ol>
                            <li>Organization: Hierarchical structure of life</li>
                            <li>Information: DNA as genetic material</li>
                            <li>Energy and Matter: Flow through living systems</li>
                            <li>Interactions: Between organisms and environment</li>
                            <li>Evolution: Unity and diversity of life</li>
                        </ol>
                    </li>
                    <li>Levels of biological organization:
                        <div class="diagram">
                            <img src="/static/images/levels_of_organization.svg" alt="Biological Hierarchy">
                            <p class="caption">Figure 1.2: Biological hierarchy showing emergent properties</p>
                        </div>
                    </li>
                    <li>Structure and function are correlated at all levels:
                        <ul>
                            <li>Molecular level: Protein structure determines function</li>
                            <li>Cellular level: Organelle structure matches function</li>
                            <li>Organism level: Body structure relates to function</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Scientific Method</h3>
                <div class="diagram">
                    <img src="/static/images/cell_cycle.svg" alt="Scientific Method">
                    <p class="caption">Figure 1.3: The scientific method cycle</p>
                </div>
                <ol>
                    <li>Observation and description of a phenomenon
                        <ul>
                            <li>Qualitative observations</li>
                            <li>Quantitative measurements</li>
                        </ul>
                    </li>
                    <li>Formulation of a hypothesis
                        <ul>
                            <li>Testable explanation</li>
                            <li>Null hypothesis</li>
                            <li>Alternative hypothesis</li>
                        </ul>
                    </li>
                    <li>Experimental design
                        <ul>
                            <li>Control groups</li>
                            <li>Independent variables</li>
                            <li>Dependent variables</li>
                            <li>Constants</li>
                        </ul>
                    </li>
                    <li>Data collection and analysis
                        <ul>
                            <li>Statistical analysis</li>
                            <li>Graphical representation</li>
                            <li>Error analysis</li>
                        </ul>
                    </li>
                    <li>Conclusion and communication
                        <ul>
                            <li>Peer review</li>
                            <li>Publication</li>
                            <li>Replication</li>
                        </ul>
                    </li>
                </ol>
            </div>
            """,
            "unit": 1
        },
        {
            "title": "The Chemical Context of Life",
            "content": """
            <div class="content-section">
                <h3>Elements and Compounds</h3>
                <div class="diagram">
                    <img src="/static/images/metabolic_pathways.svg" alt="Periodic Table">
                    <p class="caption">Figure 2.1: Essential elements in living organisms</p>
                </div>
                <ul>
                    <li>Major elements in living matter:
                        <table class="element-table">
                            <tr>
                                <th>Element</th>
                                <th>Symbol</th>
                                <th>Percentage</th>
                                <th>Function</th>
                            </tr>
                            <tr>
                                <td>Carbon</td>
                                <td>C</td>
                                <td>18.5%</td>
                                <td>Backbone of organic molecules</td>
                            </tr>
                            <tr>
                                <td>Hydrogen</td>
                                <td>H</td>
                                <td>9.5%</td>
                                <td>Component of water and organic molecules</td>
                            </tr>
                            <tr>
                                <td>Oxygen</td>
                                <td>O</td>
                                <td>65%</td>
                                <td>Component of water and organic molecules</td>
                            </tr>
                            <tr>
                                <td>Nitrogen</td>
                                <td>N</td>
                                <td>3.3%</td>
                                <td>Component of proteins and nucleic acids</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Chemical Bonds and Molecular Interactions</h3>
                <div class="diagram">
                    <img src="/static/images/fluid_mosaic.svg" alt="Chemical Bonds">
                    <p class="caption">Figure 2.2: Types of chemical bonds and their properties</p>
                </div>
                <ul>
                    <li>Covalent bonds:
                        <ul>
                            <li>Single, double, and triple bonds</li>
                            <li>Polar vs. nonpolar covalent bonds</li>
                            <li>Electronegativity differences</li>
                        </ul>
                    </li>
                    <li>Ionic bonds:
                        <ul>
                            <li>Cation and anion formation</li>
                            <li>Ionic compounds in solution</li>
                            <li>Electrolytes in biological systems</li>
                        </ul>
                    </li>
                    <li>Hydrogen bonds:
                        <ul>
                            <li>Water molecule interactions</li>
                            <li>Protein structure stabilization</li>
                            <li>DNA base pairing</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 1
        },
        {
            "title": "Carbon and the Molecular Diversity of Life",
            "content": """
            <h3>Carbon Chemistry</h3>
            <ul>
                <li>Carbon forms four covalent bonds</li>
                <li>Carbon skeletons vary in length and shape</li>
                <li>Functional groups determine chemical properties</li>
                <li>Isomers: structural, geometric, and enantiomers</li>
            </ul>
            
            <h3>Macromolecules</h3>
            <ul>
                <li>Carbohydrates: fuel and building material</li>
                <li>Lipids: diverse hydrophobic molecules</li>
                <li>Proteins: molecular tools of the cell</li>
                <li>Nucleic acids: information molecules</li>
                <li>Dehydration synthesis and hydrolysis</li>
            </ul>
            """,
            "unit": 1
        }
    ]

    # Unit 2: Cell Structure and Function (Chapters 6-7)
    topics_unit2 = [
        {
            "title": "A Tour of the Cell",
            "content": """
            <div class="content-section">
                <h3>Cell Theory and Microscopy</h3>
                <div class="diagram">
                    <img src="/static/images/cell_comparison.svg" alt="Cell Theory">
                    <p class="caption">Figure 6.1: The three principles of cell theory</p>
                </div>
                <ul>
                    <li>Cell Theory:
                        <ol>
                            <li>All living organisms are composed of cells</li>
                            <li>Cells are the basic units of structure and function</li>
                            <li>New cells arise from pre-existing cells</li>
                        </ol>
                    </li>
                    <li>Microscopy techniques:
                        <table class="element-table">
                            <tr>
                                <th>Type</th>
                                <th>Resolution</th>
                                <th>Advantages</th>
                                <th>Limitations</th>
                            </tr>
                            <tr>
                                <td>Light Microscope</td>
                                <td>200 nm</td>
                                <td>Live specimens, color images</td>
                                <td>Limited resolution</td>
                            </tr>
                            <tr>
                                <td>Electron Microscope</td>
                                <td>0.2 nm</td>
                                <td>High resolution</td>
                                <td>Dead specimens, black and white</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Prokaryotic vs Eukaryotic Cells</h3>
                <div class="diagram">
                    <img src="/static/images/cell_comparison.svg" alt="Cell Comparison">
                    <p class="caption">Figure 6.2: Comparison of prokaryotic and eukaryotic cells</p>
                </div>
                <ul>
                    <li>Prokaryotic cells:
                        <ul>
                            <li>No nucleus or membrane-bound organelles</li>
                            <li>Circular DNA in nucleoid region</li>
                            <li>Cell wall and capsule</li>
                            <li>Flagella and pili for movement</li>
                        </ul>
                    </li>
                    <li>Eukaryotic cells:
                        <ul>
                            <li>Membrane-bound nucleus</li>
                            <li>Complex endomembrane system</li>
                            <li>Mitochondria and chloroplasts</li>
                            <li>Cytoskeleton for support</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Organelles and Their Functions</h3>
                <div class="diagram">
                    <img src="/static/images/cell_comparison.svg" alt="Animal Cell">
                    <p class="caption">Figure 6.3: Structure of a typical animal cell</p>
                </div>
                <table class="element-table">
                    <tr>
                        <th>Organelle</th>
                        <th>Structure</th>
                        <th>Function</th>
                    </tr>
                    <tr>
                        <td>Nucleus</td>
                        <td>Double membrane, nucleolus</td>
                        <td>DNA storage, transcription</td>
                    </tr>
                    <tr>
                        <td>Endoplasmic Reticulum</td>
                        <td>Network of membranes</td>
                        <td>Protein synthesis, lipid production</td>
                    </tr>
                    <tr>
                        <td>Golgi Apparatus</td>
                        <td>Stack of flattened sacs</td>
                        <td>Protein modification, packaging</td>
                    </tr>
                    <tr>
                        <td>Mitochondria</td>
                        <td>Double membrane, cristae</td>
                        <td>ATP production, cellular respiration</td>
                    </tr>
                    <tr>
                        <td>Lysosomes</td>
                        <td>Membrane-bound vesicles</td>
                        <td>Digestion, waste processing</td>
                    </tr>
                </table>
            </div>
            """,
            "unit": 2
        },
        {
            "title": "Membrane Structure and Function",
            "content": """
            <div class="content-section">
                <h3>Membrane Structure</h3>
                <div class="diagram">
                    <img src="/static/images/fluid_mosaic.svg" alt="Fluid Mosaic Model">
                    <p class="caption">Figure 7.1: Fluid mosaic model of membrane structure</p>
                </div>
                <ul>
                    <li>Phospholipid bilayer:
                        <ul>
                            <li>Hydrophilic heads face outward</li>
                            <li>Hydrophobic tails face inward</li>
                            <li>Fluid nature allows movement</li>
                        </ul>
                    </li>
                    <li>Membrane proteins:
                        <table class="element-table">
                            <tr>
                                <th>Type</th>
                                <th>Location</th>
                                <th>Function</th>
                            </tr>
                            <tr>
                                <td>Integral</td>
                                <td>Embedded in bilayer</td>
                                <td>Transport, signaling</td>
                            </tr>
                            <tr>
                                <td>Peripheral</td>
                                <td>Surface of membrane</td>
                                <td>Support, communication</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Membrane Transport</h3>
                <div class="diagram">
                    <img src="/static/images/fluid_mosaic.svg" alt="Membrane Transport">
                    <p class="caption">Figure 7.2: Types of membrane transport</p>
                </div>
                <ul>
                    <li>Passive transport:
                        <ul>
                            <li>Diffusion: movement down concentration gradient</li>
                            <li>Osmosis: water movement across membrane</li>
                            <li>Facilitated diffusion: protein-assisted transport</li>
                        </ul>
                    </li>
                    <li>Active transport:
                        <ul>
                            <li>Primary active transport: ATP-powered pumps</li>
                            <li>Secondary active transport: coupled transport</li>
                            <li>Bulk transport: endocytosis and exocytosis</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 2
        }
    ]

    # Unit 3: Cellular Energetics (Chapters 8-10)
    topics_unit3 = [
        {
            "title": "An Introduction to Metabolism",
            "content": """
            <div class="content-section">
                <h3>Metabolic Pathways</h3>
                <div class="diagram">
                    <img src="/static/images/metabolic_pathways.svg" alt="Metabolic Pathways">
                    <p class="caption">Figure 8.1: Overview of metabolic pathways</p>
                </div>
                <ul>
                    <li>Types of metabolic pathways:
                        <table class="element-table">
                            <tr>
                                <th>Type</th>
                                <th>Description</th>
                                <th>Example</th>
                                <th>Energy Change</th>
                            </tr>
                            <tr>
                                <td>Catabolic</td>
                                <td>Breakdown of complex molecules</td>
                                <td>Cellular respiration</td>
                                <td>Releases energy</td>
                            </tr>
                            <tr>
                                <td>Anabolic</td>
                                <td>Building of complex molecules</td>
                                <td>Protein synthesis</td>
                                <td>Requires energy</td>
                            </tr>
                        </table>
                    </li>
                    <li>Bioenergetics:
                        <ul>
                            <li>Energy flow through living systems</li>
                            <li>ATP as energy currency</li>
                            <li>Redox reactions in metabolism</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Energy and Enzymes</h3>
                <div class="diagram">
                    <img src="/static/images/enzyme_action.svg" alt="Enzyme Action">
                    <p class="caption">Figure 8.2: Enzyme action and regulation</p>
                </div>
                <ul>
                    <li>Laws of thermodynamics:
                        <ol>
                            <li>First Law: Energy cannot be created or destroyed</li>
                            <li>Second Law: Entropy increases in spontaneous processes</li>
                        </ol>
                    </li>
                    <li>Enzyme structure and function:
                        <ul>
                            <li>Active site and substrate binding</li>
                            <li>Induced fit model</li>
                            <li>Factors affecting enzyme activity:
                                <ul>
                                    <li>Temperature</li>
                                    <li>pH</li>
                                    <li>Substrate concentration</li>
                                    <li>Inhibitors</li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 3
        },
        {
            "title": "Cellular Respiration and Fermentation",
            "content": """
            <div class="content-section">
                <h3>Overview of Cellular Respiration</h3>
                <div class="diagram">
                    <img src="/static/images/cellular_respiration.svg" alt="Cellular Respiration">
                    <p class="caption">Figure 9.1: Stages of cellular respiration</p>
                </div>
                <ul>
                    <li>Three main stages:
                        <table class="element-table">
                            <tr>
                                <th>Stage</th>
                                <th>Location</th>
                                <th>Input</th>
                                <th>Output</th>
                                <th>ATP Produced</th>
                            </tr>
                            <tr>
                                <td>Glycolysis</td>
                                <td>Cytoplasm</td>
                                <td>Glucose</td>
                                <td>2 Pyruvate</td>
                                <td>2 ATP (net)</td>
                            </tr>
                            <tr>
                                <td>Citric Acid Cycle</td>
                                <td>Mitochondrial Matrix</td>
                                <td>Pyruvate</td>
                                <td>CO2, NADH, FADH2</td>
                                <td>2 ATP</td>
                            </tr>
                            <tr>
                                <td>Oxidative Phosphorylation</td>
                                <td>Inner Mitochondrial Membrane</td>
                                <td>NADH, FADH2, O2</td>
                                <td>H2O, ATP</td>
                                <td>~28 ATP</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Fermentation</h3>
                <div class="diagram">
                    <img src="/static/images/fermentation.svg" alt="Fermentation">
                    <p class="caption">Figure 9.2: Types of fermentation</p>
                </div>
                <ul>
                    <li>Types of fermentation:
                        <ul>
                            <li>Alcohol fermentation:
                                <ul>
                                    <li>Pyruvate → Acetaldehyde → Ethanol</li>
                                    <li>Used by yeast and some bacteria</li>
                                </ul>
                            </li>
                            <li>Lactic acid fermentation:
                                <ul>
                                    <li>Pyruvate → Lactate</li>
                                    <li>Used by muscle cells and some bacteria</li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li>Comparison with aerobic respiration:
                        <ul>
                            <li>ATP yield: 2 vs 32 ATP</li>
                            <li>Oxygen requirement: anaerobic vs aerobic</li>
                            <li>Final electron acceptor: organic molecule vs oxygen</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 3
        },
        {
            "title": "Photosynthesis",
            "content": """
            <div class="content-section">
                <h3>Light Reactions</h3>
                <div class="diagram">
                    <img src="/static/images/light_reactions.svg" alt="Light Reactions">
                    <p class="caption">Figure 10.1: Light-dependent reactions of photosynthesis</p>
                </div>
                <ul>
                    <li>Chloroplast structure:
                        <ul>
                            <li>Thylakoid membranes</li>
                            <li>Grana and stroma</li>
                            <li>Photosystems I and II</li>
                        </ul>
                    </li>
                    <li>Light absorption and electron transport:
                        <table class="element-table">
                            <tr>
                                <th>Component</th>
                                <th>Function</th>
                                <th>Location</th>
                            </tr>
                            <tr>
                                <td>Photosystem II</td>
                                <td>Water splitting, electron excitation</td>
                                <td>Thylakoid membrane</td>
                            </tr>
                            <tr>
                                <td>Electron Transport Chain</td>
                                <td>Electron transfer, proton pumping</td>
                                <td>Thylakoid membrane</td>
                            </tr>
                            <tr>
                                <td>Photosystem I</td>
                                <td>NADP+ reduction</td>
                                <td>Thylakoid membrane</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Calvin Cycle</h3>
                <div class="diagram">
                    <img src="/static/images/calvin_cycle.svg" alt="Calvin Cycle">
                    <p class="caption">Figure 10.2: Calvin cycle reactions</p>
                </div>
                <ul>
                    <li>Three phases:
                        <ol>
                            <li>Carbon fixation:
                                <ul>
                                    <li>CO2 + RuBP → 3-PGA</li>
                                    <li>Catalyzed by rubisco</li>
                                </ul>
                            </li>
                            <li>Reduction:
                                <ul>
                                    <li>3-PGA → G3P</li>
                                    <li>Uses ATP and NADPH</li>
                                </ul>
                            </li>
                            <li>Regeneration:
                                <ul>
                                    <li>G3P → RuBP</li>
                                    <li>Uses ATP</li>
                                </ul>
                            </li>
                        </ol>
                    </li>
                    <li>Photorespiration and C4/CAM plants:
                        <ul>
                            <li>Photorespiration: wasteful process</li>
                            <li>C4 plants: spatial separation</li>
                            <li>CAM plants: temporal separation</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 3
        }
    ]

    # Unit 4: Cell Communication and Cell Cycle (Chapters 11-12)
    topics_unit4 = [
        {
            "title": "Cell Communication",
            "content": """
            <div class="content-section">
                <h3>Overview of Cell Signaling</h3>
                <div class="diagram">
                    <img src="/static/images/cell_signaling.svg" alt="Cell Signaling">
                    <p class="caption">Figure 11.1: The three stages of cell signaling</p>
                </div>
                <ul>
                    <li>Types of signaling:
                        <table class="element-table">
                            <tr>
                                <th>Type</th>
                                <th>Distance</th>
                                <th>Examples</th>
                            </tr>
                            <tr>
                                <td>Paracrine</td>
                                <td>Short-distance</td>
                                <td>Growth factors, cytokines</td>
                            </tr>
                            <tr>
                                <td>Endocrine</td>
                                <td>Long-distance</td>
                                <td>Hormones in bloodstream</td>
                            </tr>
                            <tr>
                                <td>Synaptic</td>
                                <td>Cell-to-cell</td>
                                <td>Neurotransmitters</td>
                            </tr>
                            <tr>
                                <td>Autocrine</td>
                                <td>Self</td>
                                <td>Immune cells</td>
                            </tr>
                        </table>
                    </li>
                    <li>Stages of cell signaling:
                        <ol>
                            <li>Reception: Signal binds to receptor</li>
                            <li>Transduction: Signal is converted and amplified</li>
                            <li>Response: Cell behavior changes</li>
                        </ol>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Signal Transduction Pathways</h3>
                <div class="diagram">
                    <img src="/static/images/signal_transduction.svg" alt="Signal Transduction">
                    <p class="caption">Figure 11.2: Major signal transduction pathways</p>
                </div>
                <ul>
                    <li>Receptor types:
                        <ul>
                            <li>G protein-coupled receptors (GPCRs):
                                <ul>
                                    <li>Seven transmembrane domains</li>
                                    <li>Activate G proteins when signal binds</li>
                                    <li>Examples: epinephrine, glucagon receptors</li>
                                </ul>
                            </li>
                            <li>Receptor tyrosine kinases (RTKs):
                                <ul>
                                    <li>Dimerize when signal binds</li>
                                    <li>Cross-phosphorylate tyrosines</li>
                                    <li>Examples: insulin, growth factor receptors</li>
                                </ul>
                            </li>
                            <li>Ion channel receptors:
                                <ul>
                                    <li>Open or close in response to signals</li>
                                    <li>Allow rapid ion flow</li>
                                    <li>Examples: nicotinic acetylcholine receptors</li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li>Second messengers:
                        <table class="element-table">
                            <tr>
                                <th>Second Messenger</th>
                                <th>Source</th>
                                <th>Function</th>
                            </tr>
                            <tr>
                                <td>cAMP</td>
                                <td>ATP (via adenylyl cyclase)</td>
                                <td>Activates protein kinase A</td>
                            </tr>
                            <tr>
                                <td>IP3/DAG</td>
                                <td>PIP2 (via phospholipase C)</td>
                                <td>Increases Ca2+, activates protein kinase C</td>
                            </tr>
                            <tr>
                                <td>Ca2+</td>
                                <td>ER/extracellular fluid</td>
                                <td>Activates calcium-dependent proteins</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>
            """,
            "unit": 4
        },
        {
            "title": "The Cell Cycle and Cell Division",
            "content": """
            <div class="content-section">
                <h3>Cell Cycle Overview</h3>
                <div class="diagram">
                    <img src="/static/images/cell_cycle.svg" alt="Cell Cycle">
                    <p class="caption">Figure 12.1: Phases of the cell cycle</p>
                </div>
                <ul>
                    <li>Cell cycle phases:
                        <table class="element-table">
                            <tr>
                                <th>Phase</th>
                                <th>Events</th>
                                <th>Duration (typical)</th>
                            </tr>
                            <tr>
                                <td>G1 (Gap 1)</td>
                                <td>Cell growth, protein synthesis</td>
                                <td>~11 hours</td>
                            </tr>
                            <tr>
                                <td>S (Synthesis)</td>
                                <td>DNA replication</td>
                                <td>~8 hours</td>
                            </tr>
                            <tr>
                                <td>G2 (Gap 2)</td>
                                <td>Preparation for mitosis</td>
                                <td>~4 hours</td>
                            </tr>
                            <tr>
                                <td>M (Mitosis)</td>
                                <td>Nuclear and cell division</td>
                                <td>~1 hour</td>
                            </tr>
                        </table>
                    </li>
                    <li>Cell cycle regulation:
                        <ul>
                            <li>Checkpoints:
                                <ul>
                                    <li>G1 checkpoint (restriction point): decides whether to commit to division</li>
                                    <li>G2 checkpoint: checks if DNA is properly replicated</li>
                                    <li>M checkpoint: ensures chromosomes are properly attached to spindle</li>
                                </ul>
                            </li>
                            <li>Cyclins and cyclin-dependent kinases (Cdks):
                                <ul>
                                    <li>Cyclin levels rise and fall during cell cycle</li>
                                    <li>Cdks are activated when bound to cyclins</li>
                                    <li>Different cyclin-Cdk complexes trigger different phases</li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Mitosis and Cytokinesis</h3>
                <div class="diagram">
                    <img src="/static/images/mitosis.svg" alt="Mitosis">
                    <p class="caption">Figure 12.2: Stages of mitosis</p>
                </div>
                <ul>
                    <li>Mitosis phases:
                        <ol>
                            <li>Prophase:
                                <ul>
                                    <li>Chromatin condenses into chromosomes</li>
                                    <li>Nuclear envelope breaks down</li>
                                    <li>Spindle apparatus forms</li>
                                </ul>
                            </li>
                            <li>Metaphase:
                                <ul>
                                    <li>Chromosomes align at equatorial plate</li>
                                    <li>Kinetochores attach to spindle fibers</li>
                                </ul>
                            </li>
                            <li>Anaphase:
                                <ul>
                                    <li>Sister chromatids separate</li>
                                    <li>Chromatids move to opposite poles</li>
                                </ul>
                            </li>
                            <li>Telophase:
                                <ul>
                                    <li>Nuclear envelopes re-form</li>
                                    <li>Chromosomes decondense</li>
                                    <li>Cytokinesis begins</li>
                                </ul>
                            </li>
                        </ol>
                    </li>
                    <li>Cytokinesis: Division of the cytoplasm
                        <ul>
                            <li>Animal cells: Contractile ring of actin pinches cell in two</li>
                            <li>Plant cells: Cell plate forms at the equator</li>
                        </ul>
                    </li>
                    <li>Cancer and cell cycle:
                        <ul>
                            <li>Loss of cell cycle control</li>
                            <li>Mutations in proto-oncogenes and tumor suppressor genes</li>
                            <li>Examples: p53, Ras, Rb</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 4
        }
    ]

    # Unit 5: Heredity (Chapters 13-15)
    topics_unit5 = [
        {
            "title": "Meiosis and Sexual Life Cycles",
            "content": """
            <div class="content-section">
                <h3>Meiosis Overview</h3>
                <div class="diagram">
                    <img src="/static/images/meiosis.svg" alt="Meiosis">
                    <p class="caption">Figure 13.1: Stages of meiosis I and meiosis II</p>
                </div>
                <ul>
                    <li>Sexual vs. asexual reproduction:
                        <table class="element-table">
                            <tr>
                                <th>Characteristic</th>
                                <th>Sexual Reproduction</th>
                                <th>Asexual Reproduction</th>
                            </tr>
                            <tr>
                                <td>Number of parents</td>
                                <td>Two</td>
                                <td>One</td>
                            </tr>
                            <tr>
                                <td>Genetic variation</td>
                                <td>High</td>
                                <td>Minimal</td>
                            </tr>
                            <tr>
                                <td>Cell division</td>
                                <td>Meiosis</td>
                                <td>Mitosis</td>
                            </tr>
                            <tr>
                                <td>Offspring</td>
                                <td>Genetically diverse</td>
                                <td>Genetically identical</td>
                            </tr>
                        </table>
                    </li>
                    <li>Homologous chromosomes:
                        <ul>
                            <li>Pairs of chromosomes with same length, centromere position, and gene loci</li>
                            <li>One from each parent</li>
                            <li>Contain same genes but potentially different alleles</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Meiosis I and II</h3>
                <div class="diagram">
                    <img src="/static/images/crossing_over.svg" alt="Crossing Over">
                    <p class="caption">Figure 13.2: Crossing over during prophase I</p>
                </div>
                <ul>
                    <li>Meiosis I: Reduction division
                        <ol>
                            <li>Prophase I:
                                <ul>
                                    <li>Homologous chromosomes pair up (synapsis)</li>
                                    <li>Crossing over occurs between non-sister chromatids</li>
                                    <li>Chiasmata form at crossover points</li>
                                </ul>
                            </li>
                            <li>Metaphase I:
                                <ul>
                                    <li>Homologous pairs align at metaphase plate</li>
                                    <li>Independent assortment of maternal and paternal chromosomes</li>
                                </ul>
                            </li>
                            <li>Anaphase I:
                                <ul>
                                    <li>Homologous chromosomes separate</li>
                                    <li>Sister chromatids remain attached</li>
                                </ul>
                            </li>
                            <li>Telophase I and Cytokinesis:
                                <ul>
                                    <li>Two haploid cells form</li>
                                    <li>Each chromosome still consists of two chromatids</li>
                                </ul>
                            </li>
                        </ol>
                    </li>
                    <li>Meiosis II: Equational division
                        <ol>
                            <li>Prophase II: Chromosomes condense</li>
                            <li>Metaphase II: Chromosomes align at metaphase plate</li>
                            <li>Anaphase II: Sister chromatids separate</li>
                            <li>Telophase II and Cytokinesis: Four haploid cells form</li>
                        </ol>
                    </li>
                </ul>
            </div>
            """,
            "unit": 5
        },
        {
            "title": "Mendelian Genetics",
            "content": """
            <div class="content-section">
                <h3>Mendel's Experiments</h3>
                <div class="diagram">
                    <img src="/static/images/mendel_experiment.svg" alt="Mendel's Experiment">
                    <p class="caption">Figure 14.1: Mendel's monohybrid cross experiment</p>
                </div>
                <ul>
                    <li>Mendel's approach:
                        <ul>
                            <li>Used pure-breeding pea plants</li>
                            <li>Studied one trait at a time (monohybrid cross)</li>
                            <li>Tracked traits through generations</li>
                            <li>Performed statistical analysis</li>
                        </ul>
                    </li>
                    <li>Mendel's laws:
                        <ol>
                            <li>Law of Segregation:
                                <ul>
                                    <li>Each individual has two alleles for each gene</li>
                                    <li>Alleles separate during gamete formation</li>
                                    <li>Each gamete receives only one allele</li>
                                </ul>
                            </li>
                            <li>Law of Independent Assortment:
                                <ul>
                                    <li>Alleles of different genes assort independently</li>
                                    <li>Applies to genes on different chromosomes</li>
                                </ul>
                            </li>
                        </ol>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Genetic Crosses</h3>
                <div class="diagram">
                    <img src="/static/images/punnett_square.svg" alt="Punnett Square">
                    <p class="caption">Figure 14.2: Punnett square showing a dihybrid cross</p>
                </div>
                <ul>
                    <li>Key genetic terms:
                        <table class="element-table">
                            <tr>
                                <th>Term</th>
                                <th>Definition</th>
                                <th>Example</th>
                            </tr>
                            <tr>
                                <td>Genotype</td>
                                <td>Genetic makeup</td>
                                <td>TT, Tt, tt</td>
                            </tr>
                            <tr>
                                <td>Phenotype</td>
                                <td>Observable traits</td>
                                <td>Tall, short</td>
                            </tr>
                            <tr>
                                <td>Homozygous</td>
                                <td>Two identical alleles</td>
                                <td>TT or tt</td>
                            </tr>
                            <tr>
                                <td>Heterozygous</td>
                                <td>Two different alleles</td>
                                <td>Tt</td>
                            </tr>
                            <tr>
                                <td>Dominant</td>
                                <td>Expressed in heterozygote</td>
                                <td>T (tall)</td>
                            </tr>
                            <tr>
                                <td>Recessive</td>
                                <td>Masked in heterozygote</td>
                                <td>t (short)</td>
                            </tr>
                        </table>
                    </li>
                    <li>Types of genetic crosses:
                        <ul>
                            <li>Monohybrid cross: One trait (e.g., Tt × Tt)</li>
                            <li>Dihybrid cross: Two traits (e.g., TtRr × TtRr)</li>
                            <li>Test cross: Unknown × recessive (e.g., T? × tt)</li>
                        </ul>
                    </li>
                    <li>Probability in genetics:
                        <ul>
                            <li>Product rule: Probability of two independent events = product of individual probabilities</li>
                            <li>Sum rule: Probability of either of two mutually exclusive events = sum of individual probabilities</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 5
        },
        {
            "title": "Chromosomal Basis of Inheritance",
            "content": """
            <div class="content-section">
                <h3>Chromosome Theory</h3>
                <div class="diagram">
                    <img src="/static/images/sex_chromosomes.svg" alt="Sex Chromosomes">
                    <p class="caption">Figure 15.1: X and Y sex chromosomes</p>
                </div>
                <ul>
                    <li>Chromosome theory of inheritance:
                        <ul>
                            <li>Genes are located on chromosomes</li>
                            <li>Chromosomes segregate during meiosis</li>
                            <li>Each pair of homologous chromosomes carries the same genes</li>
                        </ul>
                    </li>
                    <li>Sex chromosomes and determination:
                        <table class="element-table">
                            <tr>
                                <th>System</th>
                                <th>Female</th>
                                <th>Male</th>
                                <th>Examples</th>
                            </tr>
                            <tr>
                                <td>XX-XY</td>
                                <td>XX</td>
                                <td>XY</td>
                                <td>Humans, most mammals</td>
                            </tr>
                            <tr>
                                <td>ZZ-ZW</td>
                                <td>ZW</td>
                                <td>ZZ</td>
                                <td>Birds, some reptiles</td>
                            </tr>
                            <tr>
                                <td>XX-XO</td>
                                <td>XX</td>
                                <td>XO</td>
                                <td>Some insects</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Linkage and Recombination</h3>
                <div class="diagram">
                    <img src="/static/images/linkage_map.svg" alt="Linkage Map">
                    <p class="caption">Figure 15.2: Genetic linkage map</p>
                </div>
                <ul>
                    <li>Linked genes:
                        <ul>
                            <li>Genes on same chromosome tend to be inherited together</li>
                            <li>Linkage strength depends on distance between genes</li>
                            <li>Complete linkage: genes always inherited together</li>
                        </ul>
                    </li>
                    <li>Genetic recombination:
                        <ul>
                            <li>Crossing over breaks linkage</li>
                            <li>Recombination frequency used to map genes</li>
                            <li>1% recombination frequency ≈ 1 map unit (centimorgan)</li>
                        </ul>
                    </li>
                    <li>Chromosomal mutations:
                        <ul>
                            <li>Deletion: Loss of genetic material</li>
                            <li>Duplication: Repetition of segment</li>
                            <li>Inversion: Reversal of segment</li>
                            <li>Translocation: Movement to different chromosome</li>
                            <li>Nondisjunction: Failure of chromosomes to separate</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 5
        }
    ]

    # Unit 6: Gene Expression and Regulation (Chapters 16-18)
    topics_unit6 = [
        {
            "title": "The Molecular Basis of Inheritance",
            "content": """
            <div class="content-section">
                <h3>DNA Structure and Replication</h3>
                <div class="diagram">
                    <img src="/static/images/dna_structure.svg" alt="DNA Structure">
                    <p class="caption">Figure 16.1: DNA double helix structure showing base pairing and key enzymes</p>
                </div>
                <ul>
                    <li>DNA structure:
                        <ul>
                            <li>Double helix with complementary base pairing (A-T, G-C)</li>
                            <li>Antiparallel strands (5' to 3' direction)</li>
                            <li>Sugar-phosphate backbone with hydrogen-bonded base pairs</li>
                            <li>Major and minor grooves</li>
                        </ul>
                    </li>
                    <li>Key enzymes:
                        <ul>
                            <li>DNA Polymerase: Adds new nucleotides during replication</li>
                            <li>Helicase: Unwinds the double helix</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>DNA Replication Process</h3>
                <div class="diagram">
                    <img src="/static/images/dna_replication.svg" alt="DNA Replication">
                    <p class="caption">Figure 16.2: Semi-conservative DNA replication</p>
                </div>
                <ul>
                    <li>Replication process:
                        <table class="element-table">
                            <tr>
                                <th>Step</th>
                                <th>Enzymes</th>
                                <th>Function</th>
                            </tr>
                            <tr>
                                <td>Initiation</td>
                                <td>Helicase, Primase</td>
                                <td>Unwinds DNA, creates RNA primer</td>
                            </tr>
                            <tr>
                                <td>Elongation</td>
                                <td>DNA Polymerase III</td>
                                <td>Adds nucleotides to growing strand</td>
                            </tr>
                            <tr>
                                <td>Termination</td>
                                <td>DNA Polymerase I, Ligase</td>
                                <td>Removes primers, joins Okazaki fragments</td>
                            </tr>
                        </table>
                    </li>
                    <li>Replication features:
                        <ul>
                            <li>Leading and lagging strands</li>
                            <li>Okazaki fragments</li>
                            <li>Proofreading and repair mechanisms</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 6
        },
        {
            "title": "Gene Expression and Regulation",
            "content": """
<h2>Unit 6: Gene Expression and Regulation</h2>

<h3>DNA Structure and Replication</h3>
<img src="{{ url_for('static', filename='images/dna_structure.svg') }}" alt="DNA Structure" class="diagram">
<p class="caption">Figure 6.1: DNA Double Helix Structure with Key Enzymes</p>

<p>DNA (Deoxyribonucleic Acid) is the molecule that carries genetic information in all living organisms. Its structure consists of:</p>
<ul>
    <li>Double helix formation with sugar-phosphate backbones</li>
    <li>Complementary base pairing (A-T, G-C)</li>
    <li>Key enzymes involved in replication:
        <ul>
            <li>DNA Polymerase: Synthesizes new DNA strands</li>
            <li>Helicase: Unwinds the double helix</li>
            <li>Topoisomerase: Prevents supercoiling</li>
            <li>Ligase: Joins Okazaki fragments</li>
        </ul>
    </li>
</ul>

<h3>Transcription and Translation</h3>
<img src="{{ url_for('static', filename='images/transcription.svg') }}" alt="Transcription Process" class="diagram">
<p class="caption">Figure 6.2: The Process of Transcription</p>

<p>The central dogma of molecular biology describes the flow of genetic information:</p>
<ol>
    <li>Transcription: DNA → RNA
        <ul>
            <li>Initiation: RNA polymerase binds to promoter</li>
            <li>Elongation: RNA strand synthesis</li>
            <li>Termination: Release of RNA transcript</li>
        </ul>
    </li>
    <li>Translation: RNA → Protein
        <ul>
            <li>mRNA codons specify amino acids</li>
            <li>tRNA brings amino acids to ribosome</li>
            <li>Ribosome catalyzes peptide bond formation</li>
        </ul>
    </li>
</ol>

<h3>Regulation of Gene Expression</h3>
<img src="{{ url_for('static', filename='images/signal_transduction.svg') }}" alt="Signal Transduction" class="diagram">
<p class="caption">Figure 6.3: Signal Transduction Pathways</p>

<p>Gene expression is tightly regulated through multiple mechanisms:</p>
<ul>
    <li>Transcriptional Regulation
        <ul>
            <li>Transcription factors
                <ul>
                    <li>General transcription factors: Required for all genes</li>
                    <li>Specific transcription factors: Regulate specific genes</li>
                    <li>Activators and repressors</li>
                </ul>
            </li>
            <li>Enhancers and silencers
                <ul>
                    <li>Enhancers: Increase transcription</li>
                    <li>Silencers: Decrease transcription</li>
                    <li>Can be located far from the gene</li>
                </ul>
            </li>
            <li>Chromatin remodeling
                <ul>
                    <li>Histone modifications (acetylation, methylation)</li>
                    <li>DNA methylation</li>
                    <li>Chromatin structure changes</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Post-transcriptional Regulation
        <ul>
            <li>RNA processing and splicing
                <ul>
                    <li>5' cap addition</li>
                    <li>3' poly-A tail addition</li>
                    <li>Intron removal and exon splicing</li>
                    <li>Alternative splicing</li>
                </ul>
            </li>
            <li>mRNA stability
                <ul>
                    <li>mRNA degradation pathways</li>
                    <li>RNA interference (RNAi)</li>
                    <li>MicroRNAs and small interfering RNAs</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Translational and Post-translational Regulation
        <ul>
            <li>Protein modification
                <ul>
                    <li>Phosphorylation</li>
                    <li>Glycosylation</li>
                    <li>Ubiquitination</li>
                </ul>
            </li>
            <li>Protein degradation
                <ul>
                    <li>Proteasome pathway</li>
                    <li>Lysosomal degradation</li>
                    <li>Autophagy</li>
                </ul>
            </li>
            <li>Feedback inhibition
                <ul>
                    <li>Allosteric regulation</li>
                    <li>Competitive inhibition</li>
                    <li>Non-competitive inhibition</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Mutations and Genetic Variation</h3>
<p>Genetic variation arises through:</p>
<ul>
    <li>Point mutations
        <ul>
            <li>Substitutions: Silent, missense, nonsense</li>
            <li>Insertions and deletions: Frameshift mutations</li>
        </ul>
    </li>
    <li>Chromosomal mutations
        <ul>
            <li>Duplications: Gene family evolution</li>
            <li>Inversions: Altered gene order</li>
            <li>Translocations: Chromosome rearrangements</li>
        </ul>
    </li>
    <li>Gene flow and genetic drift
        <ul>
            <li>Migration between populations</li>
            <li>Founder effect</li>
            <li>Bottleneck effect</li>
        </ul>
    </li>
    <li>Horizontal gene transfer
        <ul>
            <li>Transformation</li>
            <li>Transduction</li>
            <li>Conjugation</li>
        </ul>
    </li>
</ul>

<h3>Biotechnology and Genetic Engineering</h3>
<p>Modern techniques in genetic manipulation include:</p>
<ul>
    <li>PCR (Polymerase Chain Reaction)
        <ul>
            <li>Denaturation, annealing, extension</li>
            <li>Exponential amplification</li>
            <li>Applications in research and diagnostics</li>
        </ul>
    </li>
    <li>Gel electrophoresis
        <ul>
            <li>DNA fragment separation</li>
            <li>Size determination</li>
            <li>Southern blotting</li>
        </ul>
    </li>
    <li>DNA sequencing
        <ul>
            <li>Sanger sequencing</li>
            <li>Next-generation sequencing</li>
            <li>Whole genome sequencing</li>
        </ul>
    </li>
    <li>CRISPR-Cas9 gene editing
        <ul>
            <li>Targeted DNA cleavage</li>
            <li>Gene knockout and knock-in</li>
            <li>Therapeutic applications</li>
        </ul>
    </li>
    <li>Recombinant DNA technology
        <ul>
            <li>Plasmid vectors</li>
            <li>Gene cloning</li>
            <li>Transgenic organisms</li>
        </ul>
    </li>
</ul>
"""
        },
        {
            "title": "Evolution by Natural Selection",
            "content": """
<h2>Unit 7: Evolution by Natural Selection</h2>

<h3>Darwin's Theory of Evolution</h3>
<img src="{{ url_for('static', filename='images/evolution_tree.svg') }}" alt="Evolutionary Tree" class="diagram">
<p class="caption">Figure 7.1: Phylogenetic tree showing evolutionary relationships</p>

<p>Charles Darwin's theory of evolution by natural selection is based on four key principles:</p>
<ol>
    <li>Variation exists in populations
        <ul>
            <li>Genetic variation: Mutations, recombination</li>
            <li>Phenotypic variation: Observable traits</li>
            <li>Environmental variation: Different selective pressures</li>
        </ul>
    </li>
    <li>Some variations are heritable
        <ul>
            <li>DNA as the genetic material</li>
            <li>Mendelian inheritance patterns</li>
            <li>Polygenic traits and continuous variation</li>
        </ul>
    </li>
    <li>More offspring are produced than can survive
        <ul>
            <li>Exponential population growth potential</li>
            <li>Limited resources and competition</li>
            <li>Density-dependent factors</li>
        </ul>
    </li>
    <li>Individuals with favorable traits survive and reproduce
        <ul>
            <li>Differential reproductive success</li>
            <li>Adaptation to environment</li>
            <li>Fitness and selection</li>
        </ul>
    </li>
</ol>

<h3>Evidence for Evolution</h3>
<p>Multiple lines of evidence support the theory of evolution:</p>
<ul>
    <li>Fossil Record
        <ul>
            <li>Transitional forms
                <ul>
                    <li>Tiktaalik: Fish to amphibian</li>
                    <li>Archaeopteryx: Dinosaur to bird</li>
                    <li>Whale evolution sequence</li>
                </ul>
            </li>
            <li>Stratigraphy and dating
                <ul>
                    <li>Radiometric dating</li>
                    <li>Index fossils</li>
                    <li>Geological time scale</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Comparative Anatomy
        <ul>
            <li>Homologous structures
                <ul>
                    <li>Limb bones in vertebrates</li>
                    <li>Pentadactyl limb pattern</li>
                    <li>Vestigial structures</li>
                </ul>
            </li>
            <li>Analogous structures
                <ul>
                    <li>Convergent evolution</li>
                    <li>Wings in bats, birds, and insects</li>
                    <li>Eyes in vertebrates and cephalopods</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Molecular Biology
        <ul>
            <li>DNA and protein sequences
                <ul>
                    <li>Universal genetic code</li>
                    <li>Conserved genes and proteins</li>
                    <li>Molecular clocks</li>
                </ul>
            </li>
            <li>Comparative genomics
                <ul>
                    <li>Gene families</li>
                    <li>Pseudogenes</li>
                    <li>Mobile genetic elements</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Mechanisms of Evolution</h3>
<img src="{{ url_for('static', filename='images/natural_selection.svg') }}" alt="Natural Selection" class="diagram">
<p class="caption">Figure 7.2: Types of Natural Selection</p>

<p>Evolution occurs through several mechanisms:</p>
<ul>
    <li>Natural Selection
        <ul>
            <li>Directional Selection
                <ul>
                    <li>Favors one extreme phenotype</li>
                    <li>Example: Peppered moth color change</li>
                    <li>Results in shift in population mean</li>
                </ul>
            </li>
            <li>Stabilizing Selection
                <ul>
                    <li>Favors intermediate phenotypes</li>
                    <li>Example: Human birth weight</li>
                    <li>Reduces variation in population</li>
                </ul>
            </li>
            <li>Disruptive Selection
                <ul>
                    <li>Favors both extremes</li>
                    <li>Example: African seedcracker finch</li>
                    <li>Can lead to speciation</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Genetic Drift
        <ul>
            <li>Founder Effect
                <ul>
                    <li>Small group establishes new population</li>
                    <li>Reduced genetic variation</li>
                    <li>Example: Amish population</li>
                </ul>
            </li>
            <li>Bottleneck Effect
                <ul>
                    <li>Population size drastically reduced</li>
                    <li>Loss of genetic diversity</li>
                    <li>Example: Cheetah population</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Gene Flow
        <ul>
            <li>Migration between populations
                <ul>
                    <li>Introduction of new alleles</li>
                    <li>Reduction of genetic differences</li>
                    <li>Example: Human migration patterns</li>
                </ul>
            </li>
            <li>Hybridization
                <ul>
                    <li>Interspecies gene transfer</li>
                    <li>Example: Hybrid zones in birds</li>
                    <li>Impact on speciation</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Mutation
        <ul>
            <li>Point mutations
                <ul>
                    <li>Single nucleotide changes</li>
                    <li>Impact on protein function</li>
                    <li>Example: Sickle cell anemia</li>
                </ul>
            </li>
            <li>Chromosomal mutations
                <ul>
                    <li>Duplications and deletions</li>
                    <li>Inversions and translocations</li>
                    <li>Example: Human chromosome 2 fusion</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Speciation and Macroevolution</h3>
<p>The process of speciation and large-scale evolutionary patterns:</p>
<ul>
    <li>Types of Speciation
        <ul>
            <li>Allopatric Speciation
                <ul>
                    <li>Geographic isolation</li>
                    <li>Example: Galapagos finches</li>
                    <li>Role of vicariance and dispersal</li>
                </ul>
            </li>
            <li>Sympatric Speciation
                <ul>
                    <li>Reproductive isolation without geographic separation</li>
                    <li>Example: Cichlid fish in African lakes</li>
                    <li>Polyploidy in plants</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Reproductive Isolation
        <ul>
            <li>Prezygotic Barriers
                <ul>
                    <li>Habitat isolation</li>
                    <li>Temporal isolation</li>
                    <li>Behavioral isolation</li>
                    <li>Mechanical isolation</li>
                    <li>Gametic isolation</li>
                </ul>
            </li>
            <li>Postzygotic Barriers
                <ul>
                    <li>Reduced hybrid viability</li>
                    <li>Reduced hybrid fertility</li>
                    <li>Hybrid breakdown</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Patterns of Evolution
        <ul>
            <li>Gradualism vs. Punctuated Equilibrium
                <ul>
                    <li>Gradual change over time</li>
                    <li>Rapid change followed by stasis</li>
                    <li>Fossil record evidence</li>
                </ul>
            </li>
            <li>Adaptive Radiation
                <ul>
                    <li>Rapid diversification</li>
                    <li>Example: Darwin's finches</li>
                    <li>Ecological opportunity</li>
                </ul>
            </li>
            <li>Convergent Evolution
                <ul>
                    <li>Similar adaptations in unrelated species</li>
                    <li>Example: Wings in bats and birds</li>
                    <li>Similar selective pressures</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
"""
        },
        {
            "title": "Evolution by Natural Selection",
            "content": """
            <div class="content-section">
                <h3>Darwin's Theory</h3>
                <div class="diagram">
                    <img src="/static/images/evolution_tree.svg" alt="Evolutionary Tree">
                    <p class="caption">Figure 22.1: Phylogenetic tree showing evolutionary relationships</p>
                </div>
                <ul>
                    <li>Key principles:
                        <ol>
                            <li>Variation exists in populations</li>
                            <li>Some variations are heritable</li>
                            <li>More offspring are produced than can survive</li>
                            <li>Individuals with favorable traits survive and reproduce</li>
                        </ol>
                    </li>
                    <li>Evidence for evolution:
                        <table class="element-table">
                            <tr>
                                <th>Type</th>
                                <th>Description</th>
                                <th>Example</th>
                            </tr>
                            <tr>
                                <td>Fossil Record</td>
                                <td>Transitional forms</td>
                                <td>Tiktaalik (fish to amphibian)</td>
                            </tr>
                            <tr>
                                <td>Comparative Anatomy</td>
                                <td>Homologous structures</td>
                                <td>Limb bones in vertebrates</td>
                            </tr>
                            <tr>
                                <td>Molecular Biology</td>
                                <td>DNA similarities</td>
                                <td>Cytochrome c in mitochondria</td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Mechanisms of Evolution</h3>
                <div class="diagram">
                    <img src="/static/images/natural_selection.svg" alt="Natural Selection">
                    <p class="caption">Figure 22.2: Types of natural selection</p>
                </div>
                <ul>
                    <li>Types of selection:
                        <ul>
                            <li>Directional: Favors one extreme</li>
                            <li>Stabilizing: Favors intermediate</li>
                            <li>Disruptive: Favors both extremes</li>
                        </ul>
                    </li>
                    <li>Other mechanisms:
                        <ul>
                            <li>Genetic drift: Random changes in allele frequencies</li>
                            <li>Gene flow: Movement of alleles between populations</li>
                            <li>Mutation: Source of new genetic variation</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            "unit": 7
        }
    ]

    # Unit 8: Ecology (Chapters 50-55)
    topics_unit8 = [
        {
            "title": "Ecology",
            "content": """
<h2>Unit 8: Ecology</h2>

<h3>Ecological Organization</h3>
<img src="{{ url_for('static', filename='images/levels_of_organization.svg') }}" alt="Ecological Organization" class="diagram">
<p class="caption">Figure 8.1: Levels of ecological organization</p>

<p>Ecology studies the interactions between organisms and their environment at multiple levels:</p>
<ul>
    <li>Organismal Ecology
        <ul>
            <li>Physiological adaptations
                <ul>
                    <li>Temperature regulation</li>
                    <li>Water balance</li>
                    <li>Energy acquisition</li>
                </ul>
            </li>
            <li>Behavioral adaptations
                <ul>
                    <li>Foraging strategies</li>
                    <li>Reproductive behaviors</li>
                    <li>Social interactions</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Population Ecology
        <ul>
            <li>Population dynamics
                <ul>
                    <li>Growth patterns</li>
                    <li>Age structure</li>
                    <li>Density and distribution</li>
                </ul>
            </li>
            <li>Population regulation
                <ul>
                    <li>Density-dependent factors</li>
                    <li>Density-independent factors</li>
                    <li>Carrying capacity</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Community Ecology
        <ul>
            <li>Species interactions
                <ul>
                    <li>Competition</li>
                    <li>Predation</li>
                    <li>Symbiosis</li>
                </ul>
            </li>
            <li>Community structure
                <ul>
                    <li>Species diversity</li>
                    <li>Trophic levels</li>
                    <li>Succession</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Ecosystem Ecology
        <ul>
            <li>Energy flow
                <ul>
                    <li>Primary production</li>
                    <li>Food webs</li>
                    <li>Energy pyramids</li>
                </ul>
            </li>
            <li>Biogeochemical cycles
                <ul>
                    <li>Carbon cycle</li>
                    <li>Nitrogen cycle</li>
                    <li>Water cycle</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Energy Flow and Trophic Levels</h3>
<img src="{{ url_for('static', filename='images/ecosystem_energy.svg') }}" alt="Energy Flow" class="diagram">
<p class="caption">Figure 8.2: Energy flow through an ecosystem</p>

<p>Energy flows through ecosystems in a one-way direction:</p>
<ul>
    <li>Primary Production
        <ul>
            <li>Photosynthesis
                <ul>
                    <li>Light energy conversion</li>
                    <li>Carbon fixation</li>
                    <li>Net primary productivity</li>
                </ul>
            </li>
            <li>Chemosynthesis
                <ul>
                    <li>Deep-sea vent communities</li>
                    <li>Hydrogen sulfide oxidation</li>
                    <li>Extremophile ecosystems</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Trophic Levels
        <ul>
            <li>Producers (Autotrophs)
                <ul>
                    <li>Plants</li>
                    <li>Algae</li>
                    <li>Cyanobacteria</li>
                </ul>
            </li>
            <li>Consumers (Heterotrophs)
                <ul>
                    <li>Primary consumers (Herbivores)</li>
                    <li>Secondary consumers (Carnivores)</li>
                    <li>Tertiary consumers (Top predators)</li>
                </ul>
            </li>
            <li>Decomposers
                <ul>
                    <li>Bacteria</li>
                    <li>Fungi</li>
                    <li>Detritivores</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Energy Transfer
        <ul>
            <li>10% Rule
                <ul>
                    <li>Energy loss between levels</li>
                    <li>Heat dissipation</li>
                    <li>Metabolic costs</li>
                </ul>
            </li>
            <li>Ecological Pyramids
                <ul>
                    <li>Energy pyramid</li>
                    <li>Biomass pyramid</li>
                    <li>Numbers pyramid</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Population Dynamics</h3>
<img src="{{ url_for('static', filename='images/population_growth.svg') }}" alt="Population Growth" class="diagram">
<p class="caption">Figure 8.3: Population growth models</p>

<p>Population dynamics examines changes in population size and structure:</p>
<ul>
    <li>Population Growth Models
        <ul>
            <li>Exponential Growth
                <ul>
                    <li>Unlimited resources</li>
                    <li>J-shaped curve</li>
                    <li>Intrinsic growth rate</li>
                </ul>
            </li>
            <li>Logistic Growth
                <ul>
                    <li>Limited resources</li>
                    <li>S-shaped curve</li>
                    <li>Carrying capacity</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Population Regulation
        <ul>
            <li>Density-Dependent Factors
                <ul>
                    <li>Competition for resources</li>
                    <li>Predation</li>
                    <li>Disease</li>
                </ul>
            </li>
            <li>Density-Independent Factors
                <ul>
                    <li>Weather events</li>
                    <li>Natural disasters</li>
                    <li>Human activities</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Life History Strategies
        <ul>
            <li>r-selected Species
                <ul>
                    <li>Many offspring</li>
                    <li>Little parental care</li>
                    <li>Early maturity</li>
                </ul>
            </li>
            <li>K-selected Species
                <ul>
                    <li>Few offspring</li>
                    <li>Extensive parental care</li>
                    <li>Late maturity</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Community Interactions</h3>
<p>Communities are shaped by complex interactions between species:</p>
<ul>
    <li>Competition
        <ul>
            <li>Intraspecific Competition
                <ul>
                    <li>Same species</li>
                    <li>Resource partitioning</li>
                    <li>Territoriality</li>
                </ul>
            </li>
            <li>Interspecific Competition
                <ul>
                    <li>Different species</li>
                    <li>Competitive exclusion</li>
                    <li>Character displacement</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Predation
        <ul>
            <li>Predator-Prey Dynamics
                <ul>
                    <li>Population cycles</li>
                    <li>Defense mechanisms</li>
                    <li>Co-evolution</li>
                </ul>
            </li>
            <li>Herbivory
                <ul>
                    <li>Plant defenses</li>
                    <li>Chemical deterrents</li>
                    <li>Mutualistic relationships</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Symbiosis
        <ul>
            <li>Mutualism
                <ul>
                    <li>Both species benefit</li>
                    <li>Example: Pollination</li>
                    <li>Example: Mycorrhizae</li>
                </ul>
            </li>
            <li>Commensalism
                <ul>
                    <li>One benefits, other unaffected</li>
                    <li>Example: Epiphytes</li>
                    <li>Example: Barnacles on whales</li>
                </ul>
            </li>
            <li>Parasitism
                <ul>
                    <li>One benefits, other harmed</li>
                    <li>Example: Tapeworms</li>
                    <li>Example: Pathogenic bacteria</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

<h3>Ecosystem Services</h3>
<p>Ecosystems provide essential services that support life:</p>
<ul>
    <li>Provisioning Services
        <ul>
            <li>Food production</li>
            <li>Fresh water</li>
            <li>Raw materials</li>
            <li>Medicinal resources</li>
        </ul>
    </li>
    <li>Regulating Services
        <ul>
            <li>Climate regulation</li>
            <li>Water purification</li>
            <li>Pollination</li>
            <li>Pest control</li>
        </ul>
    </li>
    <li>Supporting Services
        <ul>
            <li>Nutrient cycling</li>
            <li>Soil formation</li>
            <li>Primary production</li>
            <li>Habitat provision</li>
        </ul>
    </li>
    <li>Cultural Services
        <ul>
            <li>Recreation</li>
            <li>Aesthetic value</li>
            <li>Spiritual significance</li>
            <li>Educational opportunities</li>
        </ul>
    </li>
</ul>
"""
        },
        {
            "title": "Population Ecology",
            "content": """
            <div class="content-section">
                <h3>Population Growth</h3>
                <div class="diagram">
                    <img src="/static/images/population_growth.svg" alt="Population Growth">
                    <p class="caption">Figure 51.1: Population growth models</p>
                </div>
                <ul>
                    <li>Exponential growth: J-shaped curve</li>
                    <li>Logistic growth: S-shaped curve</li>
                    <li>Carrying capacity: Maximum sustainable population</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Population Regulation</h3>
                <div class="diagram">
                    <img src="/static/images/population_regulation.svg" alt="Population Regulation">
                    <p class="caption">Figure 51.2: Types of population regulation</p>
                </div>
                <ul>
                    <li>Density-dependent factors</li>
                    <li>Density-independent factors</li>
                    <li>Carrying capacity</li>
                </ul>
            </div>
            """,
            "unit": 8
        },
        {
            "title": "Community Ecology",
            "content": """
            <div class="content-section">
                <h3>Species Interactions</h3>
                <div class="diagram">
                    <img src="/static/images/species_interactions.svg" alt="Species Interactions">
                    <p class="caption">Figure 52.1: Types of species interactions</p>
                </div>
                <ul>
                    <li>Competition</li>
                    <li>Predation</li>
                    <li>Symbiosis</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Community Structure</h3>
                <div class="diagram">
                    <img src="/static/images/community_structure.svg" alt="Community Structure">
                    <p class="caption">Figure 52.2: Structure of a community</p>
                </div>
                <ul>
                    <li>Species diversity</li>
                    <li>Trophic levels</li>
                    <li>Succession</li>
                </ul>
            </div>
            """,
            "unit": 8
        },
        {
            "title": "Ecosystem Ecology",
            "content": """
            <div class="content-section">
                <h3>Energy Flow</h3>
                <div class="diagram">
                    <img src="/static/images/ecosystem_energy.svg" alt="Energy Flow">
                    <p class="caption">Figure 53.1: Energy flow through an ecosystem</p>
                </div>
                <ul>
                    <li>Primary production</li>
                    <li>Food webs</li>
                    <li>Energy pyramids</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>Biogeochemical Cycles</h3>
                <div class="diagram">
                    <img src="/static/images/biogeochemical_cycles.svg" alt="Biogeochemical Cycles">
                    <p class="caption">Figure 53.2: Biogeochemical cycles</p>
                </div>
                <ul>
                    <li>Carbon cycle</li>
                    <li>Nitrogen cycle</li>
                    <li>Water cycle</li>
                </ul>
            </div>
            """,
            "unit": 8
        }
    ]

    # Combine all topics
    all_topics = (topics_unit1 + topics_unit2 + topics_unit3 + topics_unit4 +
                 topics_unit5 + topics_unit6 + topics_unit7 + topics_unit8)
    
    # Add topics to database
    for topic_data in all_topics:
        topic = Topic(**topic_data)
        db.session.add(topic)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # Clear existing topics
        Topic.query.delete()
        add_enhanced_topics()
        print("Database populated with enhanced content successfully!") 