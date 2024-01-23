/* eslint-disable @typescript-eslint/no-explicit-any */

import axios, { AxiosInstance } from "axios";
import { AggregationType, StatsReponse, StatsRequest } from "../types/services";
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
      const params: { [key: string]: string } = {
        ...this.buildAggregationParms(request.aggregation),
        truncateDate: `sale_date=${request.period}`,
        groupBy: timeFieldName,
        county__in: request.counties.join(","),
        locality__in: request.localities.join(","),
        neighborhood__in: request.neighborhoods.join(","),
        street__in: request.streets.join(","),
        orderBy: timeFieldName,
      };
      const response = await this.http.get(this.baseURL, { params });
      const timeSeries = response.data.map((item: any) => {
        return {
          time: moment(item[timeFieldName]).format("YYYY"),
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
