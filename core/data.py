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


TONE_META = {
    "rose": {
        "badge": "bg-rose-50 text-rose-700 ring-rose-200/70",
        "dot": "bg-rose-500",
        "icon": "bg-rose-50 text-rose-600",
        "soft": "bg-rose-50",
        "text": "text-rose-700",
    },
    "amber": {
        "badge": "bg-amber-50 text-amber-700 ring-amber-200/70",
        "dot": "bg-amber-500",
        "icon": "bg-amber-50 text-amber-600",
        "soft": "bg-amber-50",
        "text": "text-amber-700",
    },
    "blue": {
        "badge": "bg-sky-50 text-sky-700 ring-sky-200/70",
        "dot": "bg-sky-500",
        "icon": "bg-sky-50 text-sky-600",
        "soft": "bg-sky-50",
        "text": "text-sky-700",
    },
    "violet": {
        "badge": "bg-violet-50 text-violet-700 ring-violet-200/70",
        "dot": "bg-violet-500",
        "icon": "bg-violet-50 text-violet-600",
        "soft": "bg-violet-50",
        "text": "text-violet-700",
    },
    "green": {
        "badge": "bg-emerald-50 text-emerald-700 ring-emerald-200/70",
        "dot": "bg-emerald-500",
        "icon": "bg-emerald-50 text-emerald-600",
        "soft": "bg-emerald-50",
        "text": "text-emerald-700",
    },
    "teal": {
        "badge": "bg-brand-50 text-brand-700 ring-brand-200/70",
        "dot": "bg-brand-500",
        "icon": "bg-brand-50 text-brand-700",
        "soft": "bg-brand-50",
        "text": "text-brand-700",
    },
    "slate": {
        "badge": "bg-slate-100 text-slate-600 ring-slate-200",
        "dot": "bg-slate-400",
        "icon": "bg-slate-100 text-slate-500",
        "soft": "bg-slate-50",
        "text": "text-slate-600",
    },
}

ALERT_CATEGORIES = [
    ("", "Toutes"),
    ("peremption", "Péremption"),
    ("stock", "Stock"),
    ("rappel", "Rappels"),
    ("systeme", "Système"),
]

ALERTS = [
    {
        "id": 1,
        "category": "peremption",
        "title": "Lot périmé bloqué automatiquement",
        "detail": "LOT-2026-F032 · Metformine 850 mg · péremption 28/10/2026. Stock retiré de la vente.",
        "severity": "Critique",
        "tone": "rose",
        "icon": "alert",
        "time": "Il y a 2 h",
        "source": "contrôle automatique",
        "action_label": "Voir le lot",
        "action_url": "stock_lots",
        "query": "?q=LOT-2026-F032",
        "unread": True,
    },
    {
        "id": 2,
        "category": "peremption",
        "title": "Péremption proche · J-12",
        "detail": "LOT-2026-A184 · Doliprane 1000 mg · 42 unités restantes. Prioriser en préparation FEFO.",
        "severity": "Péremption",
        "tone": "amber",
        "icon": "clock",
        "time": "Aujourd'hui · 08:05",
        "source": "seuil 30 jours",
        "action_label": "Traiter",
        "action_url": "stock_lots",
        "query": "?q=LOT-2026-A184",
        "unread": True,
    },
    {
        "id": 3,
        "category": "stock",
        "title": "Stock sous le seuil · Amoxicilline 500 mg",
        "detail": "18 unités disponibles pour un seuil de 50. Délai fournisseur estimé : 3 jours.",
        "severity": "Stock",
        "tone": "amber",
        "icon": "box",
        "time": "Il y a 3 h",
        "source": "seuil de réapprovisionnement",
        "action_label": "Commander",
        "action_url": "commande_nouvelle",
        "query": "",
        "unread": True,
    },
    {
        "id": 4,
        "category": "rappel",
        "title": "Rappel de lot en cours",
        "detail": "LOT-2026-A184 · 6 clients concernés · 4 notifications envoyées sur 6.",
        "severity": "Rappel",
        "tone": "blue",
        "icon": "shield",
        "time": "Il y a 5 h",
        "source": "pharmacien responsable",
        "action_label": "Suivre",
        "action_url": "rappel_lot",
        "query": "",
        "unread": True,
    },
    {
        "id": 5,
        "category": "stock",
        "title": "Rupture de stock · Artéméther/Luméfantrine",
        "detail": "0 unité disponible · 2 commandes en attente de stock.",
        "severity": "Rupture",
        "tone": "rose",
        "icon": "ban",
        "time": "Hier · 17:40",
        "source": "stock central",
        "action_label": "Réapprovisionner",
        "action_url": "commande_nouvelle",
        "query": "",
        "unread": False,
    },
    {
        "id": 6,
        "category": "stock",
        "title": "Lot en quarantaine · LOT-2026-H077",
        "detail": "Ibuprofène 400 mg · contrôle qualité en attente depuis 48 h.",
        "severity": "Qualité",
        "tone": "violet",
        "icon": "lock",
        "time": "Hier · 11:20",
        "source": "non disponible à la vente",
        "action_label": "Contrôler",
        "action_url": "stock_lots",
        "query": "?q=LOT-2026-H077",
        "unread": False,
    },
    {
        "id": 7,
        "category": "systeme",
        "title": "Sauvegarde quotidienne terminée",
        "detail": "Base de données sauvegardée · 2,4 Go · conservation 30 jours.",
        "severity": "Système",
        "tone": "slate",
        "icon": "check-circle",
        "time": "Aujourd'hui · 02:00",
        "source": "système",
        "action_label": "Détails",
        "action_url": "administration",
        "query": "",
        "unread": False,
    },
]

