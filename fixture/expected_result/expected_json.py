class ExpectedJson:
    @staticmethod
    def expected_json_payload():
        return [{"name": {"common": "Sweden", "official": "Kingdom of Sweden",
                          "nativeName": {"swe": {"official": "Konungariket Sverige", "common": "Sverige"}}},
                 "tld": [".se"], "cca2": "SE", "ccn3": "752", "cca3": "SWE", "cioc": "SWE", "independent": True,
                 "status": "officially-assigned", "unMember": True,
                 "currencies": {"SEK": {"name": "Swedish krona", "symbol": "kr"}},
                 "idd": {"root": "+4", "suffixes": ["6"]}, "capital": ["Stockholm"],
                 "altSpellings": ["SE", "Kingdom of Sweden", "Konungariket Sverige"], "region": "Europe",
                 "subregion": "Northern Europe", "languages": {"swe": "Swedish"},
                 "translations": {"ara": {"official": "مملكة السويد", "common": "السويد"},
                                  "bre": {"official": "Rouantelezh Sveden", "common": "Sveden"},
                                  "ces": {"official": "Švédské království", "common": "Švédsko"},
                                  "cym": {"official": "Kingdom of Sweden", "common": "Sweden"},
                                  "deu": {"official": "Königreich Schweden", "common": "Schweden"},
                                  "est": {"official": "Rootsi Kuningriik", "common": "Rootsi"},
                                  "fin": {"official": "Ruotsin kuningaskunta", "common": "Ruotsi"},
                                  "fra": {"official": "Royaume de Suède", "common": "Suède"},
                                  "hrv": {"official": "Kraljevina Švedska", "common": "Švedska"},
                                  "hun": {"official": "Svéd Királyság", "common": "Svédország"},
                                  "ita": {"official": "Regno di Svezia", "common": "Svezia"},
                                  "jpn": {"official": "スウェーデン王国", "common": "スウェーデン"},
                                  "kor": {"official": "스웨덴 왕국", "common": "스웨덴"},
                                  "nld": {"official": "Koninkrijk Zweden", "common": "Zweden"},
                                  "per": {"official": "پادشاهی سوئد", "common": "سوئد"},
                                  "pol": {"official": "Królestwo Szwecji", "common": "Szwecja"},
                                  "por": {"official": "Reino da Suécia", "common": "Suécia"},
                                  "rus": {"official": "Королевство Швеция", "common": "Швеция"},
                                  "slk": {"official": "Švédske kráľovstvo", "common": "Švédsko"},
                                  "spa": {"official": "Reino de Suecia", "common": "Suecia"},
                                  "srp": {"official": "Краљевина Шведска", "common": "Шведска"},
                                  "swe": {"official": "Konungariket Sverige", "common": "Sverige"},
                                  "tur": {"official": "İsveç Krallığı", "common": "İsveç"},
                                  "urd": {"official": "مملکتِ سویڈن", "common": "سویڈن"},
                                  "zho": {"official": "瑞典王国", "common": "瑞典"}}, "latlng": [62.0, 15.0],
                 "landlocked": False, "borders": ["FIN", "NOR"], "area": 450295.0,
                 "demonyms": {"eng": {"f": "Swedish", "m": "Swedish"}, "fra": {"f": "Suédoise", "m": "Suédois"}},
                 "flag": "\uD83C\uDDF8\uD83C\uDDEA", "maps": {"googleMaps": "https://goo.gl/maps/iqygE491ADVgnBW39",
                                                              "openStreetMaps": "https://www.openstreetmap.org/relation/52822"},
                 "population": 10353442, "gini": {"2018": 30.0}, "fifa": "SWE",
                 "car": {"signs": ["S"], "side": "right"}, "timezones": ["UTC+01:00"], "continents": ["Europe"],
                 "flags": {"png": "https://flagcdn.com/w320/se.png", "svg": "https://flagcdn.com/se.svg",
                           "alt": "The flag of Sweden has a blue field with a large golden-yellow cross that extend to the edges of the field. The vertical part of this cross is offset towards the hoist side."},
                 "coatOfArms": {"png": "https://mainfacts.com/media/images/coats_of_arms/se.png",
                                "svg": "https://mainfacts.com/media/images/coats_of_arms/se.svg"},
                 "startOfWeek": "monday", "capitalInfo": {"latlng": [59.33, 18.05]},
                 "postalCode": {"format": "SE-### ##", "regex": "^(?:SE)*(\\d{5})$"}}]
        # return [
        #     {
        #         "name": {
        #             "common": "Sweden1",
        #             "official": "Kingdom of Sweden",
        #             "nativeName": {
        #                 "swe": {
        #                     "official": "Konungariket Sverige",
        #                     "common": "Sverige"
        #                 }
        #             }
        #         },
        #         "tld": [
        #             ".se"
        #         ],
        #         "cca2": "SE",
        #         "ccn3": "752",
        #         "cca3": "SWE",
        #         "cioc": "SWE",
        #         "independent": True,
        #         "status": "officially-assigned",
        #         "unMember": True,
        #         "currencies": {
        #             "SEK": {
        #                 "name": "Swedish krona",
        #                 "symbol": "kr"
        #             }
        #         },
        #         "idd": {
        #             "root": "+4",
        #             "suffixes": [
        #                 "6"
        #             ]
        #         },
        #         "capital": [
        #             "Stockholm"
        #         ],
        #         "altSpellings": [
        #             "SE",
        #             "Kingdom of Sweden",
        #             "Konungariket Sverige"
        #         ],
        #         "region": "Europe",
        #         "subregion": "Northern Europe",
        #         "languages": {
        #             "swe": "Swedish"
        #         },
        #         "translations": {
        #             "ara": {
        #                 "official": "مملكة السويد",
        #                 "common": "السويد"
        #             },
        #             "bre": {
        #                 "official": "Rouantelezh Sveden",
        #                 "common": "Sveden"
        #             },
        #             "ces": {
        #                 "official": "Švédské království",
        #                 "common": "Švédsko"
        #             },
        #             "cym": {
        #                 "official": "Kingdom of Sweden",
        #                 "common": "Sweden"
        #             },
        #             "deu": {
        #                 "official": "Königreich Schweden",
        #                 "common": "Schweden"
        #             },
        #             "est": {
        #                 "official": "Rootsi Kuningriik",
        #                 "common": "Rootsi"
        #             },
        #             "fin": {
        #                 "official": "Ruotsin kuningaskunta",
        #                 "common": "Ruotsi"
        #             },
        #             "fra": {
        #                 "official": "Royaume de Suède",
        #                 "common": "Suède"
        #             },
        #             "hrv": {
        #                 "official": "Kraljevina Švedska",
        #                 "common": "Švedska"
        #             },
        #             "hun": {
        #                 "official": "Svéd Királyság",
        #                 "common": "Svédország"
        #             },
        #             "ita": {
        #                 "official": "Regno di Svezia",
        #                 "common": "Svezia"
        #             },
        #             "jpn": {
        #                 "official": "スウェーデン王国",
        #                 "common": "スウェーデン"
        #             },
        #             "kor": {
        #                 "official": "스웨덴 왕국",
        #                 "common": "스웨덴"
        #             },
        #             "nld": {
        #                 "official": "Koninkrijk Zweden",
        #                 "common": "Zweden"
        #             },
        #             "per": {
        #                 "official": "پادشاهی سوئد",
        #                 "common": "سوئد"
        #             },
        #             "pol": {
        #                 "official": "Królestwo Szwecji",
        #                 "common": "Szwecja"
        #             },
        #             "por": {
        #                 "official": "Reino da Suécia",
        #                 "common": "Suécia"
        #             },
        #             "rus": {
        #                 "official": "Королевство Швеция",
        #                 "common": "Швеция"
        #             },
        #             "slk": {
        #                 "official": "Švédske kráľovstvo",
        #                 "common": "Švédsko"
        #             },
        #             "spa": {
        #                 "official": "Reino de Sucia",
        #                 "common": "Suecia"
        #             },
        #             "srp": {
        #                 "official": "Краљевина Шведска",
        #                 "common": "Шведска"
        #             },
        #             "swe": {
        #                 "official": "Konungariket Sverige",
        #                 "common": "Sverige"
        #             },
        #             "tur": {
        #                 "official": "İsveç Krallığı",
        #                 "common": "İsveç"
        #             },
        #             "urd": {
        #                 "official": "مملکتِ سویڈن",
        #                 "common": "سویڈن"
        #             },
        #             "zho": {
        #                 "official": "瑞典王国",
        #                 "common": "瑞典"
        #             }
        #         },
        #         "latlng": [
        #             62,
        #             15
        #         ],
        #         "landlocked": False,
        #         "borders": [
        #             "FIN",
        #             "NOR"
        #         ],
        #         "area": 450295,
        #         "demonyms": {
        #             "eng": {
        #                 "f": "Swedish",
        #                 "m": "Swedish"
        #             },
        #             "fra": {
        #                 "f": "Suédoise",
        #                 "m": "Suédoi"
        #             }
        #         },
        #         "flag": "🇸🇪",
        #         "maps": {
        #             "googleMaps": "https://goo.gl/maps/iqygE491ADVgnBW39",
        #             "openStreetMaps": "https://www.openstreetmap.org/relation/52822"
        #         },
        #         "population": 10353442,
        #         "gini": {
        #             "2018": 30
        #         },
        #         "fifa": "SWE",
        #         "car": {
        #             "signs": [
        #                 "S"
        #             ],
        #             "side": "right"
        #         },
        #         "timezones": [
        #             "UTC+01:00"
        #         ],
        #         "continents": [
        #             "Europe"
        #         ],
        #         "flags": {
        #             "png": "https://flagcdn.com/w320/se.png",
        #             "svg": "https://flagcdn.com/se.svg",
        #             "alt": "The flag of Sweden has a blue field with a large golden-yellow cross that extend to the edges of the field. The vertical part of this cross is offset towards the hoist side."
        #         },
        #         "coatOfArms": {
        #             "png": "https://mainfacts.com/media/images/coats_of_arms/se.png",
        #             "svg": "https://mainfacts.com/media/images/coats_of_arms/se.svg"
        #         },
        #         "startOfWeek": "monday",
        #         "capitalInfo": {
        #             "latlng": [
        #                 59.33,
        #                 18.05
        #             ]
        #         },
        #         "postalCode": {
        #             "format": "SE-### ##",
        #             "regex": "^(?:SE)*(\\d{5})$"
        #         }
        #     }
        # ]
