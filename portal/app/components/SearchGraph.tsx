/* eslint-disable @typescript-eslint/no-explicit-any */

import { useCurrentRefinements } from "react-instantsearch";
import { useEffect, useState } from "react";
import StatsService from "../services/stats.service";
import {
  AggregationType,
  AggregationPeriod,
  StatsRecord,
} from "../types/services";
import { Box, Flex, LoadingOverlay, Text, Title } from "@mantine/core";
import { LineChart } from "@mantine/charts";

const statsService = new StatsService();

const SearchGraph = function (): JSX.Element {
  const { items } = useCurrentRefinements();
  const [aggregation] = useState<AggregationPeriod>(AggregationPeriod.YEAR);
  const [pricesStats, setPricesStats] = useState<StatsRecord[]>([]);
  const [countStats, setCountStats] = useState<StatsRecord[]>([]);
  const [hasError, setHasError] = useState(false);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const counties = getRefinements(items, "county");
      const localities = getRefinements(items, "locality");
      const neighborhoods = getRefinements(items, "neighborhood");
      const streets = getRefinements(items, "street");
      const saleYears = getRefinements(items, "sale_year");

      const pricesData = await statsService.getStats({
        aggregation: AggregationType.MEDIAN_PRICE,
        counties,
        localities,
        neighborhoods,
        streets,
        saleYears,
        period: aggregation,
      });
      setPricesStats(pricesData.data);

      const countsData = await statsService.getStats({
        aggregation: AggregationType.COUNT,
        counties,
        localities,
        neighborhoods,
        streets,
        saleYears,
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
      setHasError(false);
      setLoading(true);
      fetchData();
    } catch (error) {
      setHasError(true);
    } finally {
      setLoading(false);
    }
  }, [items, aggregation]);

  if (isLoading) return <LoadingOverlay />;

  if (hasError)
    return (
      <Box className="flex h-full w-full items-center align-middle justify-center">
        <Text size="md">Oops! Something went wrong!</Text>
      </Box>
    );

  return (
    <Flex direction="column" gap="lg">
      <Flex direction="column" className="w-full">
        <Title order={2} className="py-10 text-sm uppercase">
          Median price
        </Title>
        <LineChart
          data={pricesStats}
          className="text-xs"
          h={300}
          dataKey="time"
          withLegend={false}
          series={[{ name: "value", color: "red" }]}
          valueFormatter={(v) =>
            new Intl.NumberFormat("en", { notation: "compact" }).format(v)
          }
        />
      </Flex>
      <Flex direction="column" className="w-full">
        <Title order={2} className="py-10 text-sm uppercase">
          Number of properties sold
        </Title>
        <LineChart
          data={countStats}
          className="text-xs"
          h={300}
          dataKey="time"
          withLegend={false}
          valueFormatter={(v) =>
            new Intl.NumberFormat("en", { notation: "compact" }).format(v)
          }
          series={[{ name: "value", color: "red" }]}
        />
      </Flex>
    </Flex>
  );
};

export default SearchGraph;