ALERT_RULES = [
    {"title": "Péremption < 30 jours", "detail": "Alerte quotidienne · lot + quantité", "enabled": True, "locked": True},
    {"title": "Stock sous le seuil", "detail": "Seuil défini par produit", "enabled": True, "locked": False},
    {"title": "Rappel de lot", "detail": "Notification immédiate · tous rôles", "enabled": True, "locked": True},
    {"title": "Rupture de stock", "detail": "Commande en attente impactée", "enabled": False, "locked": False},
]


def decorate_alert(alert):
    item = {**alert}
    item["tone_meta"] = TONE_META[alert["tone"]]
    return item


def filter_alerts(category="", query=""):
    query = (query or "").strip().lower()
    alerts = []
    for alert in ALERTS:
        if category and alert["category"] != category:
            continue
        if query and query not in f"{alert['title']} {alert['detail']}".lower():
            continue
        alerts.append(decorate_alert(alert))
    return alerts


def alert_counts():
    counts = {key: 0 for key, _ in ALERT_CATEGORIES}
    counts[""] = len(ALERTS)
    for alert in ALERTS:
        counts[alert["category"]] += 1
    return counts


DELIVERY_META = {
    "attente": {"label": "En attente", "tone": "slate"},
    "encours": {"label": "En cours", "tone": "blue"},
    "livree": {"label": "Livrée", "tone": "green"},
    "retournee": {"label": "Retournée", "tone": "rose"},
}

DELIVERY_TABS = [
    ("", "Toutes"),
    ("attente", "En attente"),
    ("encours", "En cours"),
    ("livree", "Livrées"),
    ("retournee", "Retournées"),
]

DELIVERIES = [
    {
        "reference": "BL-2026-0184",
        "order": "CMD-2026-0152",
        "order_id": 1,
        "client": "Pharmacie du Plateau",
        "client_type": "Pharmacie",
        "zone": "Plateau",
        "driver": "S. Traoré",
        "status": "encours",
        "date": "11 nov. 2026",
        "time": "09:50",
        "parcels": 4,
    },
    {
        "reference": "BL-2026-0183",
        "order": "CMD-2026-0150",
        "order_id": 3,
        "client": "Pharmacie Sainte-Marie",
        "client_type": "Pharmacie",
        "zone": "Marcory",
        "driver": "A. Yao",
        "status": "attente",
        "date": "11 nov. 2026",
        "time": "09:15",
        "parcels": 2,
    },
    {
        "reference": "BL-2026-0182",
        "order": "CMD-2026-0149",
        "order_id": 4,
        "client": "CHU de Treichville",
        "client_type": "Structure de santé",
        "zone": "Treichville",
        "driver": "S. Traoré",
        "status": "encours",
        "date": "11 nov. 2026",
        "time": "08:40",
        "parcels": 6,
    },
    {
        "reference": "BL-2026-0181",
        "order": "CMD-2026-0146",
        "order_id": 7,
        "client": "Pharmacie Les Palmiers",
        "client_type": "Pharmacie",
        "zone": "Abobo",
        "driver": "A. Yao",
        "status": "livree",
        "date": "11 nov. 2026",
        "time": "08:05",
        "parcels": 5,
    },
    {
        "reference": "BL-2026-0180",
        "order": "CMD-2026-0144",
        "order_id": 9,
        "client": "Pharmacie Bel Air",
        "client_type": "Pharmacie",
        "zone": "Bingerville",
        "driver": "K. Bamba",
        "status": "livree",
        "date": "10 nov. 2026",
        "time": "17:30",
        "parcels": 2,
    },
    {
        "reference": "BL-2026-0179",
        "order": "CMD-2026-0143",
        "order_id": 10,
        "client": "Hôpital Général d'Abobo",
        "client_type": "Structure de santé",
        "zone": "Abobo",
        "driver": "K. Bamba",
        "status": "retournee",
        "date": "10 nov. 2026",
        "time": "16:20",
        "parcels": 8,
    },
]

DELIVERY_TOUR = {
    "driver": "S. Traoré",
    "vehicle": "Camion CI-4821-AB",
    "zone": "Plateau / Treichville",
    "window": "07:30 → 13:00",
    "done": 2,
    "total": 5,
    "progress": 40,
    "stops": [
        {"client": "Pharmacie du Plateau", "reference": "BL-2026-0184", "parcels": 4, "status": "En cours", "tone": "blue", "icon": "truck"},
        {"client": "CHU de Treichville", "reference": "BL-2026-0182", "parcels": 6, "status": "En cours", "tone": "blue", "icon": "truck"},
        {"client": "Clinique La Providence", "reference": "BL-2026-0185", "parcels": 2, "status": "À venir", "tone": "slate", "icon": "clock"},
    ],
}

LAST_DELIVERY = {
    "reference": "BL-2026-0181",
    "client": "Pharmacie Les Palmiers",
    "order": "CMD-2026-0146",
    "driver": "A. Yao",
    "date": "11/11/2026",
    "products": [
        {"name": "Ceftriaxone 1 g", "lot": "LOT-2026-C021", "expiry": "06/2027", "qty": 50},
        {"name": "Oméprazole 20 mg", "lot": "LOT-2027-D008", "expiry": "04/2027", "qty": 50},
    ],
}


def decorate_delivery(delivery):
    item = {**delivery}
    meta = DELIVERY_META[delivery["status"]]
    item["status_label"] = meta["label"]
    item["tone_meta"] = TONE_META[meta["tone"]]
    item["initials"] = _initials(delivery["client"])
    return item


def filter_deliveries(status="", query="", zone="", driver=""):
    query = (query or "").strip().lower()
    result = []
    for delivery in DELIVERIES:
        if status and delivery["status"] != status:
            continue
        if zone and delivery["zone"] != zone:
            continue
        if driver and delivery["driver"] != driver:
            continue
        if query and query not in f"{delivery['reference']} {delivery['order']} {delivery['client']} {delivery['zone']}".lower():
            continue
        result.append(decorate_delivery(delivery))
    return result


