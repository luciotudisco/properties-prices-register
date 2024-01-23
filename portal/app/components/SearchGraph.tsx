/* eslint-disable @typescript-eslint/no-explicit-any */

import { useCurrentRefinements } from "react-instantsearch";
import { useEffect, useState } from "react";
import { Box, CircularProgress, Grid, Typography } from "@mui/material";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import moment from "moment";

const SearchGraph = function (): JSX.Element {
  const { items } = useCurrentRefinements();
  const [pricesStats, setPricesStats] = useState([]);
  const [countStats, setCountStats] = useState([]);
  const [isLoading, setLoading] = useState(true);

  const fetchStats = async (
    aggregation: { [key: string]: string },
    counties: string[],
    localities: string[],
    neighborhoods: string[],
    sreets: string[],
  ) => {
    const url = new URL(
      "https://api.irishpropertiesprices.com/v1/properties/stats",
    );
    const params: { [key: string]: string } = {
      ...aggregation,
      truncateDate: "sale_date=year",
      groupBy: "sale_date__trunc__year",
      county__in: counties.join(","),
      locality__in: localities.join(","),
      neighborhood__in: neighborhoods.join(","),
      street__in: sreets.join(","),
      orderBy: "sale_date__trunc__year",
    };
    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key]),
    );
    const response = await fetch(url);
    const data = response.json();
    return data;
  };

  const extractRefinementsValues = (items: any[], attribute: string) => {
    return (
      items
        .find((item) => item.attribute == attribute)
        ?.refinements.map((refinement: any) => refinement.value as string) || []
    );
  };

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const counties = extractRefinementsValues(items, "county");
      const localities = extractRefinementsValues(items, "locality");
      const neighborhoods = extractRefinementsValues(items, "neighborhood");
      const streets = extractRefinementsValues(items, "street");

      const medianPricesAggregation = {
        aggregation: "percentile",
        aggregationField: "price",
        percentile: "0.5",
      };
      const pricesData = await fetchStats(
        medianPricesAggregation,
        counties,
        localities,
        neighborhoods,
        streets,
      );
      setPricesStats(pricesData);

      const countAggregation = { aggregation: "count" };
      const countsData = await fetchStats(
        countAggregation,
        counties,
        localities,
        neighborhoods,
        streets,
      );
      setCountStats(countsData);

      setLoading(false);
    };

    fetchData();
  }, [items]);

  if (isLoading)
    return (
      <Box className="flex h-full w-full items-center align-middle justify-center">
        <CircularProgress />
      </Box>
    );

  return (
    <Grid container className="h-full w-full" spacing={20}>
      <Grid item xs={12} className=" w-full h-full">
        <Typography className="font-mono py-10 font-bold">
          Median price by year
        </Typography>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            syncId="yearly-charts"
            data={pricesStats}
            className="text-xs font-mono"
            margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="sale_date__trunc__year"
              tickFormatter={(tick) =>
                moment(tick, "YYYY-MM-DD").format("YYYY")
              }
            />
            <YAxis
              dataKey="value"
              tickFormatter={(value) =>
                new Intl.NumberFormat("en", { notation: "compact" }).format(
                  value,
                )
              }
            />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
          </LineChart>
        </ResponsiveContainer>
      </Grid>
      <Grid item xs={12} className=" w-full h-full">
        <Typography className="font-mono py-10 font-bold">
          Number of properties sold by year
        </Typography>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            syncId="yearly-charts"
            data={countStats}
            className="text-xs font-mono"
            margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="sale_date__trunc__year"
              tickFormatter={(tick) =>
                moment(tick, "YYYY-MM-DD").format("YYYY")
              }
            />
            <YAxis
              dataKey="value"
              tickFormatter={(value) =>
                new Intl.NumberFormat("en").format(value)
              }
            />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
          </LineChart>
        </ResponsiveContainer>
      </Grid>
    </Grid>
  );
};

export default SearchGraph;
