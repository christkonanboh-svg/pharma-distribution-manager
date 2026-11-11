from datetime import date
from functools import wraps

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from . import data

MONTHS = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
]

WEEKDAYS = [
    "lundi",
    "mardi",
    "mercredi",
    "jeudi",
    "vendredi",
    "samedi",
    "dimanche",
]


def current_user(request):
    return request.session.get("demo_user")


def demo_login_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not current_user(request):
            login_url = reverse("login")
            return redirect(f"{login_url}?next={request.path}")
        return view(request, *args, **kwargs)

    return wrapper


def base_context(request, active_nav, nav_title, nav_subtitle, **extra):
    return {
        "user": current_user(request),
        "active_nav": active_nav,
        "nav_title": nav_title,
        "nav_subtitle": nav_subtitle,
        **extra,
    }


def root_view(request):
    if current_user(request):
        return redirect("dashboard")
    return redirect("login")


def login_view(request):
    if current_user(request):
        return redirect("dashboard")

    next_url = request.POST.get("next") or request.GET.get("next") or ""
    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip().lower()
        password = request.POST.get("password", "")
        account = data.DEMO_ACCOUNTS.get(username)

        if account and account["password"] == password:
            request.session["demo_user"] = {
                "username": username,
                "name": account["name"],
                "role": account["role"],
                "initials": account["initials"],
                "email": account["email"],
            }
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect("dashboard")

        error = "Identifiant ou mot de passe incorrect. Utilisez un compte de démonstration."

    accounts = [
        {
            "username": username,
            "name": account["name"],
            "role": account["role"],
            "initials": account["initials"],
        }
        for username, account in data.DEMO_ACCOUNTS.items()
    ]

    return render(
        request,
        "pages/login.html",
        {
            "accounts": accounts,
            "demo_password": "demo1234",
            "error": error,
            "next": next_url,
            "logged_out": request.GET.get("deconnecte") == "1",
        },
    )


def logout_view(request):
    request.session.flush()
    return redirect(f"{reverse('login')}?deconnecte=1")


@demo_login_required
def dashboard_view(request):
    user = current_user(request)
    today = date.today()
    date_label = (
        f"{WEEKDAYS[today.weekday()].capitalize()} "
        f"{today.day} {MONTHS[today.month - 1]} {today.year}"
    )
    hour = 9
    greeting = "Bonjour" if hour < 18 else "Bonsoir"
    orders = data.all_orders()

    context = base_context(
        request,
        "dashboard",
        "Tableau de bord",
        "Vue d'ensemble des opérations",
    )
    context.update({
        "date_label": date_label,
        "greeting": greeting,
        "kpis": data.KPIS,
        "revenue_chart": data.REVENUE_CHART,
        "pipeline": data.PIPELINE,
        "stock_alerts": data.STOCK_ALERTS,
        "top_products": data.TOP_PRODUCTS,
        "activity": data.ACTIVITY,
        "recent_orders": orders[:5],
        "status_counts": data.status_counts(),
        "total_orders": len(orders),
    })
    return render(request, "pages/dashboard.html", context)


@demo_login_required
def commandes_view(request):
    user = current_user(request)
    query = request.GET.get("q", "")
    status = request.GET.get("status", "")
    client = request.GET.get("client", "")

    if status not in data.STATUS_META:
        status = ""

    orders = data.filter_orders(query=query, status=status, client=client)
    total_amount = sum(order["amount"] for order in orders)
    counts = data.status_counts()
    all_count = len(data.ORDERS)
    status_tab_items = [
        {
            "value": value,
            "label": label,
            "count": all_count if value == "" else counts[value],
        }
        for value, label in data.STATUS_TABS
    ]

    context = base_context(
        request,
        "commandes",
        "Commandes",
        "Gestion des commandes",
    )
    context.update({
        "orders": orders,
        "total_amount": total_amount,
        "total_orders": len(orders),
        "query": query,
        "active_status": status,
        "active_client": client,
        "status_tabs": status_tab_items,
        "status_counts": counts,
        "all_count": all_count,
        "clients": data.clients(),
        "urgent_count": sum(1 for order in orders if order["priority"] == "Haute"),
        "awaiting_count": counts["attente"],
    })

    if request.headers.get("HX-Request") == "true":
        return render(request, "partials/commandes_table.html", context)

    return render(request, "pages/commandes.html", context)


@demo_login_required
def commande_detail_view(request, pk):
    order = data.get_order(pk)
    if not order:
        return HttpResponse(
            '<div class="p-8 text-center text-sm text-slate-500">Commande introuvable.</div>',
            status=404,
        )
    return render(request, "partials/commande_detail.html", {"order": order})


