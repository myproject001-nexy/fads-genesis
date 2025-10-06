#!/usr/bin/env python3
"""
Script per creare il database Personae_Simulate.json
Integra ricerca approfondita su Gebru e Senge con ricerca parallela su altri 10 esperti
"""

import json
from datetime import datetime

# Carica i risultati della ricerca parallela
with open('/home/ubuntu/fads-genesis/02_COMMUNITY/ricerca_profili_esperti.json', 'r') as f:
    ricerca_parallela = json.load(f)

# Database personae
personae = []

# 1. Timnit Gebru (ricerca approfondita manuale)
personae.append({
    "id": 1,
    "nome": "Timnit Gebru",
    "ruolo_primario": "AI Ethics Researcher, Founder of DAIR",
    "organizzazione": "Distributed AI Research Institute (DAIR)",
    "tesi_principali": [
        "Large Language Models hanno costi ambientali enormi che beneficiano solo organizzazioni ricche",
        "Dataset troppo grandi per essere documentati perpetuano danni senza ricorso",
        "AI riflette e amplifica discriminazione esistente contro comunità marginalizzate",
        "Necessità di cambiamento istituzionale e strutturale per AI etica",
        "Slow AI Movement: rallentare per fare meglio, con prospettive diverse"
    ],
    "stile_comunicativo": "Diretto e senza compromessi, basato su evidenza empirica, focus su impatto sociale e giustizia, prospettiva intersezionale, critica sistemica ma costruttiva",
    "focus_probabile_su_fads": "Apprezzerebbe trasparenza e supervisione umana, ma chiederà: trasparenza per chi? Supervisione di quali umani? Manca analisi di potere, prospettiva geografica/culturale, meccanismi per coinvolgere comunità marginalizzate, affrontare costi ambientali",
    "citazioni_chiave": [
        "A methodology that relies on datasets too large to document is therefore inherently risky",
        "It is past time for researchers to prioritize energy efficiency and cost",
        "Ethical AI requires institutional and structural change"
    ],
    "opere_fondamentali": [
        "On the Dangers of Stochastic Parrots (2021)",
        "Gender Shades (con Joy Buolamwini)",
        "The TESCREAL bundle (2024)"
    ]
})

# 2. Peter Senge (ricerca approfondita manuale)
personae.append({
    "id": 2,
    "nome": "Peter Senge",
    "ruolo_primario": "Systems Thinking Expert, Learning Organization Pioneer",
    "organizzazione": "MIT Sloan School of Management, Society for Organizational Learning",
    "tesi_principali": [
        "Learning Organization: capacità di apprendere più velocemente della competizione è unico vantaggio sostenibile",
        "Systems Thinking integra le altre 4 discipline: Personal Mastery, Mental Models, Shared Vision, Team Learning",
        "Vedere strutture sistemiche sottostanti, non solo eventi isolati",
        "Leader come designer, teacher e steward (non comandante)",
        "Empowerment senza allineamento porta solo caos"
    ],
    "stile_comunicativo": "Olistico e integrativo, pragmatico ma visionario, collaborativo e non gerarchico, paziente e orientato al processo, ottimista ma realistico, accessibile e didattico",
    "focus_probabile_su_fads": "Apprezzerebbe trasparenza (simile a rendere espliciti mental models) e approccio sistemico. Chiederà: come diventa FADS una learning organization? Dove sono i feedback loops? Come si sviluppa personal mastery? Come si crea shared vision? Troppo focus su regole, poco su apprendimento",
    "citazioni_chiave": [
        "In the long run, the only sustainable source of competitive advantage is your organization's ability to learn faster than the competition",
        "We cannot address issues that we don't see",
        "Empowering individuals when there is no or low alignment only brings chaos"
    ],
    "opere_fondamentali": [
        "The Fifth Discipline (1990, revised 2006)",
        "The Fifth Discipline Fieldbook (1994)"
    ]
})

# Aggiungi i risultati della ricerca parallela
for idx, result in enumerate(ricerca_parallela['results'], start=3):
    if result['error']:
        continue
    
    output = result['output']
    
    # Converti tesi_principali da stringa separata da ; a lista
    tesi_list = [t.strip() for t in output['tesi_principali'].split(';') if t.strip()]
    
    # Converti citazioni da stringa a lista
    citazioni_list = [c.strip().strip('"') for c in output['citazioni_chiave'].split('";') if c.strip()]
    
    # Estrai opere fondamentali
    opere_list = []
    for line in output['opere_fondamentali'].split('\n'):
        if line.strip() and line.strip().startswith('**'):
            # Estrai titolo tra **
            title_end = line.find('**', 2)
            if title_end > 0:
                opere_list.append(line[2:title_end].strip())
    
    personae.append({
        "id": idx,
        "nome": output['nome_esperto'],
        "ruolo_primario": result['input'].split(' - ', 1)[1] if ' - ' in result['input'] else "Expert",
        "organizzazione": "Vedi opere fondamentali",
        "tesi_principali": tesi_list[:5],  # Max 5
        "stile_comunicativo": output['stile_comunicativo'],
        "focus_probabile_su_fads": output['focus_probabile_fads'],
        "citazioni_chiave": citazioni_list[:3],  # Max 3
        "opere_fondamentali": opere_list
    })

# Crea il database finale
database = {
    "metadata": {
        "versione": "1.0",
        "data_creazione": datetime.now().isoformat(),
        "descrizione": "Database delle Personae Simulate per il Protocollo del Consiglio delle Menti Simulate - Progetto FADS Genesis",
        "totale_profili": len(personae),
        "metodo": "Ricerca approfondita manuale (Gebru, Senge) + ricerca parallela automatizzata (10 esperti)"
    },
    "personae": personae
}

# Salva il database
output_path = '/home/ubuntu/fads-genesis/02_COMMUNITY/Personae_Simulate.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(database, f, ensure_ascii=False, indent=2)

print(f"✅ Database Personae_Simulate.json creato con successo!")
print(f"📊 Totale profili: {len(personae)}")
print(f"📁 Percorso: {output_path}")
print("\n🎭 Profili inclusi:")
for p in personae:
    print(f"  {p['id']}. {p['nome']} - {p['ruolo_primario']}")

