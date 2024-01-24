/* eslint-disable @typescript-eslint/no-explicit-any */

import { useCurrentRefinements } from "react-instantsearch";
import { useEffect, useState } from "react";
import {
  Box,
  CircularProgress,
  Grid,
  MenuItem,
  Select,
  Typography,
} from "@mui/material";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import StatsService from "../services/stats.service";
import {
  AggregationType,
  AggregationPeriod,
  StatsRecord,
} from "../types/services";

const statsService = new StatsService();

const SearchGraph = function (): JSX.Element {
  const { items } = useCurrentRefinements();
  const [aggregation, setAggregation] = useState<AggregationPeriod>(
    AggregationPeriod.YEAR,
  );
  const [pricesStats, setPricesStats] = useState<StatsRecord[]>([]);
  const [countStats, setCountStats] = useState<StatsRecord[]>([]);
  const [isLoading, setLoading] = useState(true);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const counties = getRefinements(items, "county");
      const localities = getRefinements(items, "locality");
      const neighborhoods = getRefinements(items, "neighborhood");
      const streets = getRefinements(items, "street");
      const sale_years = getRefinements(items, "sale_year");

      const pricesData = await statsService.getStats({
        aggregation: AggregationType.MEDIAN_PRICE,
        counties,
        localities,
        neighborhoods,
        streets,
        sale_years,
        period: aggregation,
      });
      setPricesStats(pricesData.data);

      const countsData = await statsService.getStats({
        aggregation: AggregationType.COUNT,
        counties,
        localities,
        neighborhoods,
        streets,
        sale_years,
        period: aggregation,
      });
      setCountStats(countsData.data);
    };

    const getRefinements = (items: any, attribute: string) => {
      const item = items.find((item: any) => item.attribute == attribute);
      if (!item) {
        return [];
      }
      return item.refinements.map((refinement: any) => refinement.value) || [];
    };

    try {
      if (isLoading) {
        return;
      }
      setHasError(false);
      setLoading(true);
      fetchData();
    } catch (error) {
      setHasError(true);
    } finally {
      setLoading(false);
    }
  }, [items, aggregation]);

  if (isLoading)
    return (
      <Box className="flex h-full w-full items-center align-middle justify-center">
        <CircularProgress />
      </Box>
    );

  if (hasError)
    return (
      <Box className="flex h-full w-full items-center align-middle justify-center">
        <Typography fontSize="medium" variant="body2">
          Oops! Something went wrong!
        </Typography>
      </Box>
    );

  return (
    <Grid container className="h-full w-full p-5">
      <Grid
        item
        xs={12}
        className="w-full flex justify-center align-middle items-center"
      >
        <Select
          value={aggregation}
          defaultValue={AggregationPeriod.YEAR}
          onChange={(event) =>
            setAggregation(event.target.value as AggregationPeriod)
          }
          disabled={isLoading}
          variant="outlined"
          label="Time aggregation"
          className="w-min-60"
          size="small"
        >
          <MenuItem value={AggregationPeriod.YEAR}>Yearly</MenuItem>
          <MenuItem value={AggregationPeriod.MONTH}>Monthly</MenuItem>
        </Select>
      </Grid>
      <Grid item xs={12} className="w-full h-full pb-10 max-h-96">
        <Typography className="font-mono py-10 font-bold text-sm" variant="h2">
          Median price
        </Typography>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            syncId="yearly-charts"
            data={pricesStats}
            className="text-xs font-mono"
            margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis
              dataKey="value"
              tickFormatter={(v) =>
                new Intl.NumberFormat("en", { notation: "compact" }).format(v)
              }
            />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
            <Tooltip />
          </LineChart>
        </ResponsiveContainer>
      </Grid>
      <Grid item xs={12} className=" w-full h-full pt-10 max-h-96">
        <Typography className="font-mono py-10 font-bold  text-sm" variant="h2">
          Number of properties sold
        </Typography>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            syncId="yearly-charts"
            data={countStats}
            className="text-xs font-mono"
            margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis
              dataKey="value"
              tickFormatter={(v) =>
                new Intl.NumberFormat("en", { notation: "compact" }).format(v)
              }
            />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
            <Tooltip
              labelFormatter={(value) => {
                return `label: ${value}`;
              }}
            />
          </LineChart>
        </ResponsiveContainer>
      </Grid>
    </Grid>
  );
};

export default SearchGraph;
