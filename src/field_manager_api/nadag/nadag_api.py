from shapely.geometry import Polygon
import requests
import pandas as pd

NADAG_URL_utvidet = "https://ogcapitest.ngu.no/rest/services/grunnundersokelser_utvidet"

NADAG_URL = "https://ogcapitest.ngu.no/rest/services/grunnundersokelser"
# NADAG_URL ikke utvidet funker bedre, har endepunkter med data på seg
# TODO
# Legge til data på borhull objectet som fetches fra apiene på href,
# validere det mange har ikke data på seg
# Legge til tolkning av filen som hentes fra href
# Kun lagre tolkningen


def get_nadag_geotekniskborehull():
    url = f"{NADAG_URL}/collections/geotekniskborehull/items"
    return url


def get_nadag_geotekniskborehullunders():
    url = f"{NADAG_URL}/collections/geotekniskborehullunders/items"
    return url


def get_nadag_geoteknisktolketlag():
    url = f"{NADAG_URL}/collections/geoteknisktolketlag/items"
    return url


def get_nadag_grunnvanndata():
    url = f"{NADAG_URL}/collections/grunnvanndata/items"
    return url


def get_nadag_document():
    url = f"{NADAG_URL}/collections/geotekniskdokument/items"
    return url


def _calculate_bbox_from_polygon(polygon: Polygon) -> str:
    """
    Calculate the bounding box from a Polygon object.
    """
    x_min, y_min, x_max, y_max = polygon.bounds
    return f"{x_min},{y_min},{x_max},{y_max}"


