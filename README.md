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

Koronavirusla bağlı məqalələr

`GET https://covid-az.herokuapp.com/api/articles`

```json
[
  [
    "COVID-19 nədir ?", 
    "<p>Koronaviruslar (CoV), adi soyuqdəymə əlamətlərindən Yaxın Şərq Respirator Sindromu ( Middle East Respiratory Syndrome Coronavirus – MERS – CoV) və Şiddətli Kəskin Respirator Sindrom (SARS – CoV) kimi daha ciddi patologiyalara qədər çeşidli xəstəliklərə\n    səbəb olan böyük bir virus fəsiləsidir.\n</p>\n\n<p>\n    Koronaviruslar zoonoz infeksiya kimi heyvanlardan yoluxaraq insanlarda xəstəlik törədə bilir. Ətraflı araşdırmalar nəticəsində, SARS-CoV-un müşk pişiklərindən, MERS-CoV-un isə tək hürgüclü dəvələrdən insanlara yoluxduğu məlum olmuşdur. Hazırda insanlara\n    yoluxmayan, ancaq heyvanlarda rast gəlinən bir çox koronavirus tipi mövcuddur.\n</p>\n\n<p>\n    31 dekabr 2019-cu ildə Ümumdünya Səhiyyə Təşkilatı (ÜST) Çin Ölkə Ofisi Çinin Hubei əyalətinin Wuhan şəhərində etiologiyası naməlum olan pnevmoniya ilə xəstələnmə halları haqqında məlumat vermişdir. 7 Yanvar 2020-ci ildə isə bu fakt daha əvvəllər insanlarda\n    rast gəlinməmiş yeni bir koronavirus (2019 Novel Coronavirus COVID-19) olaraq təsdiqlənmişdir.</p>"
  ],
  [
    "Virusun yayılması", 
    "2019‑nCoV xəstəliyinə yoluxmuş insan asanlıqla bu xəstəliyi başqasına yoluxdura bilər. COVID‑19 virusuna yoluxmuş şəxsin asqırması və ya öskürməsi zamanı ağız və burun boşluğundan havaya buraxılan kiçik damcılar vasitəsilə virus yayılaraq digər insanlara\nkeçə bilər. Bu damcının başqasının nəfəs yoluna düşməsi nəticəsində baş verir. Eyni zamanda bu damcılar ətrafda yerləşən əşyalara və səthlərə düşür. İnsanlar həmin əşyalara və ya səthlərə toxunduqdan sonra gözə, burun və ya ağıza toxunaraq virusa yoluxa\nbilərlər. Bu səbəbdən xəstələnmiş şəxslə 1 metrdən artıq məsafə saxlamaq və üz nahiyəsinə toxunmazdan əvvəl əlləri yumaq çox vacibdir."
  ]
]
```

Koronavirusla əlaqəli Azərbaycan Respublikası Nazirlər Kabinetinin xəbərləri

`GET https://covid-az.herokuapp.com/api/news`

```json
[
  {
    "body": "<div><p style=\"text-align: justify;\">Azərbaycan Respublikasında 9 yeni koronavirus infeksiyasına yoluxma faktı qeydə alınmışdır. Xüsusi rejimli xəstəxanalara yerləşdirilən və müşahidə altında olan pasiyentlər özlərini normal hiss edirlər, səhhətləri stabildir.</p>\n<p style=\"text-align: justify;\">Hazırda Azərbaycanda 42 nəfər aktiv koronavirus xəstəsi xüsusi rejimli müəssisələrdə həkim nəzarəti altında saxlanılır, onların müalicəsi ilə bağlı müvafiq tədbirlər davam etdirilir.</p>\n<p style=\"text-align: justify;\">Bir daha vətəndaşlarımızı şəxsi gigiyena qaydalarına, Ümumdünya Səhiyyə Təşkilatının, Nazirlər Kabineti yanında Operativ Qərargahın tələb və tövsiyələrinə ciddi riayət etməyə çağırırıq.</p>\n<p style=\"text-align: justify;\">Vətəndaşlardan özünütəcrid tədbirlərinə uyğun davranmaq, yalnız ciddi ehtiyac yarandıqda evdən çıxmaq, digər şəxslərlə minimum kontaktda olmaq, insanların sıx toplaşdığı yerlərə getməmək və digər qaydalara əməl etmək tələb olunur.</p></div>", 
    "title": "Azərbaycan Respublikası Nazirlər Kabinetinin  yanında Operativ Qərargahın  MƏLUMATI "
  }, 
  {
    "body": "<div><p style=\"text-align: justify;\">Martın 21-də Nazirlər Kabinetində operativ qərargahın növbəti iclası keçirilib.</p>\n<p style=\"text-align: justify;\">İclasda koronavirus infeksiyasının yayılmasının qarşısının alınması ilə bağlı hazırkı vəziyyət təhlil olunub, səhiyyə sahəsində görülməli işlər, tətbiq olunmuş məhdudiyyətlərin ilkin nəticələri və digər məsələlər müzakirə edilib, həyata keçiriləcək vəzifələrə dair tapşırıqlar verilib.</p></div>", 
    "title": "Nazirlər Kabineti yanında operativ qərargahın iclasında epidemiya (Covid-19) ilə mübarizənin hazırkı vəziyyəti müzakirə olunub "
  }
]
```