@demo_login_required
def alertes_view(request):
    category = request.GET.get("category", "")
    query = request.GET.get("q", "")
    if category not in dict(data.ALERT_CATEGORIES):
        category = ""

    alerts = data.filter_alerts(category=category, query=query)
    counts = data.alert_counts()
    tabs = [
        {"value": value, "label": label, "count": counts[value]}
        for value, label in data.ALERT_CATEGORIES
    ]

    total = len(data.ALERTS)
    critical = sum(1 for alert in data.ALERTS if alert["tone"] == "rose")
    to_process = sum(1 for alert in data.ALERTS if alert["tone"] == "amber")
    follow = sum(1 for alert in data.ALERTS if alert["tone"] == "blue")
    info = total - critical - to_process - follow
    p1 = round(critical / total * 100)
    p2 = round((critical + to_process) / total * 100)
    p3 = round((critical + to_process + follow) / total * 100)
    donut_style = (
        "background: conic-gradient(#e11d48 0 "
        f"{p1}%, #f59e0b {p1}% {p2}%, #0284c7 {p2}% {p3}%, #94a3b8 {p3}% 100%)"
    )

    context = base_context(
        request,
        "alertes",
        "Alertes",
        "Surveillance du stock et des lots",
        alerts=alerts,
        alert_tabs=tabs,
        active_category=category,
        query=query,
        alert_rules=data.ALERT_RULES,
        unread_count=sum(1 for alert in data.ALERTS if alert["unread"]),
        total_alerts=total,
        donut_style=donut_style,
        distribution=[
            {"label": "Critiques", "value": critical, "color": "#e11d48"},
            {"label": "À traiter", "value": to_process, "color": "#f59e0b"},
            {"label": "Suivi", "value": follow, "color": "#0284c7"},
            {"label": "Information", "value": info, "color": "#94a3b8"},
        ],
        category_bars=[
            {"label": "Péremption", "value": counts["peremption"], "share": round(counts["peremption"] / total * 100), "color": "#e11d48"},
            {"label": "Stock", "value": counts["stock"], "share": round(counts["stock"] / total * 100), "color": "#f59e0b"},
            {"label": "Rappels", "value": counts["rappel"], "share": round(counts["rappel"] / total * 100), "color": "#0284c7"},
            {"label": "Système", "value": counts["systeme"], "share": round(counts["systeme"] / total * 100), "color": "#94a3b8"},
        ],
    )
    return render(request, "pages/alertes.html", context)


@demo_login_required
def preparation_view(request):
    prep = data.decorate_prep(data.PREPARATION)
    context = base_context(
        request,
        "preparation",
        "Préparation",
        "Prélèvement FEFO des commandes",
        prep=prep,
        order=data.get_order(prep["order_id"]),
        urgency="Haute",
    )
    return render(request, "pages/preparation.html", context)


@demo_login_required
def livraisons_view(request):
    status = request.GET.get("status", "")
    query = request.GET.get("q", "")
    zone = request.GET.get("zone", "")
    driver = request.GET.get("driver", "")
    if status not in data.DELIVERY_META:
        status = ""

    deliveries = data.filter_deliveries(status=status, query=query, zone=zone, driver=driver)
    counts = data.delivery_counts()
    tabs = [
        {"value": value, "label": label, "count": counts[value]}
        for value, label in data.DELIVERY_TABS
    ]
    context = base_context(
        request,
        "livraisons",
        "Livraisons",
        "Bons de livraison et tournées",
        deliveries=deliveries,
        delivery_tabs=tabs,
        delivery_counts=counts,
        active_status=status,
        query=query,
        active_zone=zone,
        active_driver=driver,
        zones=sorted({delivery["zone"] for delivery in data.DELIVERIES}),
        drivers=sorted({delivery["driver"] for delivery in data.DELIVERIES}),
        tour=data.DELIVERY_TOUR,
        last_delivery=data.LAST_DELIVERY,
        total_deliveries=len(deliveries),
    )
    return render(request, "pages/livraisons.html", context)