def delivery_counts():
    counts = {key: 0 for key, _ in DELIVERY_TABS}
    counts[""] = len(DELIVERIES)
    for delivery in DELIVERIES:
        counts[delivery["status"]] += 1
    return counts


STOCK_STATUS_META = {
    "disponible": {"label": "Disponible", "tone": "green"},
    "perime": {"label": "Périmé", "tone": "rose"},
    "quarantaine": {"label": "Quarantaine", "tone": "violet"},
    "retire": {"label": "Retiré", "tone": "slate"},
}

STOCK_LOTS = [
    {
        "product": "Doliprane 1000 mg",
        "code": "PAR-1000",
        "form": "Comprimé",
        "category": "Antalgique",
        "supplier": "Laborex CI",
        "lot": "LOT-2026-A184",
        "qty": 42,
        "expiry": "23/11/2026",
        "days": "J-12",
        "expiry_tone": "rose",
        "status": "disponible",
        "location": "A-12",
        "price": 3500,
    },
    {
        "product": "Amoxicilline 500 mg",
        "code": "AMX-500",
        "form": "Gélule",
        "category": "Antibiotique",
        "supplier": "COPHARMA",
        "lot": "LOT-2026-C041",
        "qty": 98,
        "expiry": "28/12/2026",
        "days": "J-47",
        "expiry_tone": "amber",
        "status": "disponible",
        "location": "B-04",
        "price": 2800,
    },
    {
        "product": "Oméprazole 20 mg",
        "code": "OMP-20",
        "form": "Gélule",
        "category": "Gastro-entérologie",
        "supplier": "Ubipharm",
        "lot": "LOT-2027-D008",
        "qty": 152,
        "expiry": "04/2027",
        "days": "J-144",
        "expiry_tone": "green",
        "status": "disponible",
        "location": "A-07",
        "price": 4200,
    },
    {
        "product": "Metformine 850 mg",
        "code": "MET-850",
        "form": "Comprimé",
        "category": "Diabétologie",
        "supplier": "TEDIS Pharma",
        "lot": "LOT-2026-F032",
        "qty": 18,
        "expiry": "28/10/2026",
        "days": "Périmé",
        "expiry_tone": "rose",
        "status": "perime",
        "location": "C-09",
        "price": 2100,
    },
    {
        "product": "Paracétamol sirop 120 mg/5 ml",
        "code": "PCS-120",
        "form": "Sirop",
        "category": "Pédiatrie",
        "supplier": "Laborex CI",
        "lot": "LOT-2027-G015",
        "qty": 76,
        "expiry": "02/2027",
        "days": "J-83",
        "expiry_tone": "green",
        "status": "disponible",
        "location": "A-03",
        "price": 1800,
    },
    {
        "product": "Ibuprofène 400 mg",
        "code": "IBU-400",
        "form": "Comprimé",
        "category": "Anti-inflammatoire",
        "supplier": "COPHARMA",
        "lot": "LOT-2026-H077",
        "qty": 64,
        "expiry": "05/12/2026",
        "days": "J-24",
        "expiry_tone": "amber",
        "status": "quarantaine",
        "location": "B-11",
        "price": 1500,
    },
    {
        "product": "Artéméther-Luméfantrine 80/480",
        "code": "ART-8048",
        "form": "Comprimé",
        "category": "Antipaludique",
        "supplier": "Ubipharm",
        "lot": "LOT-2026-K019",
        "qty": 210,
        "expiry": "01/2027",
        "days": "J-51",
        "expiry_tone": "green",
        "status": "disponible",
        "location": "C-02",
        "price": 6500,
    },
    {
        "product": "Seringue 5 ml",
        "code": "SER-005",
        "form": "Dispositif médical",
        "category": "Consommable",
        "supplier": "TEDIS Pharma",
        "lot": "LOT-2027-E021",
        "qty": 480,
        "expiry": "08/2028",
        "days": "J-650",
        "expiry_tone": "green",
        "status": "disponible",
        "location": "C-02",
        "price": 350,
    },
]

STOCK_PRODUCTS = [
    {"code": "PAR-1000", "name": "Doliprane 1000 mg", "form": "Comprimé", "category": "Antalgique", "price": 3500, "threshold": 50, "stock": 240, "status": "ok"},
    {"code": "AMX-500", "name": "Amoxicilline 500 mg", "form": "Gélule", "category": "Antibiotique", "price": 2800, "threshold": 100, "stock": 98, "status": "low"},
    {"code": "OMP-20", "name": "Oméprazole 20 mg", "form": "Gélule", "category": "Gastro-entérologie", "price": 4200, "threshold": 40, "stock": 152, "status": "ok"},
    {"code": "MET-850", "name": "Metformine 850 mg", "form": "Comprimé", "category": "Diabétologie", "price": 2100, "threshold": 60, "stock": 18, "status": "critical"},
    {"code": "ART-8048", "name": "Artéméther-Luméfantrine 80/480", "form": "Comprimé", "category": "Antipaludique", "price": 6500, "threshold": 80, "stock": 210, "status": "ok"},
    {"code": "SER-005", "name": "Seringue 5 ml", "form": "Dispositif médical", "category": "Consommable", "price": 350, "threshold": 300, "stock": 480, "status": "ok"},
]