def fetch_geotechnical_borehole_data(
    url: str,
    polygon_lon_lat: Polygon,
    bbox_crs="http://www.opengis.net/def/crs/OGC/1.3/CRS84",
    crs="http://www.opengis.net/def/crs/OGC/1.3/CRS84",
    filter_crs="http://www.opengis.net/def/crs/OGC/1.3/CRS84",
    filter_lang="cql2-text",
    limit=100,
    max_allowable_offset=0.05,
    offset=0,
    skip_geometry=False,
):
    params = {
        "bbox": _calculate_bbox_from_polygon(polygon_lon_lat),
        "bbox-crs": bbox_crs,
        "crs": crs,
        "filter-crs": filter_crs,
        "filter-lang": filter_lang,
        "limit": limit,
        "maxAllowableOffset": max_allowable_offset,
        "offset": offset,
        "skipGeometry": str(skip_geometry).lower(),
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response


class NadagGeotekniskBorehullUnders:
    def __init__(self, data):
        self.geometry = data.get("geometry", {})
        self.boret_lengde = data["properties"].get("boretLengde", None)
        self.boret_lengde_til_berg = (
            data["properties"]
            .get("boretLengdeTilBerg", {})
            .get("borlengdeTilBerg", None)
        )
        self.hoyde = data["properties"].get("høyde", None)
        self.stoppkode = data["properties"].get("stoppKode", None)
        self.geoteknisk_metode = data["properties"].get("geotekniskMetode", None)
        self.metode = self.extract_metode(data["properties"])

    def extract_metode(self, properties):
        metode_data = {}
        for key, value in properties.items():
            if key.startswith("metode-"):
                metode_data[key] = self.modify_href(value)
        return metode_data

    def modify_href(self, metode_list):
        if self.geoteknisk_metode in [
            1,
            2,
            15,
        ]:  # Check if geoteknisk_metode is 1, 2, or 15
            for metode in metode_list:
                if self.geoteknisk_metode == 15:
                    metode["href"] += (
                        "?KombinasjsSondering=" + metode["title"]
                    )  # Modify URL for geoteknisk_metode = 15
                else:
                    metode["href"] += (
                        "?SomeOtherQuery=" + metode["title"]
                    )  # You can adjust this for other methods
        return metode_list

    def fetch_data(self):
        pass

    def __repr__(self):
        return (
            f"BoreholeData(geometry={self.geometry}, boret_lengde={self.boret_lengde}, "
            f"boret_lengde_til_berg={self.boret_lengde_til_berg}, høyde={self.hoyde}, "
            f"stoppkode={self.stoppkode}, geoteknisk_metode={self.geoteknisk_metode}, metode={self.metode})"
        )


class NadagGeotekniskBorehullUndersWithFetch:
    def __init__(self, data):
        self.geometry = data.get("geometry", {})
        self.boret_lengde = data["properties"].get("boretLengde", None)
        self.boret_lengde_til_berg = (
            data["properties"]
            .get("boretLengdeTilBerg", {})
            .get("borlengdeTilBerg", None)
        )
        self.hoyde = data["properties"].get("høyde", None)
        self.stoppkode = data["properties"].get("stoppKode", None)
        self.geoteknisk_metode = data["properties"].get("geotekniskMetode", None)
        self.metode = self.extract_metode(data["properties"])
        self.data = None  # Initialize _data as None to delay fetching

    def extract_metode(self, properties):
        url = None
        for key, value in properties.items():
            if key.startswith("metode-"):
                return value[0]["href"]
        return url

    def fetch_data(self):
        # Fetch the data only when called and assign it to the instance
        if self.data is None and self.metode:
            print(f"Fetching data for borehole with method {self.metode}")
            response = requests.get(self.metode)
            response.raise_for_status()
            response_json = response.json()
            features = response_json.get("properties", [])
            if not features:
                return
            for key, items in features.items():
                if "observasjon" in key.lower():
                    if not items:
                        return
                    self.data = pd.DataFrame(items)  # Assign data to the instance
                    return
        return self.data

    def predict(self):
        if self.data is None:
            return
        # Do some prediction based on the data
        pass

    def __repr__(self):
        return (
            f"BoreholeData(geometry={self.geometry}, boret_lengde={self.boret_lengde}, "
            f"boret_lengde_til_berg={self.boret_lengde_til_berg}, høyde={self.hoyde}, "
            f"stoppkode={self.stoppkode}, geoteknisk_metode={self.geoteknisk_metode}, metode={self.metode})"
        )


class GroundwaterData:
    def __init__(self, data):
        self.geometry = data.get("geometry", None)
        self.male_dato = data["properties"].get("måleDato", None)
        self.male_tidspunkt = data["properties"].get("måleTidspunkt", None)
        self.boret_lengde = data["properties"].get("boretLengde", None)
        self.grunnvann_observasjonskode = data["properties"].get(
            "grunnvannObservasjonKode", None
        )
        self.er_gyldig = data["properties"].get("erGyldig", None)
        self.grunnvannmaling_id = data["properties"].get("grunnvannmaling", None)
        self.tilhorer_grunnvannmaling = self.modify_url(
            data["properties"].get("tilhørerGrunnvannmaling", {})
        )

    def modify_url(self, tilhører_data):
        if "href" in tilhører_data:
            href = tilhører_data["href"]
            grundvanns_id = href.split("/")[
                -1
            ]  # Extract the last part of the URL (the ID)
            modified_href = (
                href.split("items")[0] + f"items?grunnvannmaling={grundvanns_id}"
            )
            return {"title": tilhører_data.get("title"), "href": modified_href}
        return {}

    def __repr__(self):
        return (
            f"GroundwaterData(geometry={self.geometry}, måle_dato={self.male_dato}, "
            f"måle_tidspunkt={self.male_tidspunkt}, boret_lengde={self.boret_lengde}, "
            f"grunnvann_observasjonskode={self.grunnvann_observasjonskode}, er_gyldig={self.er_gyldig}, "
            f"grunnvannmaling_id={self.grunnvannmaling_id}, tilhører_grunnvannmaling={self.tilhorer_grunnvannmaling})"
        )


class NadagGeotekniskUnders:
    def __init__(self, data):
        self.geometry = data.get("geometry", {})
        self.bore_nr = data["properties"].get("boreNr", None)
        self.antall_borehull_undersokelser = data["properties"].get(
            "antallBorehullUndersøkelser", None
        )
        self.kvikkleire_påvisning = data["properties"].get("kvikkleirePåvisning", None)
        self.maks_boret_lengde = data["properties"].get("maksBoretLengde", None)
        self.har_undersokelse = self.extract_links(
            data["properties"].get("harUndersøkelse", [])
        )
        self.unders_omr = self.extract_links(data["properties"].get("undersOmr", []))
        self.har_dokument = self.extract_links(
            data["properties"].get("harDokument", [])
        )

    def extract_links(self, link_list):
        return [
            item["href"].replace("/items/", "/items/?Grunnvannsmåling=") + item["title"]
            for item in link_list
        ]

    def __repr__(self):
        return (
            f"GeotekniskUnders(geometry={self.geometry}, bore_nr={self.bore_nr}, "
            f"antall_borehull_undersokelser={self.antall_borehull_undersokelser}, kvikkleire_påvisning={self.kvikkleire_påvisning}, "
            f"maks_boret_lengde={self.maks_boret_lengde}, har_undersokelse={self.har_undersokelse}, "
            f"unders_omr={self.unders_omr}, har_dokument={self.har_dokument})"
        )


def handel_geotekniskborehullunders(
    response: requests.models.Response,
    borehole_response: NadagGeotekniskBorehullUnders,
    fetch: bool = False,
):
    data = response.json()
    features = data.get("features", [])
    if not features:
        return features
    borehull = []
    for data in features:
        borehole = borehole_response(data)
        print("appending borehole")
        borehull.append(borehole)
        if fetch:
            print("fetching data")
            borehole.fetch_data()
    return borehull


def examples():
    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [11.218124, 60.06172],
                    [11.223337, 60.061436],
                    [11.223992, 60.058411],
                    [11.216654, 60.058781],
                    [11.216976, 60.061538],
                    [11.218124, 60.06172],
                ]
            ],
        },
    }

    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [10.83046, 59.902062],
                    [10.829526, 59.901239],
                    [10.829129, 59.901368],
                    [10.82899, 59.901901],
                    [10.829419, 59.902245],
                    [10.83032, 59.902164],
                    [10.83046, 59.902062],
                ]
            ],
        },
    }

    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [10.705351, 59.931692],
                    [10.704503, 59.930716],
                    [10.705522, 59.930385],
                    [10.706048, 59.931444],
                    [10.705351, 59.931692],
                ]
            ],
        },
    }
    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [10.833743, 59.901664],
                    [10.836682, 59.901486],
                    [10.83636, 59.899496],
                    [10.832884, 59.899625],
                    [10.833743, 59.901664],
                ]
            ],
        },
    }

    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [10.832391, 59.895723],
                    [10.833979, 59.89574],
                    [10.833828, 59.896391],
                    [10.831811, 59.897445],
                    [10.830621, 59.896859],
                    [10.832251, 59.895707],
                    [10.832391, 59.895723],
                ]
            ],
        },
    }

    data = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [10.545223, 59.901648],
                    [10.549428, 59.903536],
                    [10.551467, 59.903095],
                    [10.546478, 59.901131],
                    [10.545223, 59.901648],
                ]
            ],
        },
    }
    polygon = Polygon(data["geometry"]["coordinates"][0])

    response_gru = fetch_geotechnical_borehole_data(
        get_nadag_geotekniskborehullunders(), polygon
    )

    response_document = fetch_geotechnical_borehole_data(get_nadag_document(), polygon)

    data = response_gru.json().get("features", [])

    response_gru_påvisning = fetch_geotechnical_borehole_data(
        get_nadag_geotekniskborehull(), polygon
    )
    response_water = fetch_geotechnical_borehole_data(
        get_nadag_grunnvanndata(), polygon
    )

    borehole_more_data = handel_geotekniskborehullunders(
        response_gru, NadagGeotekniskBorehullUnders
    )

    borehole_data = handel_geotekniskborehullunders(
        response_gru_påvisning, NadagGeotekniskUnders
    )

    borehole_with_url = handel_geotekniskborehullunders(
        response_gru, NadagGeotekniskBorehullUndersWithFetch, fetch=True
    )

    features = response_gru.json().get("features", [])[0]
