DEMO_ACCOUNTS = {
    "a.konan": {
        "password": "demo1234",
        "name": "Awa Konan",
        "role": "Responsable commerciale",
        "initials": "AK",
        "email": "a.konan@dpci.ci",
    },
    "p.koffi": {
        "password": "demo1234",
        "name": "Dr Patrick Koffi",
        "role": "Pharmacien responsable",
        "initials": "PK",
        "email": "p.koffi@dpci.ci",
    },
    "m.diabate": {
        "password": "demo1234",
        "name": "Moussa Diabaté",
        "role": "Responsable magasin",
        "initials": "MD",
        "email": "m.diabate@dpci.ci",
    },
}

STATUS_META = {
    "attente": {
        "label": "En attente",
        "badge": "bg-amber-50 text-amber-700 ring-amber-200/70",
        "dot": "bg-amber-500",
        "bar": "bg-amber-500",
        "soft": "bg-amber-50",
        "text": "text-amber-700",
    },
    "preparation": {
        "label": "En préparation",
        "badge": "bg-sky-50 text-sky-700 ring-sky-200/70",
        "dot": "bg-sky-500",
        "bar": "bg-sky-500",
        "soft": "bg-sky-50",
        "text": "text-sky-700",
    },
    "prete": {
        "label": "Prête",
        "badge": "bg-violet-50 text-violet-700 ring-violet-200/70",
        "dot": "bg-violet-500",
        "bar": "bg-violet-500",
        "soft": "bg-violet-50",
        "text": "text-violet-700",
    },
    "expediee": {
        "label": "Expédiée",
        "badge": "bg-indigo-50 text-indigo-700 ring-indigo-200/70",
        "dot": "bg-indigo-500",
        "bar": "bg-indigo-500",
        "soft": "bg-indigo-50",
        "text": "text-indigo-700",
    },
    "livree": {
        "label": "Livrée",
        "badge": "bg-emerald-50 text-emerald-700 ring-emerald-200/70",
        "dot": "bg-emerald-500",
        "bar": "bg-emerald-500",
        "soft": "bg-emerald-50",
        "text": "text-emerald-700",
    },
    "annulee": {
        "label": "Annulée",
        "badge": "bg-rose-50 text-rose-700 ring-rose-200/70",
        "dot": "bg-rose-500",
        "bar": "bg-rose-500",
        "soft": "bg-rose-50",
        "text": "text-rose-700",
    },
}

STATUS_TABS = [
    ("", "Toutes"),
    ("attente", "En attente"),
    ("preparation", "En préparation"),
    ("prete", "Prêtes"),
    ("expediee", "Expédiées"),
    ("livree", "Livrées"),
    ("annulee", "Annulées"),
]