STOCK_MOVEMENTS = [
    {"date": "11/11 · 09:22", "type": "Sortie", "tone": "blue", "lot": "LOT-2026-A184", "qty": "-60", "user": "M. Diabaté", "reason": "Préparation CMD-2026-0152"},
    {"date": "11/11 · 08:45", "type": "Entrée", "tone": "green", "lot": "LOT-2027-E021", "qty": "+480", "user": "M. Diabaté", "reason": "Réception TEDIS Pharma"},
    {"date": "11/11 · 08:10", "type": "Retrait", "tone": "violet", "lot": "LOT-2026-F032", "qty": "-18", "user": "Dr P. Koffi", "reason": "Lot périmé — destruction"},
    {"date": "10/11 · 17:40", "type": "Ajustement", "tone": "amber", "lot": "LOT-2026-H077", "qty": "-4", "user": "M. Diabaté", "reason": "Inventaire — casse"},
    {"date": "10/11 · 15:02", "type": "Sortie", "tone": "blue", "lot": "LOT-2026-C041", "qty": "-98", "user": "M. Diabaté", "reason": "Préparation CMD-2026-0151"},
]

STOCK_STATS = {
    "value": "48,2 M FCFA",
    "under_threshold": 4,
    "watched": 7,
    "expired": 3,
    "products": 46,
    "lots": 128,
    "movements": 342,
}


def decorate_lot(lot):
    item = {**lot}
    meta = STOCK_STATUS_META[lot["status"]]
    item["status_label"] = meta["label"]
    item["status_tone"] = TONE_META[meta["tone"]]
    item["expiry_tone_meta"] = TONE_META[lot["expiry_tone"]]
    item["value"] = lot["qty"] * lot["price"]
    return item


def filter_lots(query="", category="", status="", expiry=""):
    query = (query or "").strip().lower()
    result = []
    for lot in STOCK_LOTS:
        if category and lot["category"] != category:
            continue
        if status and lot["status"] != status:
            continue
        if expiry == "30" and not (lot["expiry_tone"] == "rose" and lot["status"] != "perime"):
            continue
        if expiry == "90" and lot["expiry_tone"] == "green":
            continue
        if expiry == "expired" and lot["status"] != "perime":
            continue
        if query and query not in f"{lot['product']} {lot['code']} {lot['lot']} {lot['supplier']}".lower():
            continue
        result.append(decorate_lot(lot))
    return result


def stock_lot(lot_number):
    for lot in STOCK_LOTS:
        if lot["lot"] == lot_number:
            return decorate_lot(lot)
    return decorate_lot(STOCK_LOTS[0])


SUPPLIERS = ["Laborex CI", "COPHARMA", "Ubipharm", "TEDIS Pharma"]
STOCK_CATEGORIES = sorted({lot["category"] for lot in STOCK_LOTS})
RECENT_RECEPTIONS = [
    {"lot": "LOT-2027-E021", "product": "Seringue 5 ml", "supplier": "TEDIS Pharma", "qty": 480, "date": "11/11 · 08:45"},
    {"lot": "LOT-2026-K019", "product": "Artéméther-Luméfantrine", "supplier": "Ubipharm", "qty": 210, "date": "10/11 · 16:12"},
    {"lot": "LOT-2027-G015", "product": "Paracétamol sirop", "supplier": "Laborex CI", "qty": 76, "date": "10/11 · 10:04"},
]


PREPARATION = {
    "order_id": 1,
    "reference": "CMD-2026-0152",
    "bon": "BP-2026-0091",
    "client": "Pharmacie du Plateau",
    "magasinier": "M. Diabaté",
    "started": "09:10",
    "elapsed": "18 min",
    "lines_done": 3,
    "lines_total": 4,
    "units_done": 123,
    "units_total": 180,
    "progress": 75,
    "remaining": 57,
    "lots_prepared": [
        {"lot": "LOT-2026-A184", "product": "Doliprane", "expiry": "23/11/2026", "qty": 60},
        {"lot": "LOT-2026-C041", "product": "Amoxicilline", "expiry": "28/12/2026", "qty": 33},
        {"lot": "LOT-2026-K019", "product": "Artéméther/Luméfantrine", "expiry": "01/2027", "qty": 30},
    ],
    "lines": [
        {"product": "Doliprane 1000 mg", "code": "PAR-1000", "form": "Comprimé", "qty": 60, "lot": "LOT-2026-A184", "expiry": "23/11/2026", "days": "J-12", "tone": "rose", "location": "A-12", "picked": 60, "checked": True},
        {"product": "Amoxicilline 500 mg", "code": "AMX-500", "form": "Gélule", "qty": 45, "lot": "LOT-2026-C041", "expiry": "28/12/2026", "days": "J-47", "tone": "amber", "location": "B-04", "picked": 33, "checked": True},
        {"product": "Artéméther/Luméfantrine", "code": "ART-2604", "form": "Comprimé", "qty": 30, "lot": "LOT-2026-K019", "expiry": "01/2027", "days": "J-51", "tone": "green", "location": "C-02", "picked": 30, "checked": True},
        {"product": "Sérum physiologique 0,9 %", "code": "SER-2608", "form": "Flacon de 500 ml", "qty": 45, "lot": "LOT-2027-E021", "expiry": "08/2028", "days": "J-650", "tone": "green", "location": "C-02", "picked": 0, "checked": False},
    ],
    "shortage": {"product": "Amoxicilline 500 mg", "qty": 12},
}


def decorate_prep(prep):
    lines = []
    for line in prep["lines"]:
        item = {**line}
        item["tone_meta"] = TONE_META[line["tone"]]
        lines.append(item)
    return {**prep, "lines": lines}


