from my_functions import calc_total
from my_functions import get_totals
def get_total(orders):
  # Tu código aquí 👇
  return calc_total(get_totals(orders))

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)