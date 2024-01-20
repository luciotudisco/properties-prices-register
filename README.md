# Properties Prices Register

![CI/CD](https://github.com/luciotudisco/properties-prices-register/actions/workflows/main.yml/badge.svg)

The service provides information on residential properties purchased in
Ireland since January 1, 2010. The data is sourced from the Residential
Property Price Register, which is produced by the Property Services
Regulatory Authority (PSRA).

The available data includes the Date of Sale, Price, and Address. The raw
data obtained from the Residential Property Price Register is enhanced with
additional details obtained through the third-party geocode
API [True Way Api](https://truewayapi.com/).

## API

### Properties List

The service provides a paginated list of properties through a GET API.

It supports query filters such as county, locality, neighborhood, price,
and sale date.

[https://api.irishpropertiesprices.com/v1/properties](https://api.irishpropertiesprices.com/v1/properties)

The API supports the following query filters:

- county (e.g. `county=Dublin`, `county=Kildare`, etc.)
- locality (e.g. `locality=Naas`, `locality=Bray`, etc.)
- neighborhood (e.g. `neighborhood=Ballsbridge`, `locality=Drumcondra`, etc.)
- price (e.g. `price__gte=1000000`, `price__lte=50000`, etc.)
- sale_date (e.g. `sale_date__gte=2023-01-01`, `sale_date__lte=2012-01-01`, etc.)

#### Paginated list of all properties

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties'
```

#### Paginated list of properties for a given county

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties?county=Kildare'
```

#### Paginated list of properties for a given locality

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties?locality=Naas'
```

#### Paginated list of properties sold within a given time frame

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/?sale_date__gte=2023-12-20&sale_date__lte=2023-12-21'
```

#### Paginated list of properties sold for a price within a given range

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/?price__gte=20000&price__lte=50000'
```

### Properties Stats

The service offers aggregated statistics about sold properties through a GET API.

[https://api.irishpropertiesprices.com/v1/properties/stats](https://api.irishpropertiesprices.com/v1/properties/stats)

Key features:

- Supports multiple ggregations, such as count, percentile, max, min, average
- Allows grouping by multiple fields.
- Provides the ability to limit the number of displayed records.
- Offers filtering capabilities based on criteria such as county, locality,
  neighborhood, sale date, and price.

#### Median sale price grouped by county and year

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/stats?aggregation=percentile&aggregationField=price&percentile=0.5&truncateDate=sale_date=year&groupBy=sale_date__trunc__year,county'
```

#### Median sale price by neighbourhood in Dublin in 2023

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/stats?aggregation=percentile&aggregationField=price&percentile=0.5&groupBy=neighborhood&county=Dublin&sale_date__gte=2023-01-01&sale_date__lte=2024-01-01&orderBy=-value'
```

#### Top 10 neighbourhoods by number of sold properties in Dublin in 2023

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/stats?aggregation=count&groupBy=neighborhood&county=Dublin&sale_date__gte=2023-01-01&sale_date__lte=2024-01-01&limit=10&orderBy=-value'
```

#### Top 10 streets by median sale price in Dublin

```shell
curl --location --request GET 'https://api.irishpropertiesprices.com/v1/properties/stats?aggregation=percentile&aggregationField=price&percentile=0.5&groupBy=street&county=Dublin&limit=10&orderBy=-value'
```

## UI

An algolia-backed UI with the available data can be found at [https://irishpropertiesprices.com/](https://irishpropertiesprices.com/)