ORDERS = [
    {
        "id": 1,
        "reference": "CMD-2026-0152",
        "client": "Pharmacie du Plateau",
        "client_type": "Pharmacie",
        "city": "Plateau",
        "date": "11 nov. 2026",
        "time": "09:42",
        "amount": 2845500,
        "status": "preparation",
        "priority": "Haute",
        "lines": 4,
        "units": 180,
        "progress": 65,
        "payment": "À crédit 30 jours",
        "contact": "Dr Yao Kouassi",
        "phone": "+225 07 08 45 12 90",
        "address": "Boulevard Lagunaire, Plateau, Abidjan",
        "products": [
            {"name": "Doliprane 1000 mg", "form": "Boîte de 8 comprimés", "lot": "DOL-2610", "expiry": "05/2028", "qty": 60, "price": 950},
            {"name": "Amoxicilline 500 mg", "form": "Gélules, boîte de 12", "lot": "AMX-2409", "expiry": "09/2027", "qty": 45, "price": 1850},
            {"name": "Artéméther/Luméfantrine", "form": "Boîte de 6 comprimés", "lot": "ART-2604", "expiry": "12/2027", "qty": 30, "price": 3200},
            {"name": "Sérum physiologique 0,9 %", "form": "Flacon de 500 ml", "lot": "SER-2608", "expiry": "03/2028", "qty": 45, "price": 1200},
        ],
    },
    {
        "id": 2,
        "reference": "CMD-2026-0151",
        "client": "Clinique La Providence",
        "client_type": "Clinique",
        "city": "Cocody",
        "date": "11 nov. 2026",
        "time": "08:18",
        "amount": 4120000,
        "status": "attente",
        "priority": "Haute",
        "lines": 7,
        "units": 320,
        "progress": 0,
        "payment": "Virement à réception",
        "contact": "Mme Aïcha Bamba",
        "phone": "+225 05 44 78 23 10",
        "address": "Rue des Jardins, Cocody, Abidjan",
        "products": [
            {"name": "Ceftriaxone 1 g", "form": "Flacon injectable", "lot": "CEF-2602", "expiry": "06/2027", "qty": 80, "price": 4200},
            {"name": "Métronidazole 500 mg", "form": "Boîte de 20 comprimés", "lot": "MET-2605", "expiry": "10/2027", "qty": 60, "price": 2100},
            {"name": "NaCl 0,9 % 1 L", "form": "Poche perfusable", "lot": "NAC-2609", "expiry": "02/2028", "qty": 100, "price": 1100},
            {"name": "Diclofénac 75 mg", "form": "Ampoule injectable", "lot": "DIC-2601", "expiry": "08/2027", "qty": 80, "price": 1600},
        ],
    },
    {
        "id": 3,
        "reference": "CMD-2026-0150",
        "client": "Pharmacie Sainte-Marie",
        "client_type": "Pharmacie",
        "city": "Yopougon",
        "date": "10 nov. 2026",
        "time": "17:35",
        "amount": 1260000,
        "status": "prete",
        "priority": "Normale",
        "lines": 3,
        "units": 96,
        "progress": 100,
        "payment": "Mobile money",
        "contact": "M. Serge Gbagbo",
        "phone": "+225 01 02 34 56 78",
        "address": "Route de Dabou, Yopougon, Abidjan",
        "products": [
            {"name": "Paracétamol sirop 120 mg/5 ml", "form": "Flacon de 100 ml", "lot": "PAR-2610", "expiry": "11/2027", "qty": 36, "price": 1800},
            {"name": "Amoxicilline sirop 250 mg/5 ml", "form": "Flacon de 60 ml", "lot": "AMS-2607", "expiry": "07/2027", "qty": 30, "price": 2400},
            {"name": "Ibuprofène 200 mg", "form": "Boîte de 20 comprimés", "lot": "IBU-2603", "expiry": "04/2028", "qty": 30, "price": 1500},
        ],
    },
    {
        "id": 4,
        "reference": "CMD-2026-0149",
        "client": "CHU de Treichville",
        "client_type": "Hôpital",
        "city": "Treichville",
        "date": "10 nov. 2026",
        "time": "15:02",
        "amount": 7890000,
        "status": "expediee",
        "priority": "Haute",
        "lines": 12,
        "units": 640,
        "progress": 100,
        "payment": "Bon de commande public",
        "contact": "Pr Emmanuel N'Guessan",
        "phone": "+225 27 21 24 55 00",
        "address": "Boulevard de Marseille, Treichville, Abidjan",
        "products": [
            {"name": "Ceplosporine 1 g", "form": "Flacon injectable", "lot": "CEP-2601", "expiry": "05/2027", "qty": 120, "price": 5200},
            {"name": "Gentamicine 80 mg", "form": "Ampoule injectable", "lot": "GEN-2604", "expiry": "09/2027", "qty": 100, "price": 1400},
            {"name": "Ringer lactate 1 L", "form": "Poche perfusable", "lot": "RIN-2608", "expiry": "01/2028", "qty": 160, "price": 1200},
            {"name": "Oméprazole 20 mg", "form": "Boîte de 14 gélules", "lot": "OME-2606", "expiry": "03/2028", "qty": 100, "price": 2500},
        ],
    },
    {
        "id": 5,
        "reference": "CMD-2026-0148",
        "client": "Pharmacie de la Riviera",
        "client_type": "Pharmacie",
        "city": "Riviera",
        "date": "10 nov. 2026",
        "time": "11:47",
        "amount": 980000,
        "status": "livree",
        "priority": "Normale",
        "lines": 2,
        "units": 72,
        "progress": 100,
        "payment": "Espèces",
        "contact": "Mme Clarisse Assi",
        "phone": "+225 07 77 12 34 56",
        "address": "Rue Félicité, Riviera 2, Abidjan",
        "products": [
            {"name": "Doliprane 500 mg", "form": "Boîte de 20 comprimés", "lot": "DOL-2607", "expiry": "06/2028", "qty": 48, "price": 1200},
            {"name": "Vitamine C 500 mg", "form": "Boîte de 30 comprimés", "lot": "VIT-2605", "expiry": "10/2027", "qty": 24, "price": 2200},
        ],
    },
    {
        "id": 6,
        "reference": "CMD-2026-0147",
        "client": "Cabinet médical Akwaba",
        "client_type": "Cabinet",
        "city": "Marcory",
        "date": "10 nov. 2026",
        "time": "09:12",
        "amount": 1540000,
        "status": "preparation",
        "priority": "Normale",
        "lines": 5,
        "units": 140,
        "progress": 40,
        "payment": "À crédit 15 jours",
        "contact": "Dr Fatou Cissé",
        "phone": "+225 05 01 23 45 67",
        "address": "Zone 4, Marcory, Abidjan",
        "products": [
            {"name": "Artéméther/Luméfantrine", "form": "Boîte de 6 comprimés", "lot": "ART-2604", "expiry": "12/2027", "qty": 40, "price": 3200},
            {"name": "Doliprane 1000 mg", "form": "Boîte de 8 comprimés", "lot": "DOL-2610", "expiry": "05/2028", "qty": 40, "price": 950},
            {"name": "Amoxicilline 1 g", "form": "Boîte de 12 comprimés", "lot": "AMX-2610", "expiry": "08/2027", "qty": 30, "price": 2800},
            {"name": "Sérum physiologique 0,9 %", "form": "Flacon de 500 ml", "lot": "SER-2608", "expiry": "03/2028", "qty": 30, "price": 1200},
        ],
    },
    {
        "id": 7,
        "reference": "CMD-2026-0146",
        "client": "Pharmacie Les Palmiers",
        "client_type": "Pharmacie",
        "city": "Abobo",
        "date": "09 nov. 2026",
        "time": "16:20",
        "amount": 2210000,
        "status": "livree",
        "priority": "Normale",
        "lines": 6,
        "units": 210,
        "progress": 100,
        "payment": "Mobile money",
        "contact": "M. Issouf Traoré",
        "phone": "+225 01 45 67 89 01",
        "address": "Avenue N'Gatta, Abobo, Abidjan",
        "products": [
            {"name": "Ceftriaxone 1 g", "form": "Flacon injectable", "lot": "CEF-2602", "expiry": "06/2027", "qty": 50, "price": 4200},
            {"name": "Diclofénac 75 mg", "form": "Ampoule injectable", "lot": "DIC-2601", "expiry": "08/2027", "qty": 60, "price": 1600},
            {"name": "Oméprazole 20 mg", "form": "Boîte de 14 gélules", "lot": "OME-2606", "expiry": "03/2028", "qty": 50, "price": 2500},
            {"name": "Doliprane 500 mg", "form": "Boîte de 20 comprimés", "lot": "DOL-2607", "expiry": "06/2028", "qty": 50, "price": 1200},
        ],
    },
    {
        "id": 8,
        "reference": "CMD-2026-0145",
        "client": "Polyclinique Internationale",
        "client_type": "Clinique",
        "city": "Cocody",
        "date": "09 nov. 2026",
        "time": "14:05",
        "amount": 5430000,
        "status": "annulee",
        "priority": "Normale",
        "lines": 9,
        "units": 410,
        "progress": 0,
        "payment": "Virement bancaire",
        "contact": "Mme Nadège Kacou",
        "phone": "+225 27 22 44 66 88",
        "address": "Boulevard de France, Cocody, Abidjan",
        "products": [
            {"name": "Métronidazole 500 mg", "form": "Boîte de 20 comprimés", "lot": "MET-2605", "expiry": "10/2027", "qty": 90, "price": 2100},
            {"name": "Gentamicine 80 mg", "form": "Ampoule injectable", "lot": "GEN-2604", "expiry": "09/2027", "qty": 110, "price": 1400},
            {"name": "NaCl 0,9 % 1 L", "form": "Poche perfusable", "lot": "NAC-2609", "expiry": "02/2028", "qty": 120, "price": 1100},
            {"name": "Paracétamol 1 g", "form": "Boîte de 8 comprimés", "lot": "PAR-2608", "expiry": "04/2028", "qty": 90, "price": 1100},
        ],
    },
    {
        "id": 9,
        "reference": "CMD-2026-0144",
        "client": "Pharmacie Bel Air",
        "client_type": "Pharmacie",
        "city": "Bingerville",
        "date": "09 nov. 2026",
        "time": "10:33",
        "amount": 760000,
        "status": "livree",
        "priority": "Basse",
        "lines": 2,
        "units": 48,
        "progress": 100,
        "payment": "Espèces",
        "contact": "M. Alain N'Dri",
        "phone": "+225 07 10 20 30 40",
        "address": "Centre-ville, Bingerville",
        "products": [
            {"name": "Ibuprofène 200 mg", "form": "Boîte de 20 comprimés", "lot": "IBU-2603", "expiry": "04/2028", "qty": 24, "price": 1500},
            {"name": "Vitamine C 500 mg", "form": "Boîte de 30 comprimés", "lot": "VIT-2605", "expiry": "10/2027", "qty": 24, "price": 2200},
        ],
    },
    {
        "id": 10,
        "reference": "CMD-2026-0143",
        "client": "Hôpital Général d'Abobo",
        "client_type": "Hôpital",
        "city": "Abobo",
        "date": "08 nov. 2026",
        "time": "16:58",
        "amount": 3680000,
        "status": "livree",
        "priority": "Haute",
        "lines": 8,
        "units": 290,
        "progress": 100,
        "payment": "Bon de commande public",
        "contact": "Dr Bakary Sanogo",
        "phone": "+225 27 24 38 12 00",
        "address": "Route d'Anyama, Abobo, Abidjan",
        "products": [
            {"name": "Ringer lactate 1 L", "form": "Poche perfusable", "lot": "RIN-2608", "expiry": "01/2028", "qty": 100, "price": 1200},
            {"name": "Ceftriaxone 1 g", "form": "Flacon injectable", "lot": "CEF-2602", "expiry": "06/2027", "qty": 70, "price": 4200},
            {"name": "Paracétamol 1 g", "form": "Boîte de 8 comprimés", "lot": "PAR-2608", "expiry": "04/2028", "qty": 60, "price": 1100},
            {"name": "Oméprazole 20 mg", "form": "Boîte de 14 gélules", "lot": "OME-2606", "expiry": "03/2028", "qty": 60, "price": 2500},
        ],
    },
    {
        "id": 11,
        "reference": "CMD-2026-0142",
        "client": "Pharmacie Saint-Jean",
        "client_type": "Pharmacie",
        "city": "Koumassi",
        "date": "08 nov. 2026",
        "time": "12:24",
        "amount": 1120000,
        "status": "livree",
        "priority": "Normale",
        "lines": 3,
        "units": 88,
        "progress": 100,
        "payment": "À crédit 30 jours",
        "contact": "Mme Estelle Yao",
        "phone": "+225 05 88 77 66 55",
        "address": "Boulevard du Gabon, Koumassi, Abidjan",
        "products": [
            {"name": "Amoxicilline 500 mg", "form": "Gélules, boîte de 12", "lot": "AMX-2409", "expiry": "09/2027", "qty": 40, "price": 1850},
            {"name": "Doliprane 500 mg", "form": "Boîte de 20 comprimés", "lot": "DOL-2607", "expiry": "06/2028", "qty": 30, "price": 1200},
            {"name": "Sérum physiologique 0,9 %", "form": "Flacon de 500 ml", "lot": "SER-2608", "expiry": "03/2028", "qty": 18, "price": 1200},
        ],
    },
    {
        "id": 12,
        "reference": "CMD-2026-0141",
        "client": "Centre de Santé Adjamé",
        "client_type": "Centre de santé",
        "city": "Adjamé",
        "date": "08 nov. 2026",
        "time": "08:50",
        "amount": 2950000,
        "status": "attente",
        "priority": "Normale",
        "lines": 6,
        "units": 230,
        "progress": 0,
        "payment": "Virement à réception",
        "contact": "M. Ousmane Fofana",
        "phone": "+225 01 11 22 33 44",
        "address": "Rue du Marché, Adjamé, Abidjan",
        "products": [
            {"name": "Artéméther/Luméfantrine", "form": "Boîte de 6 comprimés", "lot": "ART-2604", "expiry": "12/2027", "qty": 50, "price": 3200},
            {"name": "Paracétamol sirop 120 mg/5 ml", "form": "Flacon de 100 ml", "lot": "PAR-2610", "expiry": "11/2027", "qty": 40, "price": 1800},
            {"name": "Amoxicilline sirop 250 mg/5 ml", "form": "Flacon de 60 ml", "lot": "AMS-2607", "expiry": "07/2027", "qty": 40, "price": 2400},
            {"name": "Métronidazole 500 mg", "form": "Boîte de 20 comprimés", "lot": "MET-2605", "expiry": "10/2027", "qty": 50, "price": 2100},
        ],
    },
]

