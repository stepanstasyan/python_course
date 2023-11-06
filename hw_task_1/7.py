def month_counter(some_years, some_months):
    months = some_years * 12
    result_months = months + some_months
    days = result_months * 29
    print(days)


month_counter(2, 5)


