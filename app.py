"""Run with: python -m streamlit run app.py"""

from decimal import Decimal, ROUND_HALF_UP

import streamlit as st


def calculate_commission(sales: Decimal) -> tuple[Decimal, Decimal]:
    """Return commission for the first $50,000 and the excess sales."""
    if not sales.is_finite() or sales < 0:
        raise ValueError("Sales must be a finite, nonnegative amount.")
    base = min(sales, Decimal("50000")) * Decimal("0.10")
    excess = max(sales - Decimal("50000"), Decimal("0")) * Decimal("0.15")
    return base, excess


def main() -> None:
    st.set_page_config(page_title="Sales Commission Calculator", page_icon="💰")
    st.title("Sales Commission Calculator")
    st.write("Earn 10% on the first $50,000 in sales, plus 15% on sales above $50,000.")

    amount = st.number_input(
        "Total sales ($)", min_value=0.0, value=0.0, step=100.0, format="%.2f"
    )
    sales = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    base, excess = calculate_commission(sales)
    total = (base + excess).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    st.metric("Total commission", f"${total:,.2f}")
    st.subheader("Commission breakdown")
    st.write(f"First $50,000 at 10%: **${base:,.2f}**")
    st.write(f"Sales above $50,000 at 15%: **${excess:,.2f}**")
    st.caption("Example: $60,000 in sales earns $5,000 + $1,500 = $6,500.")


if __name__ == "__main__":
    main()