KPIS = [
    {
        "label": "Chiffre d'affaires du jour",
        "value": "4 820 000 F",
        "trend": "+12,4 %",
        "trend_label": "vs hier",
        "positive": True,
        "icon": "wallet",
        "tone": "teal",
        "spark": [18, 22, 20, 27, 25, 31, 38, 36, 44, 48],
    },
    {
        "label": "Commandes du jour",
        "value": "38",
        "trend": "+8,1 %",
        "trend_label": "vs hier",
        "positive": True,
        "icon": "cart",
        "tone": "sky",
        "spark": [12, 18, 15, 21, 19, 25, 23, 29, 27, 34],
    },
    {
        "label": "En préparation",
        "value": "7",
        "trend": "2 urgentes",
        "trend_label": "à traiter",
        "positive": False,
        "icon": "clipboard",
        "tone": "amber",
        "spark": [8, 9, 7, 10, 11, 8, 9, 7, 8, 7],
    },
    {
        "label": "Alertes stock",
        "value": "5",
        "trend": "1 critique",
        "trend_label": "à vérifier",
        "positive": False,
        "icon": "alert",
        "tone": "rose",
        "spark": [3, 4, 4, 3, 5, 4, 6, 5, 6, 5],
    },
]

REVENUE_CHART = {
    "7j": {
        "labels": ["05 nov.", "06 nov.", "07 nov.", "08 nov.", "09 nov.", "10 nov.", "11 nov."],
        "revenue": [3.2, 4.1, 3.8, 5.4, 4.9, 6.2, 4.8],
        "orders": [22, 28, 26, 35, 31, 41, 38],
    },
    "30j": {
        "labels": ["12 oct.", "15 oct.", "18 oct.", "21 oct.", "24 oct.", "27 oct.", "30 oct.", "02 nov.", "05 nov.", "08 nov.", "11 nov."],
        "revenue": [18.4, 21.2, 19.8, 24.6, 22.1, 26.8, 25.3, 28.9, 27.4, 31.2, 29.6],
        "orders": [118, 132, 126, 148, 139, 156, 151, 163, 158, 172, 168],
    },
}

