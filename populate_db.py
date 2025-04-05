from app import app, db, Topic

def add_topics():
    # Unit 1: Chemistry of Life
    topics_unit1 = [
        {
            "title": "The Chemical Context of Life",
            "content": """
            <h3>Elements and Compounds</h3>
            <ul>
                <li>Matter consists of chemical elements in pure form and in combinations called compounds</li>
                <li>Elements cannot be broken down to other substances by chemical reactions</li>
                <li>Compounds contain two or more elements in a fixed ratio</li>
            </ul>
            
            <h3>Atoms and Molecules</h3>
            <ul>
                <li>Atoms are the smallest unit of matter that still retains the properties of an element</li>
                <li>Atoms are composed of subatomic particles: protons, neutrons, and electrons</li>
                <li>Atomic number = number of protons</li>
                <li>Mass number = protons + neutrons</li>
            </ul>
            """,
            "unit": 1
        },
        {
            "title": "Water and Life",
            "content": """
            <h3>Water's Polarity</h3>
            <ul>
                <li>Water is a polar molecule</li>
                <li>Oxygen is more electronegative than hydrogen</li>
                <li>Results in partial positive and negative charges</li>
            </ul>
            
            <h3>Hydrogen Bonding</h3>
            <ul>
                <li>Attraction between partial positive hydrogen and partial negative oxygen</li>
                <li>Gives water its unique properties</li>
                <li>Cohesion and adhesion</li>
                <li>High specific heat</li>
                <li>High heat of vaporization</li>
            </ul>
            """,
            "unit": 1
        }
    ]

    # Unit 2: Cell Structure and Function
    topics_unit2 = [
        {
            "title": "Cell Theory",
            "content": """
            <h3>Basic Principles</h3>
            <ul>
                <li>All living things are composed of cells</li>
                <li>Cells are the basic units of structure and function in living things</li>
                <li>New cells are produced from existing cells</li>
            </ul>
            
            <h3>Cell Types</h3>
            <ul>
                <li>Prokaryotic cells: no nucleus, simpler structure</li>
                <li>Eukaryotic cells: have nucleus, more complex structure</li>
            </ul>
            """,
            "unit": 2
        },
        {
            "title": "Cell Organelles",
            "content": """
            <h3>Major Organelles</h3>
            <ul>
                <li>Nucleus: contains DNA</li>
                <li>Mitochondria: energy production</li>
                <li>Endoplasmic Reticulum: protein and lipid synthesis</li>
                <li>Golgi Apparatus: protein modification and packaging</li>
                <li>Lysosomes: digestion and waste removal</li>
                <li>Chloroplasts: photosynthesis (in plants)</li>
            </ul>
            """,
            "unit": 2
        }
    ]

    # Unit 3: Cellular Energetics
    topics_unit3 = [
        {
            "title": "Enzymes",
            "content": """
            <h3>Enzyme Function</h3>
            <ul>
                <li>Biological catalysts that speed up chemical reactions</li>
                <li>Lower activation energy</li>
                <li>Not consumed in reactions</li>
            </ul>
            
            <h3>Factors Affecting Enzyme Activity</h3>
            <ul>
                <li>Temperature</li>
                <li>pH</li>
                <li>Substrate concentration</li>
                <li>Inhibitors</li>
            </ul>
            """,
            "unit": 3
        },
        {
            "title": "Cellular Respiration",
            "content": """
            <h3>Stages of Cellular Respiration</h3>
            <ul>
                <li>Glycolysis: glucose → pyruvate</li>
                <li>Krebs Cycle: complete oxidation of pyruvate</li>
                <li>Electron Transport Chain: ATP production</li>
            </ul>
            
            <h3>ATP Production</h3>
            <ul>
                <li>Substrate-level phosphorylation</li>
                <li>Oxidative phosphorylation</li>
                <li>Total ATP yield: ~36-38 ATP per glucose</li>
            </ul>
            """,
            "unit": 3
        }
    ]

    # Unit 4: Cell Communication and Cell Cycle
    topics_unit4 = [
        {
            "title": "Cell Signaling",
            "content": """
            <h3>Signal Transduction Pathways</h3>
            <ul>
                <li>Reception: signal molecule binds to receptor</li>
                <li>Transduction: signal converted to cellular response</li>
                <li>Response: specific cellular activity</li>
            </ul>
            
            <h3>Types of Signaling</h3>
            <ul>
                <li>Direct contact</li>
                <li>Paracrine signaling</li>
                <li>Endocrine signaling</li>
                <li>Synaptic signaling</li>
            </ul>
            """,
            "unit": 4
        },
        {
            "title": "Cell Cycle",
            "content": """
            <h3>Phases of the Cell Cycle</h3>
            <ul>
                <li>Interphase: G1, S, G2</li>
                <li>Mitosis: prophase, metaphase, anaphase, telophase</li>
                <li>Cytokinesis: cell division</li>
            </ul>
            
            <h3>Regulation</h3>
            <ul>
                <li>Checkpoints: G1, G2, M</li>
                <li>Cyclins and cyclin-dependent kinases</li>
                <li>Growth factors</li>
            </ul>
            """,
            "unit": 4
        }
    ]

    # Unit 5: Heredity
    topics_unit5 = [
        {
            "title": "Mendelian Genetics",
            "content": """
            <h3>Mendel's Laws</h3>
            <ul>
                <li>Law of Segregation: alleles separate during gamete formation</li>
                <li>Law of Independent Assortment: alleles of different genes assort independently</li>
            </ul>
            
            <h3>Genetic Crosses</h3>
            <ul>
                <li>Punnett squares</li>
                <li>Monohybrid and dihybrid crosses</li>
                <li>Probability calculations</li>
            </ul>
            """,
            "unit": 5
        },
        {
            "title": "Chromosomal Inheritance",
            "content": """
            <h3>Sex Chromosomes</h3>
            <ul>
                <li>X and Y chromosomes</li>
                <li>Sex-linked traits</li>
                <li>X-inactivation</li>
            </ul>
            
            <h3>Chromosomal Abnormalities</h3>
            <ul>
                <li>Nondisjunction</li>
                <li>Down syndrome</li>
                <li>Turner syndrome</li>
                <li>Klinefelter syndrome</li>
            </ul>
            """,
            "unit": 5
        }
    ]

    # Unit 6: Gene Expression and Regulation
    topics_unit6 = [
        {
            "title": "DNA Structure and Replication",
            "content": """
            <h3>DNA Structure</h3>
            <ul>
                <li>Double helix</li>
                <li>Complementary base pairing</li>
                <li>Antiparallel strands</li>
            </ul>
            
            <h3>Replication Process</h3>
            <ul>
                <li>Semi-conservative replication</li>
                <li>Leading and lagging strands</li>
                <li>DNA polymerase</li>
                <li>Okazaki fragments</li>
            </ul>
            """,
            "unit": 6
        },
        {
            "title": "Gene Expression",
            "content": """
            <h3>Transcription</h3>
            <ul>
                <li>RNA polymerase</li>
                <li>Promoter regions</li>
                <li>mRNA processing</li>
            </ul>
            
            <h3>Translation</h3>
            <ul>
                <li>Ribosomes</li>
                <li>tRNA and amino acids</li>
                <li>Genetic code</li>
            </ul>
            """,
            "unit": 6
        }
    ]

    # Unit 7: Natural Selection
    topics_unit7 = [
        {
            "title": "Evolution by Natural Selection",
            "content": """
            <h3>Darwin's Theory</h3>
            <ul>
                <li>Variation exists in populations</li>
                <li>Some variations are heritable</li>
                <li>More offspring are produced than can survive</li>
                <li>Individuals with favorable traits survive and reproduce</li>
            </ul>
            
            <h3>Evidence for Evolution</h3>
            <ul>
                <li>Fossil record</li>
                <li>Comparative anatomy</li>
                <li>Molecular biology</li>
                <li>Biogeography</li>
            </ul>
            """,
            "unit": 7
        },
        {
            "title": "Population Genetics",
            "content": """
            <h3>Hardy-Weinberg Equilibrium</h3>
            <ul>
                <li>p² + 2pq + q² = 1</li>
                <li>p + q = 1</li>
                <li>Conditions for equilibrium</li>
            </ul>
            
            <h3>Mechanisms of Evolution</h3>
            <ul>
                <li>Natural selection</li>
                <li>Genetic drift</li>
                <li>Gene flow</li>
                <li>Mutation</li>
            </ul>
            """,
            "unit": 7
        }
    ]

    # Unit 8: Ecology
    topics_unit8 = [
        {
            "title": "Ecosystem Structure",
            "content": """
            <h3>Levels of Organization</h3>
            <ul>
                <li>Individual</li>
                <li>Population</li>
                <li>Community</li>
                <li>Ecosystem</li>
                <li>Biosphere</li>
            </ul>
            
            <h3>Energy Flow</h3>
            <ul>
                <li>Food chains and webs</li>
                <li>Trophic levels</li>
                <li>Energy pyramids</li>
            </ul>
            """,
            "unit": 8
        },
        {
            "title": "Population Ecology",
            "content": """
            <h3>Population Growth</h3>
            <ul>
                <li>Exponential growth</li>
                <li>Logistic growth</li>
                <li>Carrying capacity</li>
            </ul>
            
            <h3>Population Regulation</h3>
            <ul>
                <li>Density-dependent factors</li>
                <li>Density-independent factors</li>
                <li>Life history strategies</li>
            </ul>
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
        add_topics()
        print("Database populated successfully!") 