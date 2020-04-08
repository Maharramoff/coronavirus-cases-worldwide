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
    "body": "<div><p style=\"text-align: justify;\">Azərbaycan Respublikasında 105 yeni koronavirus (COVID-19) infeksiyasına yoluxma faktı qeydə alınmış, həmin şəxslər xüsusi rejimli xəstəxanalara yerləşdirilmişdir.</p>\n<p style=\"text-align: justify;\">Eyni zamanda, koronavirus infeksiyasına yoluxmuş 19 nəfər müalicə olunaraq sağalmış və evə buraxılmışdır.</p>\n<p style=\"text-align: justify;\">Hazırkı dövrədək ölkəmizdə 822 nəfərin koronavirus infeksiyasına yoluxması faktı müəyyən edilmiş, onlardan 63 nəfəri müalicə olunaraq sağalmış, 8 nəfər vəfat etmiş, 751 nəfərin xüsusi rejimli xəstəxanalarda müalicəsi davam etdirilir. Həmin şəxslərdən 33 nəfərin vəziyyəti ağır, 47 nəfərin vəziyyəti orta ağır qiymətləndirilir, digərlərinin səhhəti stabildir.</p>\n<p> </p></div>", 
    "datetime": "08 Aprel 2020 - 19:20", 
    "id": "796", 
    "title": "Azərbaycan Respublikası Nazirlər Kabineti yanında Operativ Qərargahın məlumatı "
  }, 
  {
    "body": "<div><p style=\"text-align: justify;\">Azərbaycan Respublikasında 76 yeni koronavirus (COVID-19) infeksiyasına yoluxma faktı qeydə alınmış, bir nəfər vəfat etmişdir.</p>\n<p style=\"text-align: justify;\">Koronavirus (COVID-19) üçün götürülən analiz nümunələri müsbət çıxmış 1953-cü il təvəllüdlü, şəkərli diabet xəstəsi olan vətəndaşın səhhətinin stabilləşdirilməsi ilə bağlı aparılan reanimasiya tədbirləri nəticə verməmişdir. Onun ailə üzvləri və ünsiyyətdə olduğu digər şəxslər müəyyən edilir və karantinə götürülür.</p>\n<p style=\"text-align: justify;\">Hazırkı dövrədək ölkəmizdə 717 nəfərin koronavirus infeksiyasına yoluxması faktı müəyyən edilmiş, onlardan 44 nəfəri müalicə olunaraq sağalmış, 8 nəfər vəfat etmiş, 665 nəfərin xüsusi rejimli xəstəxanalarda müalicəsi davam etdirilir. Həmin şəxslərdən 23 nəfərin vəziyyəti ağır, 31 nəfərin vəziyyəti orta ağır qiymətləndirilir, digərlərinin səhhəti stabildir.</p>\n<p style=\"text-align: justify;\">Ötən müddət ərzində yeni yoluxma hallarının müəyyənləşdirilməsi ilə əlaqədar 53 300 test aparılmışdır.</p></div>", 
    "datetime": "07 Aprel 2020 - 15:50", 
    "id": "795", 
    "title": "Azərbaycan Respublikası Nazirlər Kabineti yanında Operativ Qərargahın məlumatı "
  }
]
```