PIPELINE = [
    {"label": "En attente", "count": 2, "color": "bg-amber-400", "text": "text-amber-700"},
    {"label": "En préparation", "count": 2, "color": "bg-sky-400", "text": "text-sky-700"},
    {"label": "Prêtes", "count": 1, "color": "bg-violet-400", "text": "text-violet-700"},
    {"label": "Expédiées", "count": 1, "color": "bg-indigo-400", "text": "text-indigo-700"},
    {"label": "Livrées", "count": 5, "color": "bg-emerald-400", "text": "text-emerald-700"},
    {"label": "Annulées", "count": 1, "color": "bg-rose-400", "text": "text-rose-700"},
]

STOCK_ALERTS = [
    {
        "title": "Lot AMX-2409 proche péremption",
        "detail": "Expire dans 12 jours · 1 240 unités",
        "severity": "Élevée",
        "tone": "amber",
        "icon": "clock",
    },
    {
        "title": "Doliprane 500 mg sous seuil",
        "detail": "180 unités restantes · seuil 300",
        "severity": "Critique",
        "tone": "rose",
        "icon": "alert",
    },
    {
        "title": "Lot PAR-2211 rappelé",
        "detail": "Laboratoire Sanofi · blocage immédiat",
        "severity": "Critique",
        "tone": "rose",
        "icon": "shield",
    },
    {
        "title": "3 lots en quarantaine",
        "detail": "Contrôle qualité en attente",
        "severity": "Moyenne",
        "tone": "sky",
        "icon": "box",
    },
]

