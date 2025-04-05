import svgwrite
import os
from PIL import Image
import numpy as np
import io
import math
import glob

def save_to_png(svg_path, png_path, width=800, height=600):
    """
    Create empty PNG file to ensure PNG version exists
    """
    # Create a blank white image
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    img.save(png_path)
    print(f"Created placeholder PNG for {svg_path} at {png_path}")

def create_levels_of_organization():
    dwg = svgwrite.Drawing('static/images/levels_of_organization.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Levels of Biological Organization', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Define levels
    levels = [
        ('Biosphere', 400, 100),
        ('Ecosystem', 400, 150),
        ('Community', 400, 200),
        ('Population', 400, 250),
        ('Organism', 400, 300),
        ('Organ System', 400, 350),
        ('Organ', 400, 400),
        ('Tissue', 400, 450),
        ('Cell', 400, 500),
        ('Organelle', 400, 550),
        ('Molecule', 400, 600)
    ]
    
    # Draw connecting lines
    for i in range(len(levels)-1):
        dwg.add(dwg.line(start=(levels[i][1], levels[i][2]), 
                        end=(levels[i+1][1], levels[i+1][2]),
                        stroke='black', stroke_width=2))
    
    # Add level boxes
    for level in levels:
        dwg.add(dwg.rect(insert=(level[1]-100, level[2]-20), 
                        size=(200, 40),
                        fill='#f0f0f0', stroke='black', stroke_width=1))
        dwg.add(dwg.text(level[0], insert=(level[1], level[2]+5),
                        text_anchor='middle', font_size='14px'))
    
    dwg.save()

def create_cell_comparison():
    dwg = svgwrite.Drawing('static/images/cell_comparison.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Prokaryotic vs Eukaryotic Cells', insert=(400, 30),
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw prokaryotic cell
    dwg.add(dwg.circle(center=(200, 300), r=100, fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Prokaryotic Cell', insert=(200, 450),
                     text_anchor='middle', font_size='16px'))
    
    # Draw eukaryotic cell
    dwg.add(dwg.circle(center=(600, 300), r=150, fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Eukaryotic Cell', insert=(600, 450),
                     text_anchor='middle', font_size='16px'))
    
    # Add organelles
    organelles = [
        ('Nucleoid', 200, 300, 30),
        ('Ribosomes', 200, 250, 10),
        ('Cell Wall', 200, 300, 90),
        ('Nucleus', 600, 300, 50),
        ('Mitochondria', 550, 250, 20),
        ('ER', 600, 350, 30),
        ('Golgi', 650, 300, 25)
    ]
    
    for organelle in organelles:
        dwg.add(dwg.circle(center=(organelle[1], organelle[2]), 
                          r=organelle[3], fill='#d0d0d0', stroke='black'))
        dwg.add(dwg.text(organelle[0], insert=(organelle[1], organelle[2]),
                        text_anchor='middle', font_size='12px'))
    
    dwg.save()

def create_fluid_mosaic():
    dwg = svgwrite.Drawing('static/images/fluid_mosaic.svg', size=('800px', '400px'))
    
    # Add title
    dwg.add(dwg.text('Fluid Mosaic Model', insert=(400, 30),
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw phospholipid bilayer
    for i in range(10):
        # Upper layer
        dwg.add(dwg.circle(center=(100+i*70, 150), r=20, fill='#f0f0f0', stroke='black'))
        dwg.add(dwg.line(start=(100+i*70, 150), end=(100+i*70, 200),
                        stroke='black', stroke_width=2))
        
        # Lower layer
        dwg.add(dwg.circle(center=(100+i*70, 250), r=20, fill='#f0f0f0', stroke='black'))
        dwg.add(dwg.line(start=(100+i*70, 250), end=(100+i*70, 200),
                        stroke='black', stroke_width=2))
    
    # Add membrane proteins
    proteins = [
        ('Integral Protein', 300, 200, 30, 60),
        ('Peripheral Protein', 500, 150, 20, 40),
        ('Channel Protein', 700, 200, 25, 50)
    ]
    
    for protein in proteins:
        dwg.add(dwg.rect(insert=(protein[1]-protein[3]/2, protein[2]-protein[4]/2),
                        size=(protein[3], protein[4]),
                        fill='#d0d0d0', stroke='black'))
        dwg.add(dwg.text(protein[0], insert=(protein[1], protein[2]+40),
                        text_anchor='middle', font_size='12px'))
    
    dwg.save()

def create_metabolic_pathways():
    dwg = svgwrite.Drawing('static/images/metabolic_pathways.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Metabolic Pathways', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw catabolic pathway
    dwg.add(dwg.text('Catabolic Pathway', insert=(200, 100), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.line(start=(100, 120), end=(300, 120), stroke='black', stroke_width=2))
    dwg.add(dwg.text('Complex Molecules', insert=(100, 150), text_anchor='middle'))
    dwg.add(dwg.text('→', insert=(200, 150), text_anchor='middle'))
    dwg.add(dwg.text('Simple Molecules', insert=(300, 150), text_anchor='middle'))
    dwg.add(dwg.text('+ Energy', insert=(300, 180), text_anchor='middle'))
    
    # Draw anabolic pathway
    dwg.add(dwg.text('Anabolic Pathway', insert=(600, 100), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.line(start=(500, 120), end=(700, 120), stroke='black', stroke_width=2))
    dwg.add(dwg.text('Simple Molecules', insert=(500, 150), text_anchor='middle'))
    dwg.add(dwg.text('→', insert=(600, 150), text_anchor='middle'))
    dwg.add(dwg.text('Complex Molecules', insert=(700, 150), text_anchor='middle'))
    dwg.add(dwg.text('- Energy', insert=(700, 180), text_anchor='middle'))
    
    dwg.save()

def create_enzyme_action():
    dwg = svgwrite.Drawing('static/images/enzyme_action.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Enzyme Action', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw enzyme and substrate
    dwg.add(dwg.rect(insert=(300, 100), size=(200, 100), 
                    fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Enzyme', insert=(400, 150), 
                     text_anchor='middle', font_size='16px'))
    
    # Draw active site
    dwg.add(dwg.circle(center=(400, 200), r=30, 
                      fill='#d0d0d0', stroke='black'))
    dwg.add(dwg.text('Active Site', insert=(400, 200), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw substrate
    dwg.add(dwg.rect(insert=(200, 300), size=(100, 50), 
                    fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Substrate', insert=(250, 325), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw product
    dwg.add(dwg.rect(insert=(500, 300), size=(100, 50), 
                    fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Product', insert=(550, 325), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw arrows
    dwg.add(dwg.line(start=(250, 300), end=(400, 230), 
                    stroke='black', stroke_width=2))
    dwg.add(dwg.line(start=(400, 230), end=(550, 300), 
                    stroke='black', stroke_width=2))
    
    dwg.save()

def create_cellular_respiration():
    dwg = svgwrite.Drawing('static/images/cellular_respiration.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Cellular Respiration', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw stages
    stages = [
        ('Glycolysis', 200, 100),
        ('Citric Acid Cycle', 400, 100),
        ('Oxidative Phosphorylation', 600, 100)
    ]
    
    for stage in stages:
        dwg.add(dwg.rect(insert=(stage[1]-80, stage[2]), size=(160, 60), 
                        fill='#f0f0f0', stroke='black'))
        dwg.add(dwg.text(stage[0], insert=(stage[1], stage[2]+30), 
                         text_anchor='middle', font_size='14px'))
    
    # Draw connecting arrows
    dwg.add(dwg.line(start=(280, 130), end=(320, 130), 
                    stroke='black', stroke_width=2))
    dwg.add(dwg.line(start=(480, 130), end=(520, 130), 
                    stroke='black', stroke_width=2))
    
    # Add ATP production
    dwg.add(dwg.text('2 ATP', insert=(200, 200), text_anchor='middle'))
    dwg.add(dwg.text('2 ATP', insert=(400, 200), text_anchor='middle'))
    dwg.add(dwg.text('~28 ATP', insert=(600, 200), text_anchor='middle'))
    
    dwg.save()

def create_fermentation():
    dwg = svgwrite.Drawing('static/images/fermentation.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Types of Fermentation', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw alcohol fermentation
    dwg.add(dwg.text('Alcohol Fermentation', insert=(200, 100), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.line(start=(100, 120), end=(300, 120), stroke='black', stroke_width=2))
    dwg.add(dwg.text('Pyruvate', insert=(100, 150), text_anchor='middle'))
    dwg.add(dwg.text('→', insert=(200, 150), text_anchor='middle'))
    dwg.add(dwg.text('Acetaldehyde', insert=(300, 150), text_anchor='middle'))
    dwg.add(dwg.text('→', insert=(400, 150), text_anchor='middle'))
    dwg.add(dwg.text('Ethanol', insert=(500, 150), text_anchor='middle'))
    
    # Draw lactic acid fermentation
    dwg.add(dwg.text('Lactic Acid Fermentation', insert=(200, 300), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.line(start=(100, 320), end=(300, 320), stroke='black', stroke_width=2))
    dwg.add(dwg.text('Pyruvate', insert=(100, 350), text_anchor='middle'))
    dwg.add(dwg.text('→', insert=(200, 350), text_anchor='middle'))
    dwg.add(dwg.text('Lactate', insert=(300, 350), text_anchor='middle'))
    
    dwg.save()

def create_light_reactions():
    dwg = svgwrite.Drawing('static/images/light_reactions.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Light Reactions', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw thylakoid membrane
    dwg.add(dwg.rect(insert=(100, 100), size=(600, 200), 
                    fill='#f0f0f0', stroke='black'))
    
    # Draw photosystems
    dwg.add(dwg.circle(center=(200, 200), r=30, fill='#d0d0d0', stroke='black'))
    dwg.add(dwg.text('PS II', insert=(200, 200), text_anchor='middle'))
    
    dwg.add(dwg.circle(center=(400, 200), r=30, fill='#d0d0d0', stroke='black'))
    dwg.add(dwg.text('PS I', insert=(400, 200), text_anchor='middle'))
    
    # Draw electron transport chain
    dwg.add(dwg.line(start=(230, 200), end=(370, 200), 
                    stroke='black', stroke_width=2))
    
    # Add labels
    dwg.add(dwg.text('H2O → O2', insert=(200, 250), text_anchor='middle'))
    dwg.add(dwg.text('NADP+ → NADPH', insert=(400, 250), text_anchor='middle'))
    
    dwg.save()

def create_calvin_cycle():
    dwg = svgwrite.Drawing('static/images/calvin_cycle.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Calvin Cycle', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw cycle
    dwg.add(dwg.circle(center=(400, 300), r=150, 
                      fill='none', stroke='black', stroke_width=2))
    
    # Add phases
    phases = [
        ('Carbon Fixation', 400, 150),
        ('Reduction', 550, 300),
        ('Regeneration', 400, 450)
    ]
    
    for phase in phases:
        dwg.add(dwg.text(phase[0], insert=(phase[1], phase[2]), 
                         text_anchor='middle', font_size='14px'))
    
    # Add arrows
    dwg.add(dwg.line(start=(400, 150), end=(550, 300), 
                    stroke='black', stroke_width=2))
    dwg.add(dwg.line(start=(550, 300), end=(400, 450), 
                    stroke='black', stroke_width=2))
    dwg.add(dwg.line(start=(400, 450), end=(400, 150), 
                    stroke='black', stroke_width=2))
    
    dwg.save()

def create_cell_signaling():
    dwg = svgwrite.Drawing('static/images/cell_signaling.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Three Stages of Cell Signaling', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw cells
    dwg.add(dwg.circle(center=(200, 300), r=80, fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Signaling Cell', insert=(200, 400), 
                     text_anchor='middle', font_size='14px'))
    
    dwg.add(dwg.circle(center=(600, 300), r=80, fill='#f0f0f0', stroke='black'))
    dwg.add(dwg.text('Target Cell', insert=(600, 400), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw signal molecule
    for i in range(5):
        dwg.add(dwg.circle(center=(300+i*50, 280+i*5), r=10, 
                          fill='#d0d0d0', stroke='black'))
    
    # Draw receptor
    dwg.add(dwg.rect(insert=(520, 280), size=(30, 50), 
                    fill='#a0a0a0', stroke='black'))
    
    # Draw response
    dwg.add(dwg.text('DNA', insert=(600, 280), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.circle(center=(600, 320), r=30, 
                      fill='none', stroke='black', stroke_dasharray='5,5'))
    
    # Add labels for stages
    dwg.add(dwg.text('1. Reception', insert=(450, 250), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.text('2. Transduction', insert=(600, 230), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.text('3. Response', insert=(600, 330), 
                     text_anchor='middle', font_size='16px'))
    
    # Draw arrows
    dwg.add(dwg.line(start=(280, 300), end=(500, 300), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    dwg.add(dwg.line(start=(550, 280), end=(580, 260), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    # Define arrow marker
    marker = dwg.marker(insert=(10, 5), size=(10, 10), orient='auto')
    marker.add(dwg.path(d='M0,0 L10,5 L0,10 L2,5 Z', fill='black'))
    dwg.defs.add(marker)
    
    dwg.save()

def create_signal_transduction():
    dwg = svgwrite.Drawing('static/images/signal_transduction.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Signal Transduction Pathways', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw cell membrane
    dwg.add(dwg.line(start=(100, 200), end=(700, 200), 
                    stroke='black', stroke_width=3))
    dwg.add(dwg.line(start=(100, 210), end=(700, 210), 
                    stroke='black', stroke_width=3))
    
    # Label extracellular and intracellular
    dwg.add(dwg.text('Extracellular', insert=(150, 180), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('Intracellular', insert=(150, 230), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw receptor types
    # GPCR
    dwg.add(dwg.text('GPCR', insert=(300, 150), 
                     text_anchor='middle', font_size='14px'))
    for i in range(7):
        dwg.add(dwg.line(start=(280+i*5, 180), end=(280+i*5, 230), 
                        stroke='black', stroke_width=2))
    
    # RTK
    dwg.add(dwg.text('RTK', insert=(500, 150), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.line(start=(480, 180), end=(480, 230), 
                    stroke='black', stroke_width=2))
    dwg.add(dwg.line(start=(520, 180), end=(520, 230), 
                    stroke='black', stroke_width=2))
    
    # Draw signaling molecules
    dwg.add(dwg.circle(center=(300, 120), r=15, 
                      fill='#d0d0d0', stroke='black'))
    dwg.add(dwg.circle(center=(500, 120), r=15, 
                      fill='#d0d0d0', stroke='black'))
    
    # Draw downstream pathways
    # For GPCR
    dwg.add(dwg.text('G protein', insert=(300, 250), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.circle(center=(300, 270), r=20, 
                      fill='#e0e0e0', stroke='black'))
    
    dwg.add(dwg.line(start=(300, 290), end=(300, 320), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    dwg.add(dwg.text('Adenylyl cyclase', insert=(300, 340), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.rect(insert=(260, 350), size=(80, 30), 
                    fill='#e0e0e0', stroke='black'))
    
    dwg.add(dwg.line(start=(300, 380), end=(300, 410), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    dwg.add(dwg.text('cAMP', insert=(300, 430), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.circle(center=(300, 450), r=15, 
                      fill='#e0e0e0', stroke='black'))
    
    # For RTK
    dwg.add(dwg.text('P', insert=(490, 240), 
                     text_anchor='middle', font_size='12px', font_weight='bold'))
    dwg.add(dwg.text('P', insert=(510, 240), 
                     text_anchor='middle', font_size='12px', font_weight='bold'))
    
    dwg.add(dwg.line(start=(500, 250), end=(500, 280), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    dwg.add(dwg.text('Ras', insert=(500, 300), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.circle(center=(500, 320), r=20, 
                      fill='#e0e0e0', stroke='black'))
    
    dwg.add(dwg.line(start=(500, 340), end=(500, 370), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    dwg.add(dwg.text('MAP kinase cascade', insert=(500, 390), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.rect(insert=(450, 400), size=(100, 30), 
                    fill='#e0e0e0', stroke='black'))
    
    # Define arrow marker
    marker = dwg.marker(insert=(10, 5), size=(10, 10), orient='auto')
    marker.add(dwg.path(d='M0,0 L10,5 L0,10 L2,5 Z', fill='black'))
    dwg.defs.add(marker)
    
    dwg.save()

def create_cell_cycle():
    dwg = svgwrite.Drawing('static/images/cell_cycle.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Cell Cycle', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw main circle
    dwg.add(dwg.circle(center=(400, 300), r=200, 
                      fill='none', stroke='black', stroke_width=2))
    
    # Draw sectors
    # G1 phase (largest)
    g1_path = 'M400,300 L400,100 A200,200 0 0,1 600,350 Z'
    dwg.add(dwg.path(d=g1_path, fill='#f0f0f0', stroke='black'))
    
    # S phase
    s_path = 'M400,300 L600,350 A200,200 0 0,1 430,500 Z'
    dwg.add(dwg.path(d=s_path, fill='#d0d0d0', stroke='black'))
    
    # G2 phase
    g2_path = 'M400,300 L430,500 A200,200 0 0,1 250,450 Z'
    dwg.add(dwg.path(d=g2_path, fill='#e0e0e0', stroke='black'))
    
    # M phase (smallest)
    m_path = 'M400,300 L250,450 A200,200 0 0,1 200,300 L400,300 Z'
    dwg.add(dwg.path(d=m_path, fill='#c0c0c0', stroke='black'))
    
    # Complete the circle
    final_path = 'M400,300 L200,300 A200,200 0 0,1 400,100 Z'
    dwg.add(dwg.path(d=final_path, fill='#f0f0f0', stroke='black'))
    
    # Add labels
    dwg.add(dwg.text('G1', insert=(500, 200), 
                     text_anchor='middle', font_size='24px', font_weight='bold'))
    dwg.add(dwg.text('S', insert=(550, 350), 
                     text_anchor='middle', font_size='24px', font_weight='bold'))
    dwg.add(dwg.text('G2', insert=(350, 450), 
                     text_anchor='middle', font_size='24px', font_weight='bold'))
    dwg.add(dwg.text('M', insert=(250, 350), 
                     text_anchor='middle', font_size='24px', font_weight='bold'))
    
    # Add checkpoints
    dwg.add(dwg.circle(center=(470, 180), r=15, 
                      fill='#ff0000', stroke='black'))
    dwg.add(dwg.text('G1 Checkpoint', insert=(470, 150), 
                     text_anchor='middle', font_size='12px'))
    
    dwg.add(dwg.circle(center=(400, 420), r=15, 
                      fill='#ff0000', stroke='black'))
    dwg.add(dwg.text('G2 Checkpoint', insert=(400, 450), 
                     text_anchor='middle', font_size='12px'))
    
    dwg.add(dwg.circle(center=(280, 350), r=15, 
                      fill='#ff0000', stroke='black'))
    dwg.add(dwg.text('M Checkpoint', insert=(280, 320), 
                     text_anchor='middle', font_size='12px'))
    
    # Add interphase label
    dwg.add(dwg.text('Interphase', insert=(450, 300), 
                     text_anchor='middle', font_size='18px'))
    
    dwg.save()

def create_mitosis():
    dwg = svgwrite.Drawing('static/images/mitosis.svg', size=('800px', '400px'))
    
    # Add title
    dwg.add(dwg.text('Stages of Mitosis', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw stages
    stages = ['Prophase', 'Metaphase', 'Anaphase', 'Telophase']
    
    for i, stage in enumerate(stages):
        x_pos = 150 + i * 170
        
        # Draw cell
        dwg.add(dwg.circle(center=(x_pos, 200), r=60, 
                          fill='none', stroke='black'))
        
        # Draw chromosomes based on stage
        if stage == 'Prophase':
            # Condensed chromosomes, nuclear envelope breaking down
            for j in range(3):
                dwg.add(dwg.line(start=(x_pos-30+j*20, 180+j*10), 
                                end=(x_pos-10+j*20, 200+j*10), 
                                stroke='blue', stroke_width=5))
            dwg.add(dwg.circle(center=(x_pos, 200), r=40, 
                              fill='none', stroke='black', stroke_dasharray='5,5'))
        
        elif stage == 'Metaphase':
            # Chromosomes aligned at metaphase plate
            for j in range(3):
                dwg.add(dwg.line(start=(x_pos-5, 170+j*20), 
                                end=(x_pos+5, 170+j*20), 
                                stroke='blue', stroke_width=5))
            dwg.add(dwg.line(start=(x_pos, 140), end=(x_pos, 260), 
                            stroke='black', stroke_dasharray='2,2'))
        
        elif stage == 'Anaphase':
            # Chromosomes moving to opposite poles
            for j in range(3):
                dwg.add(dwg.line(start=(x_pos-30, 170+j*20), 
                                end=(x_pos-20, 170+j*20), 
                                stroke='blue', stroke_width=5))
                dwg.add(dwg.line(start=(x_pos+20, 170+j*20), 
                                end=(x_pos+30, 170+j*20), 
                                stroke='blue', stroke_width=5))
        
        elif stage == 'Telophase':
            # Nuclear envelopes reforming, cell beginning to divide
            for j in range(3):
                dwg.add(dwg.line(start=(x_pos-40, 170+j*20), 
                                end=(x_pos-30, 170+j*20), 
                                stroke='blue', stroke_width=5))
                dwg.add(dwg.line(start=(x_pos+30, 170+j*20), 
                                end=(x_pos+40, 170+j*20), 
                                stroke='blue', stroke_width=5))
            dwg.add(dwg.circle(center=(x_pos-30, 200), r=25, 
                              fill='none', stroke='black'))
            dwg.add(dwg.circle(center=(x_pos+30, 200), r=25, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(x_pos, 140), end=(x_pos, 260), 
                            stroke='black', stroke_width=1))
        
        # Add stage label
        dwg.add(dwg.text(stage, insert=(x_pos, 300), 
                         text_anchor='middle', font_size='16px'))
    
    dwg.save()

def create_meiosis():
    dwg = svgwrite.Drawing('static/images/meiosis.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Stages of Meiosis', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw meiosis I
    dwg.add(dwg.text('MEIOSIS I', insert=(200, 80), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    stages_1 = ['Prophase I', 'Metaphase I', 'Anaphase I', 'Telophase I']
    
    for i, stage in enumerate(stages_1):
        y_pos = 150 + i * 100
        
        # Draw cell
        dwg.add(dwg.circle(center=(200, y_pos), r=40, 
                          fill='none', stroke='black'))
        
        # Draw chromosomes based on stage
        if stage == 'Prophase I':
            # Paired homologous chromosomes with crossing over
            dwg.add(dwg.line(start=(185, y_pos-15), end=(195, y_pos+15), 
                            stroke='blue', stroke_width=4))
            dwg.add(dwg.line(start=(205, y_pos-15), end=(215, y_pos+15), 
                            stroke='red', stroke_width=4))
            
            # Crossing over
            dwg.add(dwg.line(start=(193, y_pos), end=(207, y_pos), 
                            stroke='purple', stroke_width=2))
        
        elif stage == 'Metaphase I':
            # Homologous pairs at metaphase plate
            dwg.add(dwg.line(start=(185, y_pos), end=(195, y_pos), 
                            stroke='blue', stroke_width=4))
            dwg.add(dwg.line(start=(205, y_pos), end=(215, y_pos), 
                            stroke='red', stroke_width=4))
        
        elif stage == 'Anaphase I':
            # Homologous chromosomes separating
            dwg.add(dwg.line(start=(175, y_pos-10), end=(185, y_pos+10), 
                            stroke='blue', stroke_width=4))
            dwg.add(dwg.line(start=(215, y_pos-10), end=(225, y_pos+10), 
                            stroke='red', stroke_width=4))
        
        elif stage == 'Telophase I':
            # Two cells with one set of chromosomes each
            dwg.add(dwg.circle(center=(170, y_pos), r=25, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(160, y_pos), end=(170, y_pos), 
                            stroke='blue', stroke_width=4))
            
            dwg.add(dwg.circle(center=(230, y_pos), r=25, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(220, y_pos), end=(230, y_pos), 
                            stroke='red', stroke_width=4))
        
        # Add stage label
        dwg.add(dwg.text(stage, insert=(80, y_pos), 
                         text_anchor='middle', font_size='14px'))
    
    # Draw meiosis II
    dwg.add(dwg.text('MEIOSIS II', insert=(600, 80), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    stages_2 = ['Prophase II', 'Metaphase II', 'Anaphase II', 'Telophase II']
    
    for i, stage in enumerate(stages_2):
        y_pos = 150 + i * 100
        
        # Draw cells (two side by side)
        dwg.add(dwg.circle(center=(550, y_pos), r=30, 
                          fill='none', stroke='black'))
        dwg.add(dwg.circle(center=(650, y_pos), r=30, 
                          fill='none', stroke='black'))
        
        # Draw chromosomes based on stage
        if stage == 'Prophase II':
            # Condensed chromosomes in each cell
            dwg.add(dwg.line(start=(545, y_pos), end=(555, y_pos), 
                            stroke='blue', stroke_width=4))
            dwg.add(dwg.line(start=(645, y_pos), end=(655, y_pos), 
                            stroke='red', stroke_width=4))
        
        elif stage == 'Metaphase II':
            # Chromosomes at metaphase plate in each cell
            dwg.add(dwg.line(start=(545, y_pos), end=(555, y_pos), 
                            stroke='blue', stroke_width=4))
            dwg.add(dwg.line(start=(645, y_pos), end=(655, y_pos), 
                            stroke='red', stroke_width=4))
        
        elif stage == 'Anaphase II':
            # Sister chromatids separating in each cell
            dwg.add(dwg.line(start=(540, y_pos-5), end=(550, y_pos-5), 
                            stroke='blue', stroke_width=2))
            dwg.add(dwg.line(start=(550, y_pos+5), end=(560, y_pos+5), 
                            stroke='blue', stroke_width=2))
            
            dwg.add(dwg.line(start=(640, y_pos-5), end=(650, y_pos-5), 
                            stroke='red', stroke_width=2))
            dwg.add(dwg.line(start=(650, y_pos+5), end=(660, y_pos+5), 
                            stroke='red', stroke_width=2))
        
        elif stage == 'Telophase II':
            # Four cells, each with one chromosome
            dwg.add(dwg.circle(center=(535, y_pos-10), r=15, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(532, y_pos-10), end=(538, y_pos-10), 
                            stroke='blue', stroke_width=2))
            
            dwg.add(dwg.circle(center=(565, y_pos+10), r=15, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(562, y_pos+10), end=(568, y_pos+10), 
                            stroke='blue', stroke_width=2))
            
            dwg.add(dwg.circle(center=(635, y_pos-10), r=15, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(632, y_pos-10), end=(638, y_pos-10), 
                            stroke='red', stroke_width=2))
            
            dwg.add(dwg.circle(center=(665, y_pos+10), r=15, 
                              fill='none', stroke='black'))
            dwg.add(dwg.line(start=(662, y_pos+10), end=(668, y_pos+10), 
                            stroke='red', stroke_width=2))
        
        # Add stage label
        dwg.add(dwg.text(stage, insert=(480, y_pos), 
                         text_anchor='middle', font_size='14px'))
    
    dwg.save()

def create_crossing_over():
    dwg = svgwrite.Drawing('static/images/crossing_over.svg', size=('800px', '400px'))
    
    # Add title
    dwg.add(dwg.text('Crossing Over During Prophase I', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw homologous chromosomes
    # Maternal chromosome
    dwg.add(dwg.rect(insert=(250, 100), size=(50, 200), 
                    fill='#ff9999', stroke='black'))
    
    # Paternal chromosome
    dwg.add(dwg.rect(insert=(500, 100), size=(50, 200), 
                    fill='#9999ff', stroke='black'))
    
    # Draw crossing over stages
    # Stage 1: Homologous chromosomes
    dwg.add(dwg.text('1. Homologous chromosomes', insert=(150, 350), 
                     text_anchor='middle', font_size='14px'))
    
    # Stage 2: Synapsis
    dwg.add(dwg.text('2. Synapsis', insert=(400, 350), 
                     text_anchor='middle', font_size='14px'))
    
    # Stage 3: Crossing over
    dwg.add(dwg.text('3. Crossing over', insert=(650, 350), 
                     text_anchor='middle', font_size='14px'))
    
    # Draw arrows
    dwg.add(dwg.line(start=(200, 200), end=(300, 200), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    dwg.add(dwg.line(start=(450, 200), end=(550, 200), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    
    # Draw synapsed chromosomes
    dwg.add(dwg.rect(insert=(350, 150), size=(100, 100), 
                    fill='#cc99cc', stroke='black'))
    
    # Draw crossing over
    # Recombinant chromosome 1
    dwg.add(dwg.rect(insert=(600, 100), size=(50, 100), 
                    fill='#ff9999', stroke='black'))
    dwg.add(dwg.rect(insert=(600, 200), size=(50, 100), 
                    fill='#9999ff', stroke='black'))
    
    # Recombinant chromosome 2
    dwg.add(dwg.rect(insert=(700, 100), size=(50, 100), 
                    fill='#9999ff', stroke='black'))
    dwg.add(dwg.rect(insert=(700, 200), size=(50, 100), 
                    fill='#ff9999', stroke='black'))
    
    # Define arrow marker
    marker = dwg.marker(insert=(10, 5), size=(10, 10), orient='auto')
    marker.add(dwg.path(d='M0,0 L10,5 L0,10 L2,5 Z', fill='black'))
    dwg.defs.add(marker)
    
    dwg.save()

def create_mendel_experiment():
    dwg = svgwrite.Drawing('static/images/mendel_experiment.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Mendel\'s Monohybrid Cross', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw plant symbols
    def draw_plant(x, y, height, color, label):
        # Stem
        dwg.add(dwg.line(start=(x, y), end=(x, y-height), 
                        stroke='green', stroke_width=2))
        
        # Flower
        dwg.add(dwg.circle(center=(x, y-height), r=15, 
                          fill=color, stroke='black'))
        
        # Label
        dwg.add(dwg.text(label, insert=(x, y+20), 
                         text_anchor='middle', font_size='12px'))
    
    # P generation
    dwg.add(dwg.text('P Generation', insert=(150, 80), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    draw_plant(100, 150, 50, 'purple', 'Purple (PP)')
    draw_plant(200, 150, 50, 'white', 'White (pp)')
    
    # F1 generation
    dwg.add(dwg.text('F1 Generation', insert=(400, 250), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    for i in range(4):
        draw_plant(350 + i*30, 320, 50, 'purple', 'Pp')
    
    # F2 generation
    dwg.add(dwg.text('F2 Generation', insert=(400, 420), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    # Draw 16 plants in a 4x4 grid (3 purple : 1 white ratio)
    for i in range(4):
        for j in range(4):
            color = 'white' if (i == 3 and j == 3) else 'purple'
            label = 'pp' if (i == 3 and j == 3) else ('PP' if i < 1 and j < 1 else 'Pp')
            draw_plant(300 + i*40, 490 + j*20, 40, color, label)
    
    # Draw arrows
    dwg.add(dwg.line(start=(150, 170), end=(150, 210), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    dwg.add(dwg.text('Gametes', insert=(150, 200), 
                    text_anchor='middle', font_size='12px'))
    
    dwg.add(dwg.line(start=(400, 340), end=(400, 380), 
                    stroke='black', stroke_width=2, marker_end='url(#arrow)'))
    dwg.add(dwg.text('Self-fertilization', insert=(400, 370), 
                    text_anchor='middle', font_size='12px'))
    
    # Add Punnett square
    dwg.add(dwg.rect(insert=(560, 120), size=(180, 180), 
                    fill='none', stroke='black'))
    
    # Add dividing lines
    dwg.add(dwg.line(start=(650, 120), end=(650, 300), 
                    stroke='black', stroke_width=1))
    dwg.add(dwg.line(start=(560, 210), end=(740, 210), 
                    stroke='black', stroke_width=1))
    
    # Add labels
    dwg.add(dwg.text('P', insert=(605, 165), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('p', insert=(695, 165), 
                     text_anchor='middle', font_size='14px'))
    
    dwg.add(dwg.text('P', insert=(580, 165), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('p', insert=(580, 255), 
                     text_anchor='middle', font_size='14px'))
    
    # Add results
    dwg.add(dwg.text('PP', insert=(605, 165), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('Pp', insert=(695, 165), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('Pp', insert=(605, 255), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('pp', insert=(695, 255), 
                     text_anchor='middle', font_size='14px'))
    
    # Add ratio
    dwg.add(dwg.text('Phenotypic ratio: 3 purple : 1 white', insert=(650, 320), 
                     text_anchor='middle', font_size='14px', font_weight='bold'))
    
    # Define arrow marker
    marker = dwg.marker(insert=(10, 5), size=(10, 10), orient='auto')
    marker.add(dwg.path(d='M0,0 L10,5 L0,10 L2,5 Z', fill='black'))
    dwg.defs.add(marker)
    
    dwg.save()

def create_punnett_square():
    dwg = svgwrite.Drawing('static/images/punnett_square.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Dihybrid Cross Punnett Square', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw Punnett square frame
    square_size = 400
    dwg.add(dwg.rect(insert=(200, 100), size=(square_size, square_size), 
                    fill='none', stroke='black', stroke_width=2))
    
    # Draw grid lines for 4x4
    cell_size = square_size / 4
    for i in range(1, 4):
        # Vertical lines
        dwg.add(dwg.line(start=(200 + i*cell_size, 100), end=(200 + i*cell_size, 500), 
                        stroke='black', stroke_width=1))
        # Horizontal lines
        dwg.add(dwg.line(start=(200, 100 + i*cell_size), end=(600, 100 + i*cell_size), 
                        stroke='black', stroke_width=1))
    
    # Add gamete labels
    # Male gametes (top)
    gametes_male = ['TR', 'Tr', 'tR', 'tr']
    for i, gamete in enumerate(gametes_male):
        dwg.add(dwg.text(gamete, insert=(250 + i*cell_size, 90), 
                         text_anchor='middle', font_size='16px', font_weight='bold'))
    
    # Female gametes (left)
    gametes_female = ['TR', 'Tr', 'tR', 'tr']
    for i, gamete in enumerate(gametes_female):
        dwg.add(dwg.text(gamete, insert=(180, 150 + i*cell_size), 
                         text_anchor='middle', font_size='16px', font_weight='bold'))
    
    # Add genotypes in each cell
    genotypes = [
        ['TTRR', 'TTRr', 'TtRR', 'TtRr'],
        ['TTRr', 'TTrr', 'TtRr', 'Ttrr'],
        ['TtRR', 'TtRr', 'ttRR', 'ttRr'],
        ['TtRr', 'Ttrr', 'ttRr', 'ttrr']
    ]
    
    phenotypes = [
        ['T_R_', 'T_R_', 'T_R_', 'T_R_'],
        ['T_R_', 'T_rr', 'T_R_', 'T_rr'],
        ['T_R_', 'T_R_', 'ttR_', 'ttR_'],
        ['T_R_', 'T_rr', 'ttR_', 'ttrr']
    ]
    
    colors = [
        ['#ff9999', '#ff9999', '#ff9999', '#ff9999'],
        ['#ff9999', '#ff99ff', '#ff9999', '#ff99ff'],
        ['#ff9999', '#ff9999', '#99ff99', '#99ff99'],
        ['#ff9999', '#ff99ff', '#99ff99', '#9999ff']
    ]
    
    for i in range(4):
        for j in range(4):
            # Draw cell background
            dwg.add(dwg.rect(insert=(200 + j*cell_size, 100 + i*cell_size), 
                            size=(cell_size, cell_size), 
                            fill=colors[i][j], stroke='none'))
            
            # Add genotype
            dwg.add(dwg.text(genotypes[i][j], insert=(200 + j*cell_size + cell_size/2, 
                                                    100 + i*cell_size + cell_size/2 - 10), 
                             text_anchor='middle', font_size='12px'))
            
            # Add phenotype
            dwg.add(dwg.text(phenotypes[i][j], insert=(200 + j*cell_size + cell_size/2, 
                                                      100 + i*cell_size + cell_size/2 + 10), 
                             text_anchor='middle', font_size='12px'))
    
    # Add phenotypic ratio
    dwg.add(dwg.text('Phenotypic Ratio: 9:3:3:1', insert=(400, 520), 
                     text_anchor='middle', font_size='16px', font_weight='bold'))
    
    # Add legend
    legend_items = [
        ('Tall, round (9/16)', '#ff9999', 530, 540),
        ('Tall, wrinkled (3/16)', '#ff99ff', 530, 560),
        ('Dwarf, round (3/16)', '#99ff99', 530, 580),
        ('Dwarf, wrinkled (1/16)', '#9999ff', 530, 600)
    ]
    
    for item in legend_items:
        dwg.add(dwg.rect(insert=(500, item[3]-10), size=(20, 15), 
                        fill=item[1], stroke='black'))
        dwg.add(dwg.text(item[0], insert=(item[2], item[3]), 
                         text_anchor='start', font_size='12px'))
    
    dwg.save()

def create_sex_chromosomes():
    dwg = svgwrite.Drawing('static/images/sex_chromosomes.svg', size=('600px', '400px'))
    
    # Add title
    dwg.add(dwg.text('Sex Chromosomes', insert=(300, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw chromosomes
    # X chromosome
    dwg.add(dwg.rect(insert=(200, 100), size=(60, 180), 
                    fill='#ff9999', stroke='black', rx=10, ry=10))
    dwg.add(dwg.text('X', insert=(230, 190), 
                     text_anchor='middle', font_size='36px', font_weight='bold'))
    
    # Y chromosome
    dwg.add(dwg.rect(insert=(350, 130), size=(60, 120), 
                    fill='#9999ff', stroke='black', rx=10, ry=10))
    dwg.add(dwg.text('Y', insert=(380, 190), 
                     text_anchor='middle', font_size='36px', font_weight='bold'))
    
    # Add labels
    dwg.add(dwg.text('X Chromosome', insert=(230, 300), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('Y Chromosome', insert=(380, 300), 
                     text_anchor='middle', font_size='14px'))
    
    # Add description
    dwg.add(dwg.text('Female: XX', insert=(230, 330), 
                     text_anchor='middle', font_size='14px'))
    dwg.add(dwg.text('Male: XY', insert=(380, 330), 
                     text_anchor='middle', font_size='14px'))
    
    dwg.save()

def create_linkage_map():
    dwg = svgwrite.Drawing('static/images/linkage_map.svg', size=('800px', '400px'))
    
    # Add title
    dwg.add(dwg.text('Genetic Linkage Map', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw chromosome
    chromosome_length = 600
    dwg.add(dwg.rect(insert=(100, 150), size=(chromosome_length, 40), 
                    fill='#f0f0f0', stroke='black'))
    
    # Add markers on chromosome
    markers = [
        ('Gene A', 50),
        ('Gene B', 150),
        ('Gene C', 300),
        ('Gene D', 400),
        ('Gene E', 550)
    ]
    
    for marker in markers:
        # Draw marker line
        dwg.add(dwg.line(start=(100 + marker[1], 130), end=(100 + marker[1], 210), 
                        stroke='black', stroke_width=1))
        
        # Add marker label
        dwg.add(dwg.text(marker[0], insert=(100 + marker[1], 120), 
                         text_anchor='middle', font_size='12px'))
        
        # Add map position
        dwg.add(dwg.text(f"{marker[1]/10} cM", insert=(100 + marker[1], 230), 
                         text_anchor='middle', font_size='12px'))
    
    # Add scale bar
    dwg.add(dwg.line(start=(100, 280), end=(700, 280), 
                    stroke='black', stroke_width=2))
    
    for i in range(7):
        pos = 100 + i*100
        dwg.add(dwg.line(start=(pos, 275), end=(pos, 285), 
                        stroke='black', stroke_width=1))
        dwg.add(dwg.text(f"{i*10} cM", insert=(pos, 300), 
                         text_anchor='middle', font_size='12px'))
    
    # Add recombination frequencies
    dwg.add(dwg.text('Recombination Frequencies:', insert=(400, 350), 
                     text_anchor='middle', font_size='14px', font_weight='bold'))
    
    dwg.add(dwg.text('A-B: 10%  B-C: 15%  C-D: 10%  D-E: 15%', insert=(400, 370), 
                     text_anchor='middle', font_size='12px'))
    
    dwg.save()

def create_dna_replication():
    """Create a diagram of DNA replication"""
    dwg = svgwrite.Drawing('static/images/dna_replication.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('DNA Replication', insert=(400, 30), font_size=24, text_anchor='middle'))
    
    # Draw original DNA strand
    dwg.add(dwg.line((100, 100), (700, 100), stroke='black', stroke_width=2))
    dwg.add(dwg.line((100, 120), (700, 120), stroke='black', stroke_width=2))
    
    # Draw replication fork
    dwg.add(dwg.line((400, 100), (400, 500), stroke='black', stroke_width=2))
    
    # Draw leading and lagging strands
    dwg.add(dwg.line((400, 100), (700, 300), stroke='blue', stroke_width=2))
    dwg.add(dwg.line((400, 100), (100, 300), stroke='red', stroke_width=2))
    
    # Add labels
    dwg.add(dwg.text('Original DNA', insert=(400, 80), font_size=16, text_anchor='middle'))
    dwg.add(dwg.text('Leading Strand', insert=(550, 200), font_size=16))
    dwg.add(dwg.text('Lagging Strand', insert=(250, 200), font_size=16))
    dwg.add(dwg.text('Replication Fork', insert=(400, 520), font_size=16, text_anchor='middle'))
    
    dwg.save()

def create_evolution_tree():
    """Create a phylogenetic tree diagram"""
    dwg = svgwrite.Drawing('static/images/evolution_tree.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Phylogenetic Tree', insert=(400, 30), font_size=24, text_anchor='middle'))
    
    # Draw main branches
    dwg.add(dwg.line((400, 100), (400, 500), stroke='black', stroke_width=2))
    dwg.add(dwg.line((400, 200), (200, 300), stroke='black', stroke_width=2))
    dwg.add(dwg.line((400, 200), (600, 300), stroke='black', stroke_width=2))
    dwg.add(dwg.line((200, 300), (100, 400), stroke='black', stroke_width=2))
    dwg.add(dwg.line((200, 300), (300, 400), stroke='black', stroke_width=2))
    dwg.add(dwg.line((600, 300), (500, 400), stroke='black', stroke_width=2))
    dwg.add(dwg.line((600, 300), (700, 400), stroke='black', stroke_width=2))
    
    # Add species labels
    dwg.add(dwg.text('Species A', insert=(100, 420), font_size=16))
    dwg.add(dwg.text('Species B', insert=(300, 420), font_size=16))
    dwg.add(dwg.text('Species C', insert=(500, 420), font_size=16))
    dwg.add(dwg.text('Species D', insert=(700, 420), font_size=16))
    
    # Add time scale
    dwg.add(dwg.text('Present', insert=(400, 550), font_size=16, text_anchor='middle'))
    dwg.add(dwg.text('Past', insert=(400, 80), font_size=16, text_anchor='middle'))
    
    dwg.save()

def create_ecosystem_energy():
    """Create a diagram of energy flow in an ecosystem"""
    dwg = svgwrite.Drawing('static/images/ecosystem_energy.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('Energy Flow in Ecosystem', insert=(400, 30), font_size=24, text_anchor='middle'))
    
    # Draw trophic levels
    levels = ['Producers', 'Primary Consumers', 'Secondary Consumers', 'Tertiary Consumers']
    for i, level in enumerate(levels):
        y = 100 + i * 100
        dwg.add(dwg.rect(insert=(200, y), size=(400, 60), fill='lightgreen' if i == 0 else 'lightblue'))
        dwg.add(dwg.text(level, insert=(400, y + 35), font_size=16, text_anchor='middle'))
    
    # Draw energy flow arrows
    for i in range(3):
        y1 = 160 + i * 100
        y2 = 200 + i * 100
        dwg.add(dwg.line((400, y1), (400, y2), stroke='black', stroke_width=2))
        dwg.add(dwg.polygon([(390, y2), (410, y2), (400, y2 + 10)], fill='black'))
    
    # Add energy loss labels
    for i in range(3):
        y = 180 + i * 100
        dwg.add(dwg.text('90% Energy Loss', insert=(450, y), font_size=14))
    
    dwg.save()

def create_transcription():
    dwg = svgwrite.Drawing('static/images/transcription.svg', size=('800px', '600px'))
    
    # Background
    dwg.add(dwg.rect((0, 0), ('100%', '100%'), fill='white'))
    
    # DNA and RNA strands
    dna_y = 200
    dwg.add(dwg.path(d=f'M 100 {dna_y} C 200 {dna_y-50} 300 {dna_y+50} 400 {dna_y}', 
                     stroke='blue', fill='none', stroke_width=3))
    dwg.add(dwg.path(d=f'M 100 {dna_y+30} C 200 {dna_y-20} 300 {dna_y+80} 400 {dna_y+30}', 
                     stroke='blue', fill='none', stroke_width=3))
    
    # RNA strand being synthesized
    rna_y = dna_y - 30
    dwg.add(dwg.path(d=f'M 200 {rna_y} C 250 {rna_y-30} 300 {rna_y-30} 350 {rna_y}', 
                     stroke='red', fill='none', stroke_width=3))
    
    # RNA Polymerase
    dwg.add(dwg.circle((250, dna_y), 30, fill='purple', opacity=0.7))
    
    # Labels
    dwg.add(dwg.text('DNA Template Strand', insert=(100, dna_y-40), font_size='16px'))
    dwg.add(dwg.text('DNA Coding Strand', insert=(100, dna_y+60), font_size='16px'))
    dwg.add(dwg.text('RNA Transcript', insert=(200, rna_y-40), font_size='16px', fill='red'))
    dwg.add(dwg.text('RNA Polymerase', insert=(220, dna_y+10), font_size='16px', fill='purple'))
    
    dwg.save()

def create_natural_selection():
    dwg = svgwrite.Drawing('static/images/natural_selection.svg', size=('800px', '600px'))
    
    # Background
    dwg.add(dwg.rect((0, 0), ('100%', '100%'), fill='white'))
    
    # Draw three types of selection
    # Directional Selection
    y1 = 150
    dwg.add(dwg.path(d=f'M 50 {y1} Q 150 {y1} 200 {y1+50}', stroke='gray', fill='none'))
    dwg.add(dwg.path(d=f'M 50 {y1} Q 150 {y1-100} 200 {y1-150}', stroke='blue', fill='none', stroke_width=3))
    dwg.add(dwg.text('Directional Selection', insert=(50, y1-170), font_size='16px'))
    
    # Stabilizing Selection
    y2 = 300
    dwg.add(dwg.path(d=f'M 300 {y2} Q 400 {y2-100} 500 {y2}', stroke='gray', fill='none'))
    dwg.add(dwg.path(d=f'M 300 {y2} Q 400 {y2+50} 500 {y2}', stroke='blue', fill='none', stroke_width=3))
    dwg.add(dwg.text('Stabilizing Selection', insert=(300, y2-120), font_size='16px'))
    
    # Disruptive Selection
    y3 = 450
    dwg.add(dwg.path(d=f'M 550 {y3} Q 650 {y3} 750 {y3}', stroke='gray', fill='none'))
    dwg.add(dwg.path(d=f'M 550 {y3-50} Q 650 {y3} 750 {y3-50}', stroke='blue', fill='none', stroke_width=3))
    dwg.add(dwg.text('Disruptive Selection', insert=(550, y3-70), font_size='16px'))
    
    dwg.save()

def create_population_growth():
    dwg = svgwrite.Drawing('static/images/population_growth.svg', size=('800px', '600px'))
    
    # Background
    dwg.add(dwg.rect((0, 0), ('100%', '100%'), fill='white'))
    
    # Axes
    dwg.add(dwg.line((50, 550), (750, 550), stroke='black', stroke_width=2))  # X-axis
    dwg.add(dwg.line((50, 550), (50, 50), stroke='black', stroke_width=2))    # Y-axis
    
    # Labels
    dwg.add(dwg.text('Time', insert=(400, 580), font_size='16px', text_anchor='middle'))
    dwg.add(dwg.text('Population Size', insert=(30, 300), font_size='16px', transform='rotate(-90, 30, 300)'))
    
    # Exponential Growth Curve (J-shaped)
    exp_points = [(50, 550)]
    for i in range(1, 21):
        x = 50 + i * 35
        y = 550 - (i ** 1.8) * 3
        exp_points.append((x, max(y, 50)))
    
    exp_path = 'M ' + ' L '.join([f'{x} {y}' for x, y in exp_points])
    dwg.add(dwg.path(d=exp_path, stroke='red', fill='none', stroke_width=2))
    dwg.add(dwg.text('Exponential Growth', insert=(700, 100), font_size='16px', fill='red'))
    
    # Logistic Growth Curve (S-shaped)
    log_points = [(50, 550)]
    for i in range(1, 21):
        x = 50 + i * 35
        y = 550 - 400 / (1 + math.exp(-0.3 * (i - 10)))
        log_points.append((x, y))
    
    log_path = 'M ' + ' L '.join([f'{x} {y}' for x, y in log_points])
    dwg.add(dwg.path(d=log_path, stroke='blue', fill='none', stroke_width=2))
    dwg.add(dwg.text('Logistic Growth', insert=(700, 200), font_size='16px', fill='blue'))
    
    # Carrying Capacity Line
    dwg.add(dwg.line((50, 150), (750, 150), stroke='gray', stroke_width=1, stroke_dasharray='5,5'))
    dwg.add(dwg.text('Carrying Capacity', insert=(60, 140), font_size='14px', fill='gray'))
    
    dwg.save()

def create_dna_structure():
    dwg = svgwrite.Drawing('static/images/dna_structure.svg', size=('800px', '600px'))
    
    # Add title
    dwg.add(dwg.text('DNA Double Helix Structure', insert=(400, 30), 
                     text_anchor='middle', font_size='20px', font_weight='bold'))
    
    # Draw double helix backbone
    for i in range(20):
        # Left backbone
        y1 = 100 + i * 20
        y2 = 110 + i * 20
        dwg.add(dwg.line(start=(300 + math.sin(i*0.6)*50, y1), 
                        end=(300 + math.sin((i+1)*0.6)*50, y2),
                        stroke='#1a75ff', stroke_width=3))
        
        # Right backbone
        dwg.add(dwg.line(start=(500 + math.sin(i*0.6 + math.pi)*50, y1), 
                        end=(500 + math.sin((i+1)*0.6 + math.pi)*50, y2),
                        stroke='#1a75ff', stroke_width=3))
        
        # Base pairs
        if i % 2 == 0:
            dwg.add(dwg.line(start=(300 + math.sin(i*0.6)*50, y1),
                            end=(500 + math.sin(i*0.6 + math.pi)*50, y1),
                            stroke='#ff6666', stroke_width=2))
    
    # Add base pair labels
    dwg.add(dwg.text('A', insert=(320, 150), font_size='16px', fill='#ff6666'))
    dwg.add(dwg.text('T', insert=(480, 150), font_size='16px', fill='#ff6666'))
    dwg.add(dwg.text('G', insert=(320, 190), font_size='16px', fill='#ff6666'))
    dwg.add(dwg.text('C', insert=(480, 190), font_size='16px', fill='#ff6666'))
    
    # Add hydrogen bonds
    dwg.add(dwg.line(start=(340, 150), end=(460, 150), 
                    stroke='#999999', stroke_width=1, stroke_dasharray='2,2'))
    dwg.add(dwg.text('2 H-bonds', insert=(400, 140), 
                     text_anchor='middle', font_size='12px'))
    
    dwg.add(dwg.line(start=(340, 190), end=(460, 190), 
                    stroke='#999999', stroke_width=1, stroke_dasharray='2,2'))
    dwg.add(dwg.text('3 H-bonds', insert=(400, 180), 
                     text_anchor='middle', font_size='12px'))
    
    # Add enzymes
    # DNA Polymerase
    dwg.add(dwg.circle(center=(350, 300), r=30, 
                      fill='#ff9933', stroke='black'))
    dwg.add(dwg.text('DNA', insert=(350, 295), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.text('Polymerase', insert=(350, 310), 
                     text_anchor='middle', font_size='12px'))
    
    # Helicase
    dwg.add(dwg.circle(center=(450, 300), r=30, 
                      fill='#99cc00', stroke='black'))
    dwg.add(dwg.text('Helicase', insert=(450, 300), 
                     text_anchor='middle', font_size='14px'))
    
    # Add enzyme function labels
    dwg.add(dwg.text('Adds new nucleotides', insert=(350, 350), 
                     text_anchor='middle', font_size='12px'))
    dwg.add(dwg.text('Unwinds double helix', insert=(450, 350), 
                     text_anchor='middle', font_size='12px'))
    
    # Add structural labels
    dwg.add(dwg.text('Sugar-Phosphate', insert=(250, 200), 
                     text_anchor='end', font_size='14px'))
    dwg.add(dwg.text('Backbone', insert=(250, 220), 
                     text_anchor='end', font_size='14px'))
    
    dwg.add(dwg.text('Base Pairs', insert=(550, 200), 
                     text_anchor='start', font_size='14px'))
    
    # Add direction arrows
    dwg.add(dwg.text("5'", insert=(300, 80), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.text("3'", insert=(300, 500), 
                     text_anchor='middle', font_size='16px'))
    
    dwg.add(dwg.text("3'", insert=(500, 80), 
                     text_anchor='middle', font_size='16px'))
    dwg.add(dwg.text("5'", insert=(500, 500), 
                     text_anchor='middle', font_size='16px'))
    
    dwg.save()

if __name__ == '__main__':
    # Create images directory if it doesn't exist
    os.makedirs('static/images', exist_ok=True)
    
    # Generate SVG diagrams
    create_levels_of_organization()
    create_cell_comparison()
    create_fluid_mosaic()
    create_metabolic_pathways()
    create_enzyme_action()
    create_cellular_respiration()
    create_fermentation()
    create_light_reactions()
    create_calvin_cycle()
    create_cell_signaling()
    create_signal_transduction()
    create_cell_cycle()
    create_mitosis()
    create_meiosis()
    create_crossing_over()
    create_mendel_experiment()
    create_punnett_square()
    create_sex_chromosomes()
    create_linkage_map()
    create_dna_replication()
    create_evolution_tree()
    create_ecosystem_energy()
    create_transcription()
    create_natural_selection()
    create_population_growth()
    create_dna_structure()
    
    # Create PNG versions
    print("Creating PNG placeholder files...")
    svg_files = [f for f in os.listdir('static/images') if f.endswith('.svg')]
    for svg_file in svg_files:
        svg_path = os.path.join('static/images', svg_file)
        png_path = os.path.join('static/images', svg_file.replace('.svg', '.png'))
        try:
            save_to_png(svg_path, png_path)
        except Exception as e:
            print(f"Error creating PNG for {svg_file}: {e}")
    
    print("Diagrams generated successfully!") 