TRACE_DATA = {
    "LOT-2026-A184": {
        "lot": {
            "lot": "LOT-2026-A184",
            "product": "Doliprane 1000 mg",
            "code": "PAR-1000",
            "supplier": "Laborex CI",
            "received": "02/08/2026",
            "expiry": "23/11/2026",
            "days": "J-12",
            "qty_received": 240,
            "qty_out": 198,
            "qty_remaining": 42,
            "clients_count": 6,
            "status": "Disponible",
        },
        "movements": [
            {"title": "Sortie de stock · −60 unités", "qty": -60, "time": "11/11 · 09:22", "detail": "Préparation CMD-2026-0152 · Pharmacie du Plateau · M. Diabaté", "type": "SORTIE", "tone": "blue", "ref": "MVT-0842"},
            {"title": "Sortie de stock · −30 unités", "qty": -30, "time": "10/11 · 15:40", "detail": "Livraison BL-2026-0181 · Pharmacie Les Palmiers · A. Yao", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0146"},
            {"title": "Sortie de stock · −48 unités", "qty": -48, "time": "09/11 · 11:18", "detail": "Livraison BL-2026-0177 · CHU de Treichville · K. Bamba", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0141"},
            {"title": "Sortie de stock · −40 unités", "qty": -40, "time": "08/11 · 16:05", "detail": "Livraison BL-2026-0172 · Clinique La Providence · S. Traoré", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0138"},
            {"title": "Ajustement d'inventaire · −2 unités", "qty": -2, "time": "07/11 · 09:12", "detail": "Motif : casse constatée lors du contrôle · Dr P. Koffi", "type": "AJUSTEMENT", "tone": "amber", "ref": "Justificatif joint"},
            {"title": "2 sorties de stock · −18 unités", "qty": -18, "time": "02–06/11", "detail": "Pharmacie Marcory (12) · Centre de santé d'Adjamé (6)", "type": "SORTIES", "tone": "blue", "ref": "CMD-0129 · CMD-0121"},
            {"title": "Entrée en stock · +240 unités", "qty": 240, "time": "02/08 · 10:04", "detail": "Réception fournisseur Laborex CI · bon BLF-2026-7420 · M. Diabaté", "type": "ENTRÉE", "tone": "green", "ref": "LOT-2026-A184"},
        ],
        "clients": [
            {"client": "Pharmacie du Plateau", "type": "Pharmacie", "city": "Plateau", "date": "11/11/2026", "qty": 60, "order": "CMD-0152", "phone": "+225 27 20 45 67 89", "email": "contact@pharmacie-plateau.ci", "notified": False},
            {"client": "Pharmacie Les Palmiers", "type": "Pharmacie", "city": "Abobo", "date": "10/11/2026", "qty": 30, "order": "CMD-0146", "phone": "+225 27 21 33 12 40", "email": "lespalmiers@pharma.ci", "notified": True},
            {"client": "CHU de Treichville", "type": "Structure de santé", "city": "Treichville", "date": "09/11/2026", "qty": 48, "order": "CMD-0141", "phone": "+225 27 22 44 90 10", "email": "pharmacie@chu-treichville.ci", "notified": False},
            {"client": "Clinique La Providence", "type": "Structure de santé", "city": "Cocody", "date": "08/11/2026", "qty": 40, "order": "CMD-0138", "phone": "+225 27 22 51 08 76", "email": "achats@laprovidence.ci", "notified": True},
            {"client": "Pharmacie Marcory", "type": "Pharmacie", "city": "Marcory", "date": "02/11/2026", "qty": 12, "order": "CMD-0129", "phone": "+225 27 21 25 78 33", "email": "marcory@pharma.ci", "notified": False},
            {"client": "Centre de santé d'Adjamé", "type": "Structure de santé", "city": "Adjamé", "date": "02/11/2026", "qty": 6, "order": "CMD-0121", "phone": "+225 27 20 37 41 22", "email": "cs.adjame@sante.ci", "notified": False},
        ],
    },
    "LOT-2026-C041": {
        "lot": {
            "lot": "LOT-2026-C041",
            "product": "Amoxicilline 500 mg",
            "code": "AMX-500",
            "supplier": "COPHARMA",
            "received": "15/09/2026",
            "expiry": "28/12/2026",
            "days": "J-47",
            "qty_received": 300,
            "qty_out": 202,
            "qty_remaining": 98,
            "clients_count": 4,
            "status": "Disponible",
        },
        "movements": [
            {"title": "Sortie de stock · −98 unités", "qty": -98, "time": "10/11 · 15:02", "detail": "Préparation CMD-2026-0151 · Pharmacie Sainte-Marie · M. Diabaté", "type": "SORTIE", "tone": "blue", "ref": "MVT-0837"},
            {"title": "Sortie de stock · −65 unités", "qty": -65, "time": "07/11 · 10:30", "detail": "Livraison BL-2026-0179 · CHU de Treichville · A. Yao", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0143"},
            {"title": "Sortie de stock · −25 unités", "qty": -25, "time": "03/11 · 14:10", "detail": "Livraison BL-2026-0171 · Pharmacie Les Palmiers · S. Traoré", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0128"},
            {"title": "Sortie de stock · −14 unités", "qty": -14, "time": "28/10 · 09:05", "detail": "Livraison BL-2026-0164 · Centre de santé d'Adjamé · S. Traoré", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0117"},
            {"title": "Entrée en stock · +300 unités", "qty": 300, "time": "15/09 · 11:20", "detail": "Réception fournisseur COPHARMA · bon BLF-2026-6914 · M. Diabaté", "type": "ENTRÉE", "tone": "green", "ref": "LOT-2026-C041"},
        ],
        "clients": [
            {"client": "Pharmacie Sainte-Marie", "type": "Pharmacie", "city": "Marcory", "date": "10/11/2026", "qty": 98, "order": "CMD-0151", "phone": "+225 27 21 25 78 33", "email": "contact@sainte-marie.ci", "notified": True},
            {"client": "CHU de Treichville", "type": "Structure de santé", "city": "Treichville", "date": "07/11/2026", "qty": 65, "order": "CMD-0143", "phone": "+225 27 22 44 90 10", "email": "pharmacie@chu-treichville.ci", "notified": True},
            {"client": "Pharmacie Les Palmiers", "type": "Pharmacie", "city": "Abobo", "date": "03/11/2026", "qty": 25, "order": "CMD-0128", "phone": "+225 27 21 33 12 40", "email": "lespalmiers@pharma.ci", "notified": False},
            {"client": "Centre de santé d'Adjamé", "type": "Structure de santé", "city": "Adjamé", "date": "28/10/2026", "qty": 14, "order": "CMD-0117", "phone": "+225 27 20 37 41 22", "email": "cs.adjame@sante.ci", "notified": False},
        ],
    },
    "LOT-2026-K019": {
        "lot": {
            "lot": "LOT-2026-K019",
            "product": "Artéméther-Luméfantrine 80/480",
            "code": "ART-8048",
            "supplier": "Ubipharm",
            "received": "10/11/2026",
            "expiry": "01/2027",
            "days": "J-51",
            "qty_received": 300,
            "qty_out": 90,
            "qty_remaining": 210,
            "clients_count": 2,
            "status": "Disponible",
        },
        "movements": [
            {"title": "Sortie de stock · −60 unités", "qty": -60, "time": "11/11 · 07:55", "detail": "Préparation CMD-2026-0154 · Pharmacie Les Palmiers · M. Diabaté", "type": "SORTIE", "tone": "blue", "ref": "MVT-0841"},
            {"title": "Sortie de stock · −30 unités", "qty": -30, "time": "10/11 · 18:20", "detail": "Livraison BL-2026-0183 · CHU de Treichville · S. Traoré", "type": "SORTIE", "tone": "blue", "ref": "CMD-2026-0153"},
            {"title": "Entrée en stock · +300 unités", "qty": 300, "time": "10/11 · 16:12", "detail": "Réception fournisseur Ubipharm · bon BLF-2026-7481 · M. Diabaté", "type": "ENTRÉE", "tone": "green", "ref": "LOT-2026-K019"},
        ],
        "clients": [
            {"client": "Pharmacie Les Palmiers", "type": "Pharmacie", "city": "Abobo", "date": "11/11/2026", "qty": 60, "order": "CMD-0154", "phone": "+225 27 21 33 12 40", "email": "lespalmiers@pharma.ci", "notified": False},
            {"client": "CHU de Treichville", "type": "Structure de santé", "city": "Treichville", "date": "10/11/2026", "qty": 30, "order": "CMD-0153", "phone": "+225 27 22 44 90 10", "email": "pharmacie@chu-treichville.ci", "notified": True},
        ],
    },
    "LOT-2027-E021": {
        "lot": {
            "lot": "LOT-2027-E021",
            "product": "Seringue 5 ml",
            "code": "SER-005",
            "supplier": "TEDIS Pharma",
            "received": "11/11/2026",
            "expiry": "08/2028",
            "days": "J-650",
            "qty_received": 480,
            "qty_out": 0,
            "qty_remaining": 480,
            "clients_count": 0,
            "status": "Disponible",
        },
        "movements": [
            {"title": "Entrée en stock · +480 unités", "qty": 480, "time": "11/11 · 08:45", "detail": "Réception fournisseur TEDIS Pharma · bon BLF-2026-7498 · M. Diabaté", "type": "ENTRÉE", "tone": "green", "ref": "LOT-2027-E021"},
        ],
        "clients": [],
    },
}

TRACE_LOT = TRACE_DATA["LOT-2026-A184"]["lot"]
TRACE_CLIENTS = TRACE_DATA["LOT-2026-A184"]["clients"]


def decorate_movement(movement):
    item = {**movement}
    item["tone_meta"] = TONE_META[movement["tone"]]
    return item


for _trace in TRACE_DATA.values():
    _trace["movements"] = [decorate_movement(item) for item in _trace["movements"]]
    for _client in _trace["clients"]:
        _client["initials"] = _initials(_client["client"])

TRACE_MOVEMENTS = TRACE_DATA["LOT-2026-A184"]["movements"]


def trace_for_query(query=""):
    query = (query or "").strip()
    default = TRACE_DATA["LOT-2026-A184"]
    if not query:
        return {**default, "found": True, "query": default["lot"]["lot"]}
    needle = query.lower()
    for dataset in TRACE_DATA.values():
        lot = dataset["lot"]
        parts = [lot["lot"], lot["product"], lot["code"], lot["supplier"]]
        parts += [f"{client['client']} {client['city']} {client['order']}" for client in dataset["clients"]]
        if needle in " ".join(parts).lower():
            return {**dataset, "found": True, "query": lot["lot"]}
    return {**default, "found": False, "query": query}

RAPPEL = {
    "lot": TRACE_LOT,
    "clients": TRACE_CLIENTS,
    "notified": sum(1 for client in TRACE_CLIENTS if client["notified"]),
    "total": len(TRACE_CLIENTS),
    "units_delivered": sum(client["qty"] for client in TRACE_CLIENTS),
    "progress": round(sum(1 for client in TRACE_CLIENTS if client["notified"]) / len(TRACE_CLIENTS) * 100),
    "message": (
        "Bonjour,\n\n"
        "DPCI vous informe du rappel du lot LOT-2026-A184 (Doliprane 1000 mg, "
        "péremption 23/11/2026). Merci de suspendre la délivrance des unités issues "
        "de ce lot et de nous contacter au +225 27 20 00 00 00.\n\n"
        "Cordialement,\nLe pharmacien responsable"
    ),
}


REFERENCE_PRODUCTS = [
    {"code": "PAR-1000", "name": "Doliprane 1000 mg", "form": "Comprimé · 1000 mg", "category": "Antalgique", "threshold": 100, "stock": 240, "price": 1850, "status": "ok", "supplier": "Laborex CI", "location": "A-12", "barcode": "3400930001234", "vat": "0 %", "delay": "3 jours"},
    {"code": "AMO-500", "name": "Amoxicilline 500 mg", "form": "Gélule · 500 mg", "category": "Antibiotique", "threshold": 50, "stock": 18, "price": 3200, "status": "low", "supplier": "COPHARMA", "location": "B-04", "barcode": "3400930001241", "vat": "0 %", "delay": "3 jours"},
    {"code": "OME-020", "name": "Oméprazole 20 mg", "form": "Gélule · 20 mg", "category": "Gastro-entérologie", "threshold": 80, "stock": 540, "price": 2750, "status": "ok", "supplier": "Ubipharm", "location": "A-07", "barcode": "3400930001258", "vat": "0 %", "delay": "5 jours"},
    {"code": "ART-020", "name": "Artéméther/Luméfantrine", "form": "Comprimé · 20/120 mg", "category": "Antipaludique", "threshold": 60, "stock": 0, "price": 4900, "status": "critical", "supplier": "Ubipharm", "location": "C-02", "barcode": "3400930001265", "vat": "0 %", "delay": "4 jours"},
    {"code": "PAR-500", "name": "Paracétamol 500 mg", "form": "Comprimé · 500 mg", "category": "Antalgique", "threshold": 150, "stock": 1020, "price": 950, "status": "ok", "supplier": "Laborex CI", "location": "A-09", "barcode": "3400930001272", "vat": "0 %", "delay": "3 jours"},
    {"code": "IBU-400", "name": "Ibuprofène 400 mg", "form": "Comprimé · 400 mg", "category": "Anti-inflammatoire", "threshold": 90, "stock": 75, "price": 1500, "status": "low", "supplier": "COPHARMA", "location": "B-11", "barcode": "3400930001289", "vat": "0 %", "delay": "4 jours"},
    {"code": "CIP-500", "name": "Ciprofloxacine 500 mg", "form": "Comprimé · 500 mg", "category": "Antibiotique", "threshold": 40, "stock": 160, "price": 2400, "status": "ok", "supplier": "TEDIS Pharma", "location": "B-07", "barcode": "3400930001296", "vat": "0 %", "delay": "2 jours"},
    {"code": "SER-09", "name": "Sérum physiologique 0,9%", "form": "Ampoule · 10 ml", "category": "Solution", "threshold": 200, "stock": 88, "price": 450, "status": "low", "supplier": "TEDIS Pharma", "location": "C-02", "barcode": "3400930001302", "vat": "0 %", "delay": "5 jours"},
]

PRODUCT_STATUS_META = {
    "ok": {"label": "En stock", "tone": "green"},
    "low": {"label": "Sous seuil", "tone": "amber"},
    "critical": {"label": "Rupture", "tone": "rose"},
}

for _product in REFERENCE_PRODUCTS:
    _product["status_label"] = PRODUCT_STATUS_META[_product["status"]]["label"]
    _product["status_tone"] = TONE_META[PRODUCT_STATUS_META[_product["status"]]["tone"]]

REFERENCE_SUPPLIERS = [
    {"name": "Laborex CI", "code": "FOU-001", "contact": "Mariam Ouattara", "phone": "+225 27 21 75 00 00", "products": 412, "delay": "3 jours", "status": "Actif"},
    {"name": "COPHARMA", "code": "FOU-002", "contact": "Jean-Marc Kouadio", "phone": "+225 27 22 40 18 20", "products": 286, "delay": "4 jours", "status": "Actif"},
    {"name": "Ubipharm", "code": "FOU-003", "contact": "Fatou Diallo", "phone": "+225 27 20 31 44 08", "products": 328, "delay": "5 jours", "status": "Actif"},
    {"name": "TEDIS Pharma", "code": "FOU-004", "contact": "Serge N'Guessan", "phone": "+225 27 23 45 90 12", "products": 222, "delay": "2 jours", "status": "Actif"},
]

REFERENCE_CLIENTS = [
    {"name": "Pharmacie du Plateau", "type": "Pharmacie", "city": "Plateau", "orders": 14, "status": "Actif"},
    {"name": "CHU de Treichville", "type": "Structure de santé", "city": "Treichville", "orders": 28, "status": "Actif"},
    {"name": "Clinique La Providence", "type": "Structure de santé", "city": "Cocody", "orders": 9, "status": "Actif"},
    {"name": "Pharmacie Sainte-Marie", "type": "Pharmacie", "city": "Marcory", "orders": 7, "status": "À valider"},
    {"name": "Pharmacie Les Palmiers", "type": "Pharmacie", "city": "Abobo", "orders": 11, "status": "Actif"},
]

REFERENCE_CATEGORIES = [
    {"name": "Antalgique", "products": 184, "share": 92, "tone": "teal"},
    {"name": "Antibiotique", "products": 231, "share": 78, "tone": "blue"},
    {"name": "Antipaludique", "products": 96, "share": 48, "tone": "violet"},
    {"name": "Gastro-entérologie", "products": 142, "share": 66, "tone": "amber"},
    {"name": "Consommable", "products": 310, "share": 84, "tone": "green"},
]

REFERENCE_STATS = {
    "products": 1248,
    "low": 7,
    "suppliers": 24,
    "clients": 186,
    "categories": 18,
}

ADMIN_USERS = [
    {"name": "Awa Konan", "email": "a.konan@dpci.ci", "role": "Responsable commerciale", "last": "Aujourd'hui · 08:12", "location": "Abidjan", "ip": "192.168.1.24", "active": True, "initials": "AK", "tone": "teal"},
    {"name": "Dr Patrick Koffi", "email": "p.koffi@dpci.ci", "role": "Pharmacien responsable", "last": "Aujourd'hui · 07:45", "location": "Abidjan", "ip": "192.168.1.18", "active": True, "initials": "PK", "tone": "violet"},
    {"name": "Moussa Diabaté", "email": "m.diabate@dpci.ci", "role": "Responsable magasin", "last": "Aujourd'hui · 06:58", "location": "Entrepôt", "ip": "192.168.1.31", "active": True, "initials": "MD", "tone": "blue"},
    {"name": "Awa Yao", "email": "a.yao@dpci.ci", "role": "Préparatrice", "last": "Hier · 17:20", "location": "Entrepôt", "ip": "192.168.1.44", "active": True, "initials": "AY", "tone": "amber"},
    {"name": "Serge Traoré", "email": "s.traore@dpci.ci", "role": "Livreur", "last": "Hier · 16:05", "location": "Mobile", "ip": "102.176.4.88", "active": True, "initials": "ST", "tone": "blue"},
    {"name": "Koffi Bamba", "email": "k.bamba@dpci.ci", "role": "Livreur", "last": "26/10/2026 · 08:30", "location": "Mobile", "ip": "102.176.4.91", "active": False, "initials": "KB", "tone": "slate"},
]

ADMIN_ROLES = [
    {"name": "Pharmacien responsable", "detail": "Tous droits · rappels et validations", "count": 1, "icon": "shield", "tone": "violet"},
    {"name": "Responsable commerciale", "detail": "Commandes, clients, tarifs", "count": 2, "icon": "wallet", "tone": "teal"},
    {"name": "Responsable magasin", "detail": "Réception, stock, lots, inventaire", "count": 3, "icon": "box", "tone": "blue"},
    {"name": "Préparatrice", "detail": "Préparation FEFO et contrôle", "count": 2, "icon": "clipboard", "tone": "amber"},
    {"name": "Livreur", "detail": "Livraisons, retours, bons signés", "count": 3, "icon": "truck", "tone": "slate"},
]

AUDIT_LOG = [
    {"title": "Commande CMD-2026-0152 validée", "time": "09:42", "detail": "Awa Konan · Responsable commerciale", "tone": "teal"},
    {"title": "Préparation FEFO terminée", "time": "09:22", "detail": "Moussa Diabaté · Responsable magasin", "tone": "blue"},
    {"title": "Rappel du lot LOT-2026-A184", "time": "08:15", "detail": "Dr Patrick Koffi · Pharmacien responsable", "tone": "rose"},
    {"title": "Connexion réussie · 2FA", "time": "07:45", "detail": "Dr Patrick Koffi · 192.168.1.18", "tone": "slate"},
]

ADMIN_STATS = [
    {"label": "Utilisateurs actifs", "value": "11", "detail": "/ 12 comptes", "icon": "users", "tone": "teal"},
    {"label": "Rôles", "value": "5", "detail": "profils", "icon": "shield", "tone": "violet"},
    {"label": "Actions aujourd'hui", "value": "248", "detail": "journalisées", "icon": "activity", "tone": "blue"},
    {"label": "Sessions ouvertes", "value": "4", "detail": "postes connectés", "icon": "lock", "tone": "amber"},
]

NEW_ORDER_LINES = [
    {"product": "Doliprane 1000 mg", "code": "PAR-1000", "form": "Comprimé", "qty": 60, "stock": 240, "price": 3500, "status": "ok"},
    {"product": "Amoxicilline 500 mg", "code": "AMX-500", "form": "Gélule", "qty": 120, "stock": 98, "price": 2800, "status": "partial"},
    {"product": "Oméprazole 20 mg", "code": "OMP-20", "form": "Gélule", "qty": 40, "stock": 152, "price": 4200, "status": "ok"},
]

for _line in NEW_ORDER_LINES:
    _line["total"] = _line["qty"] * _line["price"]

NEW_ORDER = {
    "client": "Pharmacie du Plateau",
    "client_code": "PH-0012",
    "client_type": "Pharmacie",
    "city": "Plateau, Abidjan",
    "phone": "+225 27 20 45 67 89",
    "orders_count": 14,
    "date": "11/11/2026",
    "lines": NEW_ORDER_LINES,
    "lines_count": len(NEW_ORDER_LINES),
    "units": sum(line["qty"] for line in NEW_ORDER_LINES),
    "subtotal": sum(line["total"] for line in NEW_ORDER_LINES),
    "discount": 0,
    "vat": 0,
}

NEW_ORDER["total"] = NEW_ORDER["subtotal"] - NEW_ORDER["discount"] + NEW_ORDER["vat"]


def commande_page_context(order_id):
    order = get_order(order_id)
    if not order:
        return None
    lines = []
    for index, product in enumerate(order["products"]):
        served = product["qty"] if index < 3 else 0
        lines.append(
            {
                **product,
                "served": served,
                "status": "Prélevé" if index < 3 else "À prélever",
                "tone": "green" if index < 3 else "slate",
                "tone_meta": TONE_META["green" if index < 3 else "slate"],
                "total": product["qty"] * product["price"],
                "shortage": max(0, product["qty"] - served),
            }
        )
    status_index = {
        "attente": 0,
        "preparation": 1,
        "prete": 2,
        "expediee": 3,
        "livree": 4,
    }.get(order["status"], -1)
    steps = [
        {"label": label, "done": index < status_index, "current": index == status_index}
        for index, label in enumerate(["En attente", "En préparation", "Prête", "Expédiée", "Livrée"])
    ]
    return {
        "order": order,
        "lines": lines,
        "served": sum(line["served"] for line in lines),
        "total_units": order["units"],
        "steps": steps,
        "docs": [
            {"title": f"Bon de préparation BP-2026-009{order['id']}", "detail": f"Généré le {order['date']} à {order['time']}", "ready": True},
            {"title": "Bon de livraison", "detail": "À générer après confirmation", "ready": False},
        ],
    }
