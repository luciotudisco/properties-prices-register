export enum AggregationPeriod {
  YEAR = "year",
  MONTH = "month",
}

export enum AggregationType {
  COUNT = "count",
  MEDIAN_PRICE = "median_price",
}

export interface StatsRequest {
  aggregation: AggregationType;
  counties: string[];
  localities: string[];
  neighborhoods: string[];
  streets: string[];
  saleYears: number[];
  period: AggregationPeriod;
}

export interface StatsRecord {
  value: number;
  time: string;
}

export interface StatsReponse {
  data: StatsRecord[];
}