@demo_login_required
def stock_lots_view(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    status = request.GET.get("status", "")
    expiry = request.GET.get("expiry", "")
    if status not in data.STOCK_STATUS_META:
        status = ""

    lots = data.filter_lots(query=query, category=category, status=status, expiry=expiry)
    context = base_context(
        request,
        "stock",
        "Stock & lots",
        "Surveillance des lots et du stock",
        lots=lots,
        products=data.STOCK_PRODUCTS,
        movements=data.STOCK_MOVEMENTS,
        stats=data.STOCK_STATS,
        categories=data.STOCK_CATEGORIES,
        query=query,
        active_category=category,
        active_status=status,
        active_expiry=expiry,
        total_lots=len(lots),
        lot_count=len(data.STOCK_LOTS),
    )
    return render(request, "pages/stock_lots.html", context)


@demo_login_required
def reception_lot_view(request):
    products = data.REFERENCE_PRODUCTS
    selected_code = request.GET.get("product", products[0]["code"])
    selected = next((item for item in products if item["code"] == selected_code), products[0])
    received = 240
    after = selected["stock"] + received
    context = base_context(
        request,
        "reception",
        "Réception",
        "Entrée en stock d'un lot fournisseur",
        suppliers=data.SUPPLIERS,
        products=products,
        selected_product=selected,
        received=received,
        after=after,
        impact_value=received * selected["price"],
        recent_receptions=data.RECENT_RECEPTIONS,
        today="11/11/2026",
    )
    return render(request, "pages/reception_lot.html", context)


@demo_login_required
def tracabilite_view(request):
    trace = data.trace_for_query(request.GET.get("q", ""))
    lot = trace["lot"]
    context = base_context(
        request,
        "tracabilite",
        "Traçabilité",
        "Historique complet des lots",
        lot=lot,
        movements=trace["movements"],
        clients=trace["clients"],
        query=trace["query"],
        trace_found=trace["found"],
        units_out=lot["qty_out"],
    )
    return render(request, "pages/tracabilite.html", context)


@demo_login_required
def rappel_lot_view(request):
    context = base_context(
        request,
        "rappel",
        "Rappel de lot",
        "Procédure de retrait et notification",
        rappel=data.RAPPEL,
    )
    return render(request, "pages/rappel_lot.html", context)


@demo_login_required
def referentiels_view(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    status = request.GET.get("status", "")
    if status not in data.PRODUCT_STATUS_META:
        status = ""

    products = []
    for product in data.REFERENCE_PRODUCTS:
        if category and product["category"] != category:
            continue
        if status and product["status"] != status:
            continue
        if query and query not in f"{product['name']} {product['code']} {product['form']} {product['category']}".lower():
            continue
        products.append(product)

    selected_code = request.GET.get("product", products[0]["code"] if products else data.REFERENCE_PRODUCTS[0]["code"])
    selected = next(
        (item for item in data.REFERENCE_PRODUCTS if item["code"] == selected_code),
        products[0] if products else data.REFERENCE_PRODUCTS[0],
    )
    category_values = sorted({product["category"] for product in data.REFERENCE_PRODUCTS})

    context = base_context(
        request,
        "referentiels",
        "Référentiels",
        "Produits, clients et fournisseurs",
        products=products,
        suppliers=data.REFERENCE_SUPPLIERS,
        clients=data.REFERENCE_CLIENTS,
        categories=data.REFERENCE_CATEGORIES,
        category_values=category_values,
        stats=data.REFERENCE_STATS,
        selected=selected,
        query=query,
        active_category=category,
        active_status=status,
        total_products=len(products),
        product_statuses=[
            {"value": "", "label": "Tous les statuts"},
            {"value": "ok", "label": "En stock"},
            {"value": "low", "label": "Sous seuil"},
            {"value": "critical", "label": "Rupture"},
        ],
    )
    return render(request, "pages/referentiels.html", context)


@demo_login_required
def administration_view(request):
    query = request.GET.get("q", "").strip().lower()
    role = request.GET.get("role", "")
    users = []
    for item in data.ADMIN_USERS:
        if role and item["role"] != role:
            continue
        if query and query not in f"{item['name']} {item['email']} {item['role']}".lower():
            continue
        users.append(item)

    context = base_context(
        request,
        "admin",
        "Administration",
        "Utilisateurs, rôles et sécurité",
        users=users,
        roles=data.ADMIN_ROLES,
        role_values=sorted({item["role"] for item in data.ADMIN_USERS}),
        audit=data.AUDIT_LOG,
        stats=data.ADMIN_STATS,
        query=request.GET.get("q", ""),
        active_role=role,
        total_users=len(users),
    )
    return render(request, "pages/admin.html", context)


@demo_login_required
def commande_nouvelle_view(request):
    context = base_context(
        request,
        "commandes",
        "Commandes",
        "Nouvelle commande client",
        draft=data.NEW_ORDER,
        clients=data.clients(),
        products=data.REFERENCE_PRODUCTS,
        today=data.NEW_ORDER["date"],
    )
    return render(request, "pages/commande_nouvelle.html", context)


@demo_login_required
def commande_page_view(request, pk):
    detail = data.commande_page_context(pk)
    if not detail:
        return HttpResponse(
            '<div class="p-8 text-center text-sm text-slate-500">Commande introuvable.</div>',
            status=404,
        )
    context = base_context(
        request,
        "commandes",
        "Commandes",
        "Détail de la commande",
        **detail,
    )
    return render(request, "pages/commande_detail.html", context)
