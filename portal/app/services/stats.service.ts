/* eslint-disable @typescript-eslint/no-explicit-any */

import axios, { AxiosInstance } from "axios";
import {
  AggregationPeriod,
  AggregationType,
  StatsReponse,
  StatsRequest,
} from "../types/services";
import moment from "moment";

/**
 * Service for retrieving statistics related to properties.
 */
class StatsService {
  private http: AxiosInstance;
  private baseURL = "https://api.irishpropertiesprices.com/v1/properties/stats";

  constructor() {
    this.http = axios.create({
      baseURL: this.baseURL,
      withCredentials: false,
    });
  }

  /**
   * Retrieves statistics based on the provided request parameters.
   * @param request - The request object containing the parameters for the statistics.
   * @returns A promise that resolves to a response object containing the retrieved statistics.
   * @throws If an error occurs while retrieving the statistics.
   */
  public async getStats(request: StatsRequest): Promise<StatsReponse> {
    try {
      const timeFieldName = `sale_date__trunc__${request.period}`;
      const max_sale_year =
        request.saleYears.length > 0
          ? Math.max(...request.saleYears)
          : new Date().getFullYear();
      const min_sale_year =
        request.saleYears.length > 0 ? Math.min(...request.saleYears) : "2010";
      const params: { [key: string]: string } = {
        ...this.buildAggregationParms(request.aggregation),
        truncateDate: `sale_date=${request.period}`,
        groupBy: timeFieldName,
        county__in: request.counties.join(","),
        locality__in: request.localities.join(","),
        neighborhood__in: request.neighborhoods.join(","),
        street__in: request.streets.join(","),
        sale_date__gte: `${min_sale_year}-01-01`,
        sale_date__lte: `${max_sale_year}-12-31`,
        orderBy: timeFieldName,
      };
      const response = await this.http.get(this.baseURL, { params });
      const timeFormat =
        request.period === AggregationPeriod.YEAR ? "YYYY" : "YYYY-MM";
      const timeSeries = response.data.map((item: any) => {
        return {
          time: moment(item[timeFieldName]).format(timeFormat),
          value: item.value,
        };
      });
      return { data: timeSeries };
    } catch (error) {
      return Promise.reject(error);
    }
  }

  private buildAggregationParms(aggregation_type: AggregationType): {
    [key: string]: string;
  } {
    switch (aggregation_type) {
      case AggregationType.COUNT:
        return { aggregation: "count" };
      case AggregationType.MEDIAN_PRICE:
        return {
          aggregation: "percentile",
          aggregationField: "price",
          percentile: "0.5",
        };
      default:
        throw new Error(`Invalid aggregation ${aggregation_type}`);
    }
  }
}

export { StatsService as default };
