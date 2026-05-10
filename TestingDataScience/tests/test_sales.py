from hypothesis import given
from hypothesis.strategies import composite, from_regex, integers, lists

from Ch03.sales import Sale, sku_sales


@composite
def sales(draw):
    # draw - is generator witch is providing by composite decorator
    sku = draw(from_regex(r'[A-F0-9]{8}', fullmatch=True))
    amout = draw(integers(min_value=1, max_value=10_000))
    return Sale(sku, amout)  # create instance of Sale


@given(lists(elements=sales()))
def test_sku_sales(sales):
    # given provides a generator from sales function
    by_sku = sku_sales(sales)
    unknown = set(by_sku) - set(sale.sku for sale in sales)
    assert not unknown