TOP_PRODUCTS = [
    {"name": "Doliprane 1000 mg", "category": "Antalgique", "units": 3200, "share": 92, "color": "bg-teal-500"},
    {"name": "Amoxicilline 500 mg", "category": "Antibiotique", "units": 2100, "share": 74, "color": "bg-sky-500"},
    {"name": "Artéméther/Luméfantrine", "category": "Antipaludique", "units": 1800, "share": 63, "color": "bg-violet-500"},
    {"name": "Paracétamol sirop", "category": "Pédiatrie", "units": 1450, "share": 51, "color": "bg-amber-500"},
    {"name": "Métronidazole 500 mg", "category": "Antibiotique", "units": 980, "share": 34, "color": "bg-rose-500"},
]

ACTIVITY = [
    {"title": "Commande CMD-2026-0152 passée en préparation", "by": "Awa Konan", "time": "Il y a 8 min", "tone": "sky", "icon": "clipboard"},
    {"title": "Réception du lot DOL-2609 validée", "by": "Moussa Diabaté", "time": "Il y a 32 min", "tone": "emerald", "icon": "box"},
    {"title": "Alerte stock créée pour Doliprane 500 mg", "by": "Système", "time": "Il y a 1 h", "tone": "amber", "icon": "alert"},
    {"title": "Livraison CMD-2026-0148 confirmée", "by": "Awa Konan", "time": "Il y a 2 h", "tone": "teal", "icon": "truck"},
    {"title": "Rappel du lot PAR-2211 déclenché", "by": "Dr Patrick Koffi", "time": "Il y a 3 h", "tone": "rose", "icon": "shield"},
]


def _initials(value):
    parts = [part for part in str(value).replace("-", " ").split() if part]
    if not parts:
        return "DP"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def decorate(order):
    item = {**order}
    item["status_meta"] = STATUS_META[order["status"]]
    item["initials"] = _initials(order["client"])
    item["items_preview"] = order["products"][:3]
    item["remaining_products"] = max(0, len(order["products"]) - 3)
    return item


def all_orders():
    return [decorate(order) for order in ORDERS]


def get_order(order_id):
    for order in ORDERS:
        if order["id"] == int(order_id):
            return decorate(order)
    return None


def filter_orders(query="", status="", client=""):
    query = (query or "").strip().lower()
    result = []
    for order in all_orders():
        if status and order["status"] != status:
            continue
        if client and order["client"] != client:
            continue
        if query:
            haystack = " ".join(
                [
                    order["reference"],
                    order["client"],
                    order["city"],
                    order["contact"],
                    order["status_meta"]["label"],
                ]
            ).lower()
            if query not in haystack:
                continue
        result.append(order)
    return result


def status_counts():
    counts = {key: 0 for key in STATUS_META}
    for order in ORDERS:
        counts[order["status"]] += 1
    return counts


def clients():
    return sorted({order["client"] for order in ORDERS})
