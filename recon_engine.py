import pandas as pd


def reconcile_books(
    internal_df: pd.DataFrame, vendor_df: pd.DataFrame
) -> pd.DataFrame:
  merged = pd.merge(
      internal_df,
      vendor_df,
      on='Trade_ID',
      suffixes=('_Int', '_Vend'),
      how='outer',
  )
  discrepancies = []

  for idx, row in merged.iterrows():
    trade_id = row['Trade_ID']
    errors = []

    if pd.isna(row.get('Notional_Int')):
      errors.append('Missing_Internal_Feed')
    elif pd.isna(row.get('Notional_Vend')):
      errors.append('Missing_Vendor_Feed')
    else:
      val_diff = abs(row['Valuation_Int'] - row['Valuation_Vend'])
      if val_diff > 1.0:
        errors.append('Valuation_Discrepancy')
      if row['Notional_Int'] != row['Notional_Vend']:
        errors.append('Notional_Mismatch')

    if errors:
      discrepancies.append(
          {'Trade_ID': trade_id, 'Error_Categories': ', '.join(errors)}
      )

  return pd.DataFrame(discrepancies)