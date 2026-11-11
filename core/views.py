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

    context = {
        "user": user,
        "active_nav": "dashboard",
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
    }
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

    context = {
        "user": user,
        "active_nav": "commandes",
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
    }

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
