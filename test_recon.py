import pandas as pd
from recon_engine import reconcile_books


def test_missing_vendor_feed():
  internal = pd.DataFrame(
      {'Trade_ID': ['T1'], 'Notional_Int': [1000000], 'Valuation_Int': [995000]}
  )
  vendor = pd.DataFrame(columns=['Trade_ID', 'Notional_Vend', 'Valuation_Vend'])

  result = reconcile_books(internal, vendor)
  assert 'Missing_Vendor_Feed' in result['Error_Categories'].values


def test_valuation_discrepancy():
  internal = pd.DataFrame(
      {'Trade_ID': ['T2'], 'Notional_Int': [5000000], 'Valuation_Int': [4980000]}
  )
  vendor = pd.DataFrame({
      'Trade_ID': ['T2'],
      'Notional_Vend': [5000000],
      'Valuation_Vend': [4975000],
  })

  result = reconcile_books(internal, vendor)
  assert 'Valuation_Discrepancy' in result['Error_Categories'].values