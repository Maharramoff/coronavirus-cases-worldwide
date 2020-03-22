**COVID API**

COVID-19 virusu ilə bağlı real zaman ərzində məlumatın əldə olunması üçün API

Məlumatlar 5 dəqiqə intervalla yenilənir.

Sorğu nümunələri:

Ölkələr üzrə məlumat

`GET https://covid-az.herokuapp.com/api/`

```json
[
    {
        "country": "China", 
        "new_cases": "+46", 
        "new_deaths": "+6", 
        "total_cases": "81,054", 
        "total_deaths": "3,261", 
        "total_recovered": "72,440"
    }, 
    {
        "country": "Italy", 
        "new_cases": "+5,560", 
        "new_deaths": "+651", 
        "total_cases": "59,138", 
        "total_deaths": "5,476", 
        "total_recovered": "7,024"
    }, 
    {
        "country": "USA", 
        "new_cases": "+8,149", 
        "new_deaths": "+112", 
        "total_cases": "32,356", 
        "total_deaths": "414", 
        "total_recovered": "178"
    }
]
```

Qlobal statistika

`GET https://covid-az.herokuapp.com/api/stats`

```json
{
    "active_cases": "222,341", 
    "critical_cases": "10,620", 
    "new_cases": "29,524", 
    "new_deaths": "1,592", 
    "per_mln": "42.9", 
    "total_cases": "334,514", 
    "total_deaths": "14,599", 
    "total_recovered": "97,574"
}
```
